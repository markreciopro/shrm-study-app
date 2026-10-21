import json
import random
import re
from io import BytesIO
from pathlib import Path

import streamlit as st
from gTTS import gTTS

# ──────────────────────────────────────────────────────────────────────────────
# Page configuration
# ──────────────────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="SHRM-CP Hospitality Masterclass | Created by Mark Anthony Recio",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded",
)

XP_PER_CORRECT = 10
LETTERS = "ABCDEFGH"

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

    /* Question card container */
    .st-key-qcard {
        animation: fadeIn 0.5s ease-out;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(100, 255, 218, 0.3) !important;
        border-radius: 16px;
        padding: 16px 22px;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    }

    .hero-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 24px 28px;
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-bottom: 18px;
    }
    .hero-header h1 { margin: 0; font-size: 26px; font-weight: 700; color: #ffffff; }
    .hero-header p  { margin: 8px 0 0 0; font-size: 14px; color: #cbd5e1; }

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
    .stRadio label p { font-size: 15px; font-weight: 500; }

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
ITEM_PREFIX_RE = re.compile(r"^\s*\[[^\]]*#\d+\]\s*")
OPTION_PREFIX_RE = re.compile(r"^\s*[A-Ha-h][\)\.:]\s*")


def _normalize(raw: dict, idx: int) -> dict:
    options = [OPTION_PREFIX_RE.sub("", str(o)).strip() for o in raw["options"]]
    correct = int(raw["correct"])
    if len(options) < 2 or not 0 <= correct < len(options):
        raise ValueError("options/correct index are inconsistent")
    return {
        "uid": idx,
        "id": raw.get("id", idx + 1),
        "type": raw.get("type", "Knowledge Item"),
        "chapter": raw.get("chapter", "SHRM BASK Domain"),
        "competency": raw.get("competency", "HR Expertise"),
        "scenario": ITEM_PREFIX_RE.sub("", str(raw["scenario"])).strip(),
        "options": options,
        "correct": correct,
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
        return [], [], "`questions.json` not found in repository."
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
    "All SHRM-CP Items (134)": lambda q: True,
    "Knowledge Items (80)": lambda q: "situational" not in q["type"].lower(),
    "Situational Judgment Items (54)": lambda q: "situational" in q["type"].lower(),
}


# ──────────────────────────────────────────────────────────────────────────────
# Speech Synthesis
# ──────────────────────────────────────────────────────────────────────────────
EMOJI_RE = re.compile("[\U0001F300-\U0001FAFF\u2600-\u27BF\u2B50\uFE0F\u200d]+")


def clean_for_speech(text: str) -> str:
    text = EMOJI_RE.sub("", text)
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
# Session Deck State
# ──────────────────────────────────────────────────────────────────────────────
def build_deck(pool_uids=None):
    if pool_uids is None:
        keep = TYPE_FILTERS[st.session_state.get("type_filter", "All SHRM-CP Items (134)")]
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
    st.session_state.answers = {}
    st.session_state.pos = 0
    st.session_state.epoch = st.session_state.get("epoch", 0) + 1
    st.session_state.audio_data = None
    st.session_state.audio_req = "question" if st.session_state.get("auto_q", True) else None


def go_to(new_pos: int):
    deck_len = len(st.session_state.deck)
    st.session_state.pos = max(0, min(deck_len, new_pos))
    st.session_state.audio_data = None
    on_question = st.session_state.pos < deck_len
    st.session_state.audio_req = "question" if (on_question and st.session_state.get("auto_q", True)) else None


def request_audio(kind: str):
    st.session_state.audio_req = kind


def retry_missed():
    answers = st.session_state.answers
    missed = [uid for uid in st.session_state.deck if not answers.get(uid, {}).get("correct")]
    build_deck(pool_uids=missed)


def accuracy_pct() -> int:
    answers = st.session_state.answers
    return round(100 * sum(a["correct"] for a in answers.values()) / len(answers)) if answers else 0


# ──────────────────────────────────────────────────────────────────────────────
# Sidebar
# ──────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏨 SHRM-CP Masterclass")
    st.caption("Created by Mark Anthony Recio")
    st.markdown("---")
    st.write("**Target Exam:** SHRM-CP Certification")
    st.write("**Total Items:** 134 Questions (80 KI / 54 SJI)")
    st.write("**Passing Scaled Score:** 200 (Scale 120–300)")
    st.markdown("---")

    if questions:
        st.metric("Question Bank Status", f"{len(questions)} Loaded", "100% Unique ✅")
    else:
        st.error("0 Questions Loaded")

    st.markdown("### 🎛️ Session Setup")
    st.selectbox("Question Filter", list(TYPE_FILTERS), key="type_filter")
    st.checkbox("🔀 Shuffle question order", value=True, key="shuffle_q")
    st.checkbox("🔀 Shuffle answer choices", value=True, key="shuffle_a")
    if st.button("🔄 Reset / Start Session", use_container_width=True, disabled=not questions):
        build_deck()
        st.rerun()

    st.markdown("### 🔊 Audio Coach")
    st.checkbox("Auto-read question", value=True, key="auto_q")
    st.checkbox("Auto-read explanation", value=True, key="auto_e")
    st.selectbox("Voice Accent", options=["com", "co.uk", "ca"], key="tts_tld")
    st.markdown("---")
    st.caption("Created by Mark Anthony Recio | SHRM BASK Framework")


# ──────────────────────────────────────────────────────────────────────────────
# Main Header
# ──────────────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="hero-header">
        <h1>🏨 SHRM-CP Hospitality Exam Prep Masterclass</h1>
        <p>134 Unique SHRM BASK Scenarios &amp; Knowledge Items — Created by Mark Anthony Recio</p>
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
    st.warning("⚠️ No valid questions loaded. Please check `questions.json`.")
    st.stop()

if "deck" not in st.session_state:
    st.session_state.score = 0
    build_deck()
st.session_state.score = sum(XP_PER_CORRECT for a in st.session_state.answers.values() if a["correct"])

deck = st.session_state.deck
total = len(deck)
pos = st.session_state.pos


# ──────────────────────────────────────────────────────────────────────────────
# Completion Results View
# ──────────────────────────────────────────────────────────────────────────────
if pos >= total:
    answers = st.session_state.answers
    correct_n = sum(a["correct"] for a in answers.values())
    st.progress(1.0, text="Exam Session Completed")

    with st.container(border=True, key="qcard"):
        st.subheader("🏁 Performance Summary")
        scaled_score = 120 + round((correct_n / max(total, 1)) * 180)
        passed = scaled_score >= 200

        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Scaled Score", f"{scaled_score} / 300", "PASS ✅" if passed else "DID NOT PASS ❌")
        c2.metric("Raw Score", f"{correct_n} / {total}")
        c3.metric("Accuracy", f"{accuracy_pct()}%")
        c4.metric("XP Earned", f"{st.session_state.score} XP")

        # Competency summary
        stats = {}
        for uid in deck:
            comp = Q_BY_UID[uid]["competency"]
            row = stats.setdefault(comp, {"Competency": comp, "Answered": 0, "Correct": 0})
            if uid in answers:
                row["Answered"] += 1
                row["Correct"] += int(answers[uid]["correct"])
        table = []
        for row in stats.values():
            row["Accuracy"] = f"{round(100 * row['Correct'] / row['Answered'])}%" if row["Answered"] else "—"
            table.append(row)
        st.markdown("#### 📊 SHRM BASK Competency Diagnostics")
        st.dataframe(table, use_container_width=True, hide_index=True)

        missed_n = total - correct_n
        b1, b2, b3 = st.columns(3)
        b1.button("🔀 Start New Random Deck", on_click=build_deck, type="primary", use_container_width=True)
        b2.button(
            f"🔁 Retry Missed Questions ({missed_n})",
            on_click=retry_missed,
            disabled=missed_n == 0,
            use_container_width=True,
        )
        b3.button("⬅️ Review Last Item", on_click=go_to, args=(total - 1,), use_container_width=True)
    st.stop()


# ──────────────────────────────────────────────────────────────────────────────
# Question Challenge View
# ──────────────────────────────────────────────────────────────────────────────
uid = deck[pos]
q = Q_BY_UID[uid]
perm = st.session_state.perms[uid]
correct_pos = perm.index(q["correct"])
record = st.session_state.answers.get(uid)
answered = record is not None

st.progress(
    len(st.session_state.answers) / total,
    text=f"Item {pos + 1} of {total}  •  {len(st.session_state.answers)} Answered",
)

with st.container(border=True, key="qcard"):
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.subheader(f"📍 {q['chapter']}")
        st.markdown(f"**Item Type:** `{q['type']}` | 🎯 **SHRM Competency:** `{q['competency']}`")
    with col_b:
        st.metric("Total XP", f"{st.session_state.score} XP")

    st.markdown("### 🏨 Exam Scenario:")
    st.info(q["scenario"])

    a1, a2, _ = st.columns([2, 2, 3])
    a1.button("🔊 Read Question", on_click=request_audio, args=("question",), use_container_width=True)
    a2.button(
        "🔊 Read Rationale",
        on_click=request_audio,
        args=("explanation",),
        disabled=not answered,
        use_container_width=True,
    )
    audio_slot = st.container()

    choice = st.radio(
        "Select your best operational or strategic HR recommendation:",
        options=list(range(len(perm))),
        format_func=lambda i: f"{LETTERS[i]}) {q['options'][perm[i]]}",
        index=record["choice"] if answered else None,
        disabled=answered,
        key=f"radio_{st.session_state.epoch}_{uid}",
    )

    if not answered:
        if st.button("Submit Answer 🎯", type="primary", disabled=choice is None):
            is_correct = choice == correct_pos
            st.session_state.answers[uid] = {"choice": choice, "correct": is_correct}
            if st.session_state.get("auto_e", True):
                st.session_state.audio_req = "explanation"
            st.rerun()
    else:
        if record["correct"]:
            st.success(f"✅ **Correct! Excellent strategic decision.** (+{XP_PER_CORRECT} XP)")
        else:
            st.error(
                f"❌ **Incorrect.** Correct answer: "
                f"**{LETTERS[correct_pos]}) {q['options'][q['correct']]}**"
            )

        st.markdown("---")
        st.markdown("### 💡 Strategic Rationale & SHRM BASK Alignment")
        st.write(q["explanation"])
        st.markdown("### 🧠 Memory Anchor")
        st.success(q["memory_anchor"])

    request = st.session_state.pop("audio_req", None)
    if request == "explanation" and not answered:
        request = None
    if request:
        text = (
            explanation_speech(q, perm, record["correct"])
            if request == "explanation"
            else question_speech(q, perm, pos + 1, total)
        )
        try:
            with audio_slot, st.spinner("Synthesizing audio…"):
                st.session_state.audio_data = synthesize(
                    text, False, st.session_state.get("tts_tld", "com")
                )
            st.session_state.audio_fresh = True
        except Exception:
            st.session_state.audio_data = None

    if st.session_state.get("audio_data"):
        fresh = st.session_state.pop("audio_fresh", False)
        audio_slot.audio(st.session_state.audio_data, format="audio/mp3", autoplay=fresh)

# Navigation
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if pos > 0:
        st.button("⬅️ Previous Item", on_click=go_to, args=(pos - 1,))
with col3:
    last = pos == total - 1
    st.button("🏁 Finish Exam" if last else "Next Item ➡️", on_click=go_to, args=(pos + 1,), type="primary")
