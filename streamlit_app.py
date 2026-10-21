import json
import random
import re
import time
from io import BytesIO
from pathlib import Path

import streamlit as st
from gtts import gTTS

# ──────────────────────────────────────────────────────────────────────────────
# Page configuration
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP & CRME Hospitality Masterclass",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

XP_PER_CORRECT = 10
LETTERS = "ABCDEFGH"
EXAM_SECTION_SECONDS = 110 * 60  # SHRM-CP: two 110-minute testing sections
MODE_STUDY = "📚 Study mode (instant feedback)"
MODE_EXAM = "⏱️ Exam simulation (timed, no feedback)"

st.markdown(
    """
    <style>
    @keyframes fadeIn {
        0%   { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .stApp {
        background: linear-gradient(135deg, #0a192f 0%, #172a45 50%, #1f4068 100%);
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    header[data-testid="stHeader"] { background: transparent; }

    /* Question card (container created with key="qcard") */
    .st-key-qcard {
        animation: fadeIn 0.5s ease-out;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(100, 255, 218, 0.3) !important;
        border-radius: 16px;
        padding: 14px 18px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    }

    .hero-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 26px 30px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-bottom: 18px;
    }
    .hero-header h1 { margin: 0; font-size: 28px; font-weight: 700; color: #ffffff; }
    .hero-header p  { margin: 8px 0 0 0; font-size: 15px; color: #cbd5e1; }

    /* Buttons */
    .stButton > button {
        border-radius: 10px;
        font-weight: 700;
        letter-spacing: 0.4px;
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton > button:hover:not(:disabled) {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(0, 180, 216, 0.55);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%);
        color: #ffffff;
        border: none;
    }

    /* Answer choices */
    .stRadio label p { font-size: 16px; font-weight: 500; }

    section[data-testid="stSidebar"] {
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ──────────────────────────────────────────────────────────────────────────────
# Data loading & validation
# ──────────────────────────────────────────────────────────────────────────────
ITEM_PREFIX_RE = re.compile(r"^\s*\[[^\]]*#\d+\]\s*")  # e.g. "[SHRM-CP Exam Prep Item #16] "
OPTION_PREFIX_RE = re.compile(r"^\s*[A-Ha-h][\)\.:]\s*")  # e.g. "A) "


def _normalize(raw: dict, idx: int) -> dict:
    options = [OPTION_PREFIX_RE.sub("", str(o)).strip() for o in raw["options"]]
    correct = int(raw["correct"])
    if len(options) < 2 or not 0 <= correct < len(options):
        raise ValueError("options/correct index are inconsistent")
    return {
        "uid": idx,  # unique key for session state, independent of the JSON "id"
        "id": raw.get("id", idx + 1),
        "type": raw.get("type", "Knowledge Item"),
        "chapter": raw.get("chapter", "Hospitality Operations"),
        "category": raw.get("category", "Behavioral Competency"),
        "domain": raw.get("domain", ""),
        "competency": raw.get("competency", "Business Acumen"),
        "topic": raw.get("topic") or raw.get("competency", "Business Acumen"),
        "scenario": ITEM_PREFIX_RE.sub("", str(raw["scenario"])).strip(),
        "options": options,
        "correct": correct,  # index within the ORIGINAL option order
        "explanation": str(raw.get("explanation", "")).strip(),
        "memory_anchor": str(
            raw.get(
                "memory_anchor",
                "Think of this like balancing resort shifts during peak guest arrivals.",
            )
        ).strip(),
    }


@st.cache_data(show_spinner=False)
def load_questions():
    """Returns (questions, warnings, fatal_error)."""
    candidates = [Path(__file__).with_name("questions.json"), Path("questions.json")]
    path = next((p for p in candidates if p.exists()), None)
    if path is None:
        return [], [], "`questions.json` not found in the repository."
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [], [], f"Syntax error in `questions.json` at line {e.lineno}: {e.msg}"

    questions, warnings = [], []
    for i, raw in enumerate(data):
        try:
            questions.append(_normalize(raw, i))
        except (KeyError, TypeError, ValueError) as e:
            warnings.append(f"Skipped entry #{i + 1}: {e}")
    return questions, warnings, None


questions, load_warnings, fatal_error = load_questions()
Q_BY_UID = {q["uid"]: q for q in questions}

TYPE_FILTERS = {
    "All items": lambda q: True,
    "Knowledge Items only": lambda q: "situational" not in q["type"].lower(),
    "Situational Judgment (SJI) only": lambda q: "situational" in q["type"].lower(),
    "Behavioral Competencies only": lambda q: q["category"].startswith("Behavioral"),
    "HR Knowledge Domains only": lambda q: q["category"].startswith("HR"),
}


# ──────────────────────────────────────────────────────────────────────────────
# Text-to-speech helpers
# ──────────────────────────────────────────────────────────────────────────────
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\uFE0F\u200d]+")
SPEECH_FIXES = [
    (r"\bNLRA\b", "N L R A"),
    (r"\bFLSA\b", "F L S A"),
    (r"\bFMLA\b", "F M L A"),
    (r"\bEEOC\b", "E E O C"),
    (r"\bADA\b", "A D A"),
    (r"\bSHRM\b", "S H R M"),
    (r"\bCP\b", "C P"),
    (r"\bHR\b", "H R"),
    (r"\bDEI\b", "D E I"),
    (r"\bSJI\b", "S J I"),
    (r"\bBCG\b", "B C G"),
    (r"\bRIF\b", "R I F"),
    (r"\bLOTO\b", "low-toe"),
    (r"\bADDIE\b", "addy"),
    (r"\bPESTLE\b", "pestle"),
    (r"\bVII\b", "seven"),
    (r"(\d)\(([A-Za-z0-9]+)\)", r"\1 \2"),  # "5(a)(1)" -> "5 a 1"
    (r"\(([A-Za-z0-9]+)\)", r" \1"),
    (r"\s*&\s*", " and "),
    (r"\s+/\s+|/", ", "),
]


def clean_for_speech(text: str) -> str:
    text = EMOJI_RE.sub("", text)
    for pattern, repl in SPEECH_FIXES:
        text = re.sub(pattern, repl, text)
    return re.sub(r"\s+", " ", text).strip()


def _sentence(text: str) -> str:
    text = text.strip()
    return text if text.endswith((".", "!", "?", ":")) else text + "."


def question_speech(q: dict, perm: list, number: int, total: int) -> str:
    parts = [f"Question {number} of {total}.", _sentence(q["scenario"])]
    for pos, orig in enumerate(perm):
        parts.append(f"Option {LETTERS[pos]}. {_sentence(q['options'][orig])}")
    return clean_for_speech(" ".join(parts))


def explanation_speech(q: dict, perm: list, was_correct: bool) -> str:
    letter = LETTERS[perm.index(q["correct"])]
    verdict = "Correct." if was_correct else "Incorrect."
    parts = [
        verdict,
        f"The best answer is option {letter}. {_sentence(q['options'][q['correct']])}",
        _sentence(q["explanation"]),
        "Memory anchor. " + _sentence(q["memory_anchor"]),
    ]
    return clean_for_speech(" ".join(parts))


@st.cache_data(show_spinner=False, max_entries=300)
def synthesize(text: str, slow: bool, tld: str) -> bytes:
    buf = BytesIO()
    gTTS(text=text, lang="en", slow=slow, tld=tld).write_to_fp(buf)
    return buf.getvalue()


# ──────────────────────────────────────────────────────────────────────────────
# Session state: deck building, navigation, audio queue
# ──────────────────────────────────────────────────────────────────────────────
def build_deck(pool_uids=None, force_study=False):
    """(Re)build a study deck with shuffled question order and shuffled answer choices."""
    exam = st.session_state.get("mode", MODE_STUDY) == MODE_EXAM and not force_study
    if pool_uids is None:
        if exam:  # full-length simulation always uses the whole bank
            pool_uids = [q["uid"] for q in questions]
        else:
            keep = TYPE_FILTERS[st.session_state.get("type_filter", "All items")]
            pool_uids = [q["uid"] for q in questions if keep(q)]
    deck = list(pool_uids)
    if st.session_state.get("shuffle_q", True):
        random.shuffle(deck)

    perms = {}
    for uid in deck:
        order = list(range(len(Q_BY_UID[uid]["options"])))
        if st.session_state.get("shuffle_a", True):
            random.shuffle(order)
        perms[uid] = order

    st.session_state.deck = deck
    st.session_state.perms = perms
    st.session_state.answers = {}  # uid -> {"choice": position, "correct": bool}
    st.session_state.pos = 0
    st.session_state.epoch = st.session_state.get("epoch", 0) + 1
    st.session_state.audio_data = None
    st.session_state.audio_req = "question" if st.session_state.get("auto_q", True) else None
    st.session_state.exam_active = exam
    st.session_state.exam_half = (len(deck) + 1) // 2
    st.session_state.section_start = {1: time.time()}


def go_to(new_pos: int):
    deck_len = len(st.session_state.deck)
    st.session_state.pos = max(0, min(deck_len, new_pos))
    if st.session_state.get("exam_active") and st.session_state.pos >= st.session_state.exam_half:
        st.session_state.section_start.setdefault(2, time.time())
    st.session_state.audio_data = None
    on_question = st.session_state.pos < deck_len
    st.session_state.audio_req = "question" if (on_question and st.session_state.get("auto_q", True)) else None


def request_audio(kind: str):
    st.session_state.audio_req = kind


def retry_missed():
    answers = st.session_state.answers
    missed = [uid for uid in st.session_state.deck if not answers.get(uid, {}).get("correct")]
    build_deck(pool_uids=missed, force_study=True)


def accuracy_pct() -> int:
    answers = st.session_state.answers
    return round(100 * sum(a["correct"] for a in answers.values()) / len(answers)) if answers else 0


# ──────────────────────────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    try:
        st.image(
            "https://raw.githubusercontent.com/markreciopro/shrm-study-app/main/assets/logo.png",
            use_container_width=True,
            caption="MAREC Insights • Workforce Intelligence",
        )
    except Exception:
        st.markdown("## 🏨 MAREC Insights")

    st.markdown("### 🏆 Exam Masterclass Navigator")
    st.caption("Specialized for Luxury Resorts, Casinos & SHRM-CP Success")
    st.markdown("---")
    st.write("**Candidate:** Mark Anthony Recio, MBA")
    st.write("**Target Credential:** SHRM-CP / CRME")
    st.write("**Core Focus:** BASK Competencies, OSHA, DEI, Labor, Total Rewards")
    st.markdown("---")

    if questions:
        st.metric("Master Question Bank", f"{len(questions)} Questions", "100% Loaded 🌟")
    else:
        st.error("0 Questions Loaded")

    st.markdown("### 🎛️ Study Session")
    st.radio("Mode", [MODE_STUDY, MODE_EXAM], key="mode")
    if st.session_state.get("mode") == MODE_EXAM:
        st.caption(
            f"Full bank, mixed knowledge + situational items, two 110-minute sections, "
            f"answers revealed only at the end. Click **Start New Session** to begin."
        )
    st.selectbox(
        "Question set",
        list(TYPE_FILTERS),
        key="type_filter",
        disabled=st.session_state.get("mode") == MODE_EXAM,
    )
    st.checkbox("🔀 Shuffle question order", value=True, key="shuffle_q")
    st.checkbox("🔀 Shuffle answer choices", value=True, key="shuffle_a")
    if st.button("🔄 Start New Session", use_container_width=True, disabled=not questions):
        build_deck()
        st.rerun()

    st.markdown("### 🔊 Audio Coach")
    st.checkbox("Auto-read each new question", value=True, key="auto_q")
    st.checkbox("Auto-read explanation after answering", value=True, key="auto_e")
    st.checkbox("Slower speaking pace", value=False, key="tts_slow")
    st.selectbox(
        "Voice accent",
        options=["com", "co.uk", "com.au", "ca", "co.in"],
        format_func=lambda t: {
            "com": "US English",
            "co.uk": "British English",
            "com.au": "Australian English",
            "ca": "Canadian English",
            "co.in": "Indian English",
        }[t],
        key="tts_tld",
    )
    st.markdown("---")
    st.write("**System Status:** Operational 🚀")


# ──────────────────────────────────────────────────────────────────────────────
# Header
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    f"""
    <div class="hero-header">
        <h1>🏨 MAREC Insights | SHRM-CP Hospitality Masterclass</h1>
        <p>Mastering {len(questions) or 134} SHRM-BASK Scenarios, Exam Terminology,
        Real-World Examples &amp; Memory Anchors — now shuffled and read aloud.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

if fatal_error:
    st.error(f"⚠️ {fatal_error}")
    st.stop()
for w in load_warnings:
    st.warning(f"⚠️ {w}")
if not questions:
    st.warning("⚠️ No valid questions loaded. Please verify `questions.json` in your repository.")
    st.stop()

if "deck" not in st.session_state:
    st.session_state.score = 0
    build_deck()
st.session_state.score = sum(XP_PER_CORRECT for a in st.session_state.answers.values() if a["correct"])

deck = st.session_state.deck
total = len(deck)
pos = st.session_state.pos
exam_active = st.session_state.get("exam_active", False)
half = st.session_state.get("exam_half", total)


def _fmt(sec: float) -> str:
    sec = max(0, int(sec))
    return f"{sec // 3600}:{(sec % 3600) // 60:02d}:{sec % 60:02d}"


def _section_left(section: int) -> float:
    start = st.session_state.section_start.get(section, time.time())
    return EXAM_SECTION_SECONDS - (time.time() - start)


@st.fragment(run_every=1)
def exam_timer():
    """Live countdown. Auto-advances Section 1 -> 2 and auto-finishes at the end of Section 2."""
    p = st.session_state.pos
    n = len(st.session_state.deck)
    if p >= n:
        return
    section = 1 if p < half else 2
    left = _section_left(section)
    if left <= 0:
        go_to(half if section == 1 else n)
        st.rerun(scope="app")
    st.metric(f"⏱️ Section {section} of 2 — time left", _fmt(left))
    st.progress(max(0.0, min(1.0, left / EXAM_SECTION_SECONDS)))


if exam_active and pos < total:
    with st.sidebar:
        exam_timer()


# ──────────────────────────────────────────────────────────────────────────────
# Results screen
# ──────────────────────────────────────────────────────────────────────────────
if pos >= total:
    answers = st.session_state.answers
    correct_n = sum(a["correct"] for a in answers.values())
    st.progress(1.0, text="Session complete")

    with st.container(border=True, key="qcard"):
        st.subheader("🏁 Session Results")
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Total XP", f"{st.session_state.score} XP")
        c2.metric("Correct", f"{correct_n} / {total}")
        c3.metric("Accuracy (answered)", f"{accuracy_pct()}%")
        c4.metric("Unanswered", total - len(answers))

        # Per-competency breakdown
        def breakdown(field: str, label: str):
            stats = {}
            for uid in deck:
                key = Q_BY_UID[uid][field]
                row = stats.setdefault(key, {label: key, "Answered": 0, "Correct": 0})
                if uid in answers:
                    row["Answered"] += 1
                    row["Correct"] += int(answers[uid]["correct"])
            table = []
            for row in stats.values():
                row["Accuracy"] = f"{round(100 * row['Correct'] / row['Answered'])}%" if row["Answered"] else "—"
                table.append(row)
            table.sort(key=lambda r: (r["Answered"] == 0, r["Correct"] / r["Answered"] if r["Answered"] else 0))
            return table

        if st.session_state.get("exam_active"):
            st.session_state.exam_active = False  # exam over: unlock feedback for review
            st.info(
                "Exam simulation finished. Raw percentage only - SHRM reports a scaled score, "
                "so treat anything consistently below ~70% as a signal to keep studying."
            )

        t1, t2 = st.tabs(["🎯 By Topic", "🧱 By Category"])
        with t1:
            st.markdown("#### 📊 Topic Breakdown (weakest first)")
            st.dataframe(breakdown("topic", "Topic"), use_container_width=True, hide_index=True)
        with t2:
            st.markdown("#### 🧱 Behavioral Competency vs HR Knowledge vs Item Type")
            st.dataframe(breakdown("category", "Category"), use_container_width=True, hide_index=True)
            st.dataframe(breakdown("type", "Item type"), use_container_width=True, hide_index=True)

        with st.expander(f"📝 Review missed / unanswered items ({total - correct_n})"):
            for n, u in enumerate(deck, 1):
                if answers.get(u, {}).get("correct"):
                    continue
                qq = Q_BY_UID[u]
                pp = st.session_state.perms[u]
                st.markdown(f"**{n}. {qq['scenario']}**")
                if u in answers:
                    st.write(f"Your answer: {LETTERS[answers[u]['choice']]}) {qq['options'][pp[answers[u]['choice']]]}")
                else:
                    st.write("Your answer: *(unanswered)*")
                st.write(f"✅ Best answer: {LETTERS[pp.index(qq['correct'])]}) {qq['options'][qq['correct']]}")
                st.caption(qq["explanation"])
                st.markdown("---")

        missed_n = total - correct_n
        b1, b2, b3 = st.columns(3)
        b1.button("🔀 Reshuffle & Restart", on_click=build_deck, type="primary", use_container_width=True)
        b2.button(
            f"🔁 Retry Missed / Unanswered ({missed_n})",
            on_click=retry_missed,
            disabled=missed_n == 0,
            use_container_width=True,
        )
        b3.button("⬅️ Review Last Question", on_click=go_to, args=(total - 1,), use_container_width=True)
        if missed_n == 0:
            st.balloons()
    st.stop()


# ──────────────────────────────────────────────────────────────────────────────
# Question screen
# ──────────────────────────────────────────────────────────────────────────────
uid = deck[pos]
q = Q_BY_UID[uid]
perm = st.session_state.perms[uid]  # perm[display_position] = original option index
correct_pos = perm.index(q["correct"])
record = st.session_state.answers.get(uid)
answered = record is not None

st.progress(
    len(st.session_state.answers) / total,
    text=f"Question {pos + 1} of {total}  •  {len(st.session_state.answers)} answered",
)

with st.container(border=True, key="qcard"):
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.subheader(f"📍 {q['chapter']}")
        st.markdown(f"**Item Type:** `{q['type']}` | 🎯 **SHRM Competency:** `{q['competency']}`")
    with col_b:
        if exam_active:
            st.metric("Answered", f"{len(st.session_state.answers)} / {total}")
        else:
            st.metric("Total XP Score", f"{st.session_state.score} XP")

    st.markdown("### 🏨 Exam Scenario Challenge:")
    st.info(q["scenario"])

    # Audio controls
    a1, a2, _ = st.columns([2, 2, 3])
    a1.button("🔊 Read Question & Choices", on_click=request_audio, args=("question",), use_container_width=True)
    a2.button(
        "🔊 Read Explanation",
        on_click=request_audio,
        args=("explanation",),
        disabled=not answered or exam_active,
        use_container_width=True,
    )
    audio_slot = st.container()

    # Answer choices
    choice = st.radio(
        "Select your best operational or strategic HR recommendation:",
        options=list(range(len(perm))),
        format_func=lambda i: f"{LETTERS[i]}) {q['options'][perm[i]]}",
        index=record["choice"] if answered else None,
        disabled=answered,
        key=f"radio_{st.session_state.epoch}_{uid}",
    )

    if not answered:
        if st.button("Lock Answer 🔒" if exam_active else "Submit Answer 🎯", type="primary", disabled=choice is None):
            is_correct = choice == correct_pos
            st.session_state.answers[uid] = {"choice": choice, "correct": is_correct}
            st.session_state.celebrate = is_correct and not exam_active
            if st.session_state.get("auto_e", True) and not exam_active:
                st.session_state.audio_req = "explanation"
            st.rerun()
    elif exam_active:
        st.info("🔒 Answer locked. Feedback is hidden until the exam ends.")
    else:
        if record["correct"]:
            st.success(f"✅ **Correct! Excellent strategic decision.** (+{XP_PER_CORRECT} XP)")
        else:
            st.error(
                f"❌ **Incorrect.** The correct strategic choice was "
                f"**{LETTERS[correct_pos]}) {q['options'][q['correct']]}**"
            )
        if st.session_state.pop("celebrate", False):
            st.balloons()

        st.markdown("---")
        st.markdown("### 💡 Strategic Rationale & SHRM-CP Terminology")
        st.write(q["explanation"])
        st.markdown("### 🧠 Memory Anchor & Practical Example")
        st.success(q["memory_anchor"])

    # Audio rendering (generated once per request; autoplays only when freshly requested)
    request = st.session_state.pop("audio_req", None)
    if request == "explanation" and (not answered or exam_active):
        request = None
    if request:
        text = (
            explanation_speech(q, perm, record["correct"])
            if request == "explanation"
            else question_speech(q, perm, pos + 1, total)
        )
        try:
            with audio_slot, st.spinner("Preparing audio…"):
                st.session_state.audio_data = synthesize(
                    text, st.session_state.get("tts_slow", False), st.session_state.get("tts_tld", "com")
                )
            st.session_state.audio_fresh = True
        except Exception:
            st.session_state.audio_data = None
            audio_slot.warning(
                "Audio is unavailable right now. gTTS needs an internet connection and "
                "`gTTS` listed in `requirements.txt`."
            )
    if st.session_state.get("audio_data"):
        fresh = st.session_state.pop("audio_fresh", False)
        audio_slot.audio(st.session_state.audio_data, format="audio/mp3", autoplay=fresh)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if pos > 0 and not (exam_active and pos == half):
        st.button("⬅️ Previous Question", on_click=go_to, args=(pos - 1,))
with col3:
    last = pos == total - 1
    st.button("🏁 Finish & See Results" if last else "Next Question ➡️", on_click=go_to, args=(pos + 1,), type="primary")
