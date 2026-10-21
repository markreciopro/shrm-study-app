import streamlit as st
import json
from gtts import gTTS
from io import BytesIO

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
    st.write("**Target Credential:** SHRM-CP / CRME")

# Load Question Bank
@st.cache_data
def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

questions = load_questions()

# Display Total Loaded Items
st.sidebar.metric(label="Total Question Bank", value=f"{len(questions)} Questions")
st.sidebar.markdown("---")
st.sidebar.write("**System Status:** Operational 🌟")

# Main App Header
st.markdown("""
    <div style="background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%); padding: 25px; border-radius: 10px; color: white;">
        <h1 style="margin:0; font-size: 28px;">MAREC Insights | SHRM-CP HR Odyssey</h1>
        <p style="margin:5px 0 0 0; font-size: 16px; opacity: 0.9;">Hospitality Workforce Intelligence & Behavioral Competency Simulator</p>
    </div>
""", unsafe_allow_html=True)

st.write("")

if not questions:
    st.error("⚠️ `questions.json` not found or empty! Please verify the repository files.")
else:
    if 'q_index' not in st.session_state:
        st.session_state.q_index = 0
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    current_q = questions[st.session_state.q_index]

    progress_val = (st.session_state.q_index + 1) / len(questions)
    st.progress(progress_val, text=f"Exam Progress: Question {st.session_state.q_index + 1} of {len(questions)}")

    st.subheader(f"{current_q.get('chapter', 'Hospitality Operations')}")
    st.write(f"**Item Type:** {current_q.get('type', 'SJI')} | 🎯 **Core Competency:** {current_q.get('competency', 'Business Acumen & Leadership')}")

    # Scenario Box
    st.markdown("### 🏨 Hospitality Scenario Challenge:")
    st.info(current_q['scenario'])

    # Audio Reader Feature (TTS)
    if st.button("🔊 Read Scenario Aloud"):
        try:
            tts = gTTS(text=current_q['scenario'], lang='en', slow=False)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format='audio/mp3', autoplay=True)
        except Exception as e:
            st.warning("Audio synthesis note: Ensure `gTTS` is installed in `requirements.txt`.")

    # Options Form
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
                st.success("✅ **Correct! Excellent strategic decision.** (+10 XP)")
                st.balloons()
            else:
                correct_letter = chr(ord('A') + current_q['correct'])
                st.error(f"❌ **Incorrect.** The correct strategic choice was **{correct_letter}**.")

            st.markdown("---")
            st.markdown("### 💡 Strategic Rationale & Explanation")
            st.write(current_q['explanation'])

            st.markdown("### 🧠 Memory Anchor (Keep It Simple!)")
            st.success(current_q.get('memory_anchor', 'Think of this like balancing resort shifts during peak guest arrivals.'))

    # Navigation Controls
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
