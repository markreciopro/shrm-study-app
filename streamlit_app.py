import streamlit as st
import json

# Page Configuration
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP Hospitality Odyssey",
    page_icon="🦜",
    layout="wide"
)

# Sidebar Branding & Navigation
with st.sidebar:
    st.image(
        "https://marec.site/assets/img/logo.png",
        use_column_width=True,
        caption="MAREC Insights • Workforce Intelligence"
    )
    st.title("🏆 Exam Prep Navigator")
    st.caption("Specialized for Luxury Resorts, Casinos & Hospitality Operations")
    st.markdown("---")
    st.write("**Consultant Rank:** Senior HR Strategist")
    st.write("**XP Accumulated:** 150 XP")

# Robust Question Bank Loader
@st.cache_data
def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                return data
    except Exception as e:
        st.error(f"⚠️ Could not parse questions.json: {e}")
    return []

questions = load_questions()

# Sidebar Metric
st.sidebar.metric(label="Total Loaded Items", value=f"{len(questions)} Questions")
st.sidebar.markdown("---")
st.sidebar.write("**Team Morale:** 100%")

# Header
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); padding: 25px; border-radius: 10px; color: white;">
        <h1 style="margin:0; font-size: 28px;">MAREC Insights | SHRM-CP HR Odyssey</h1>
        <p style="margin:5px 0 0 0; font-size: 16px; opacity: 0.9;">Hospitality Workforce Intelligence & Behavioral Competency Simulator</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

if not questions:
    st.error("⚠️ `questions.json` is missing or invalid. Please check your JSON syntax in GitHub.")
else:
    if 'q_index' not in st.session_state:
        st.session_state.q_index = 0
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Prevent out of index error
    if st.session_state.q_index >= len(questions):
        st.session_state.q_index = 0

    current_q = questions[st.session_state.q_index]

    st.subheader(f"Question {st.session_state.q_index + 1} of {len(questions)}: {current_q.get('chapter', 'Hospitality Operations')}")
    st.write(f"**Item Type:** {current_q.get('type', 'SJI')}")
    st.info(f"🎯 **Core Competency:** {current_q.get('competency', 'Business Acumen & Leadership')}")

    st.markdown("### 🏨 Hospitality Scenario Challenge:")
    st.write(current_q['scenario'])

    form_key = f"form_{st.session_state.q_index}"
    with st.form(key=form_key):
        selected_option = st.radio(
            "Select your best operational or strategic HR recommendation:",
            current_q['options'],
            key=f"radio_{st.session_state.q_index}"
        )
        
        submitted = st.form_submit_button("Submit Answer")

        if submitted:
            st.session_state.submitted = True
            selected_idx = ord(selected_option[0]) - ord('A')
            
            if selected_idx == current_q['correct']:
                st.success("✅ **Correct! Excellent strategic decision.**")
            else:
                correct_letter = chr(ord('A') + current_q['correct'])
                st.error(f"❌ **Incorrect.** The correct strategic choice was **{correct_letter}**.")

            st.markdown("---")
            st.markdown("### 💡 Strategic Rationale & Explanation")
            st.write(current_q['explanation'])

            st.markdown("### 🧠 Memory Anchor (Keep It Simple!)")
            st.success(current_q.get('memory_anchor', 'Think of this like balancing resort shifts during peak guest arrivals.'))

    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.q_index > 0:
            if st.button("⬅️ Previous Question"):
                st.session_state.q_index -= 1
                st.session_state.submitted = False
                st.rerun()
    with col2:
        if st.session_state.q_index < len(questions) - 1:
            if st.button("Next Question ➡️"):
                st.session_state.q_index += 1
                st.session_state.submitted = False
                st.rerun()
