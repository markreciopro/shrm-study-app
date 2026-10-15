import streamlit as st
import json
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP Hospitality HR Odyssey",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- LOGO URL ---
LOGO_URL = "https://raw.githubusercontent.com/markreciopro/marec_insights/main/Gemini_Generated_Image_noss7snoss7snoss.jpg"

# --- LOAD QUESTION BANK ---
@st.cache_data
def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception as e:
        st.error(f"Error loading questions.json: {e}")
        return []

questions = load_questions()

# --- SESSION STATE INITIALIZATION ---
if "current_index" not in st.session_state:
    st.session_state.current_index = 0
if "xp" not in st.session_state:
    st.session_state.xp = 0
if "user_answers" not in st.session_state:
    st.session_state.user_answers = {}
if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Track shuffled option mappings per question index to prevent jitter on reruns
if "shuffled_options" not in st.session_state:
    st.session_state.shuffled_options = {}

total_questions = len(questions)

# --- SIDEBAR NAVIGATION & GAMIFICATION ---
with st.sidebar:
    st.image(LOGO_URL, use_container_width=True)
    st.markdown("### 🏆 Exam Prep Navigator")
    
    # Calculate Rank based on XP
    rank = "Junior Hospitality HR Analyst"
    if st.session_state.xp >= 500:
        rank = "Resort HR Generalist"
    if st.session_state.xp >= 1500:
        rank = "Senior Hospitality HR Business Partner"
    if st.session_state.xp >= 3500:
        rank = "Director of Hospitality Human Capital"
    if st.session_state.xp >= 6000:
        rank = "VP / Chief Human Resources Officer (CHRO)"

    st.write(f"**Consultant Rank:** {rank}")
    st.write(f"**XP Accumulated:** `:green[{st.session_state.xp} XP]`")
    st.write(f"**Total Loaded Items:** `{total_questions} Questions`")
    st.progress(min((st.session_state.current_index + 1) / max(total_questions, 1), 1.0))
    st.caption(f"Progress: Question {st.session_state.current_index + 1} of {total_questions}")
    
    st.markdown("---")
    if st.button("🔄 Reset Exam Progress"):
        st.session_state.current_index = 0
        st.session_state.xp = 0
        st.session_state.user_answers = {}
        st.session_state.submitted = False
        st.session_state.shuffled_options = {}
        st.rerun()

# --- MAIN HEADER BANNER WITH LOGO ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image(LOGO_URL, width=130)
with col_title:
    st.markdown("""
        <div style="background-color:#1E293B; padding:15px; border-radius:10px; color:white; border-left: 6px solid #3B82F6;">
            <h1 style="margin:0; color:#F8FAFC; font-size: 26px;">MAREC Insights | SHRM-CP HR Odyssey</h1>
            <p style="margin:5px 0 0 0; color:#94A3B8;">150-Question Hospitality Workforce Intelligence & Behavioral Simulator</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if not questions:
    st.warning("No questions found. Please check `questions.json` formatting in your GitHub repository.")
    st.stop()

# Ensure index stays within bounds
if st.session_state.current_index >= total_questions:
    st.session_state.current_index = total_questions - 1

q = questions[st.session_state.current_index]

# Header Info
st.subheader(f"Question {st.session_state.current_index + 1} of {total_questions}: {q.get('chapter', 'Hospitality HR Operations')}")
st.caption(f"**Item Type:** `{q.get('type', 'Knowledge Item')}`")
st.info(f"🎯 **Core SHRM Competency:** {q.get('competency', 'HR Expertise')}")

# Scenario Box
st.markdown(f"""
    <div style="background-color:#0F172A; padding:20px; border-radius:8px; border:1px solid #334155; margin-bottom:15px;">
        <h4 style="color:#60A5FA; margin-top:0;">Hospitality Scenario Challenge:</h4>
        <p style="color:#E2E8F0; font-size:16px; line-height:1.6;">{q.get('scenario', '')}</p>
    </div>
""", unsafe_allow_html=True)

# Key Terms Accordion
key_terms = q.get("key_terms", {})
if key_terms:
    with st.expander("📚 View SHRM Key Terms & Legal Definitions for this Scenario"):
        for term, definition in key_terms.items():
            st.markdown(f"**• {term}:** {definition}")

# Randomize options per question index deterministically for rigorous testing
q_idx = st.session_state.current_index
if q_idx not in st.session_state.shuffled_options:
    original_options = q.get("options", [])
    correct_original_idx = q.get("correct", 0)
    correct_text = original_options[correct_original_idx] if 0 <= correct_original_idx < len(original_options) else original_options[0]
    
    # Shuffle options
    shuffled = original_options.copy()
    random.shuffle(shuffled)
    new_correct_idx = shuffled.index(correct_text)
    
    st.session_state.shuffled_options[q_idx] = {
        "options": shuffled,
        "correct": new_correct_idx
    }

current_shuffled_data = st.session_state.shuffled_options[q_idx]
options = current_shuffled_data["options"]
correct_index = current_shuffled_data["correct"]

# Radio Selection for Options
selected_option = st.radio(
    "Select the best strategic intervention:",
    options,
    key=f"q_{q_idx}"
)

# Submit Answer Action
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("Submit Answer", type="primary"):
        st.session_state.submitted = True
        selected_idx = options.index(selected_option) if selected_option in options else -1
        
        if selected_idx == correct_index:
            st.session_state.xp += 50
            st.success("🎉 Correct Strategic Response! (+50 XP)")
        else:
            st.error("❌ Sub-optimal Choice. Review rationale below.")

if st.session_state.submitted:
    st.markdown("---")
    st.markdown("### 💡 Strategic Rationale & Hospitality Application")
    
    rat = q.get("strategic_rationale", "")
    ex = q.get("example", "")
    exp_text = q.get("explanation", "")
    
    if rat:
        st.markdown(f"**Strategic Rationale:** {rat}")
    if ex:
        st.markdown(f"**Hospitality Example:** {ex}")
    if not rat and not ex:
        st.write(exp_text)

# Navigation Buttons
st.markdown("---")
nav_col1, nav_col2, nav_col3 = st.columns([1, 4, 1])

with nav_col1:
    if st.button("⬅️ Previous") and st.session_state.current_index > 0:
        st.session_state.current_index -= 1
        st.session_state.submitted = False
        st.rerun()

with nav_col3:
    if st.button("Next ➡️") and st.session_state.current_index < total_questions - 1:
        st.session_state.current_index += 1
        st.session_state.submitted = False
        st.rerun()
