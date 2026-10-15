import streamlit as st
import json
import random

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP HR Odyssey",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded"
)

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

total_questions = len(questions)

# --- SIDEBAR NAVIGATION & GAMIFICATION ---
with st.sidebar:
    st.markdown("### 🏆 Exam Prep Navigator")
    
    # Calculate Rank based on XP
    rank = "Junior HR Analyst"
    if st.session_state.xp >= 500:
        rank = "HR Generalist"
    if st.session_state.xp >= 1200:
        rank = "Senior HR Business Partner"
    if st.session_state.xp >= 2500:
        rank = "Strategic HR Director"
    if st.session_state.xp >= 4000:
        rank = "Chief Human Resources Officer (CHRO)"

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
        st.rerun()

# --- MAIN CONTENT AREA ---
st.markdown("""
    <div style="background-color:#1E293B; padding:20px; border-radius:10px; color:white; margin-bottom:20px; border-left: 6px solid #3B82F6;">
        <h1 style="margin:0; color:#F8FAFC;">MAREC Insights | SHRM-CP HR Odyssey</h1>
        <p style="margin:5px 0 0 0; color:#94A3B8;">Workforce Intelligence & Behavioral Competency Simulator</p>
    </div>
""", unsafe_allow_html=True)

if not questions:
    st.warning("No questions found. Please check `questions.json` formatting in your GitHub repository.")
    st.stop()

# Ensure index stays within bounds
if st.session_state.current_index >= total_questions:
    st.session_state.current_index = total_questions - 1

q = questions[st.session_state.current_index]

# Header Info
st.subheader(f"Question {st.session_state.current_index + 1} of {total_questions}: {q.get('chapter', 'General HR')}")
st.caption(f"**Item Type:** `{q.get('type', 'Knowledge Item')}`")

st.info(f"🎯 **Core Competency:** {q.get('competency', 'HR Expertise')}")

# Scenario Box
st.markdown(f"""
    <div style="background-color:#0F172A; padding:20px; border-radius:8px; border:1px solid #334155; margin-bottom:20px;">
        <h4 style="color:#60A5FA; margin-top:0;">Scenario Challenge:</h4>
        <p style="color:#E2E8F0; font-size:16px; line-height:1.6;">{q.get('scenario', '')}</p>
    </div>
""", unsafe_allow_html=True)

# Radio Selection for Options
options = q.get("options", [])
selected_option = st.radio(
    "Select the best strategic intervention:",
    options,
    key=f"q_{st.session_state.current_index}"
)

# Submit Answer Action
col1, col2, col3 = st.columns([1, 1, 2])

with col1:
    if st.button("Submit Answer", type="primary"):
        st.session_state.submitted = True
        correct_idx = q.get("correct", 0)
        selected_idx = options.index(selected_option) if selected_option in options else -1
        
        if selected_idx == correct_idx:
            st.session_state.xp += 50
            st.success("🎉 Correct Strategic Response! (+50 XP)")
        else:
            st.error("❌ Sub-optimal Choice. Review rationale below.")

if st.session_state.submitted:
    st.markdown("---")
    st.markdown("### 💡 Strategic Rationale & Explanation")
    st.write(q.get("explanation", "No explanation available."))

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
