import streamlit as st
import json
import time
from gtts import gTTS
from io import BytesIO

# Page Configuration & Modern Hospitality Visual Styling
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP & CRME Hospitality Odyssey",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Premium Resort Styling, Glassmorphism & Animations
st.markdown("""
    <style>
    /* CSS Animations & Hospitality Theme */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(12px); }
        100% { opacity: 1; transform: translateY(0); }
    }
    
    @keyframes pulseGlow {
        0% { box-shadow: 0 0 10px rgba(30, 60, 114, 0.4); }
        50% { box-shadow: 0 0 25px rgba(42, 82, 152, 0.8); }
        100% { box-shadow: 0 0 10px rgba(30, 60, 114, 0.4); }
    }

    /* Background styling with hospitality aesthetics */
    .stApp {
        background: linear-gradient(135deg, #0f2027 0%, #203a43 50%, #2c5364 100%);
        color: #f4f6f9;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }

    /* Animated Card Containers */
    .animated-card {
        animation: fadeIn 0.6s ease-out;
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 16px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
    }

    .hero-banner {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 28px;
        border-radius: 16px;
        color: #ffffff;
        animation: pulseGlow 4s infinite ease-in-out;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }

    /* Custom Buttons Styling */
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease !important;
        background: linear-gradient(90deg, #2b5876 0%, #4e4376 100%) !important;
        color: white !important;
        border: none !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 5px 15px rgba(0,0,0,0.4) !important;
    }

    /* Sidebar Customization */
    section[data-testid="stSidebar"] {
        background-color: rgba(15, 32, 39, 0.95) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Safe Loader for questions.json with robust error handling
@st.cache_data
def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ `questions.json` file not found in the repository. Please make sure it is committed.")
        return []
    except json.JSONDecodeError as e:
        st.error(f"⚠️ Syntax error in `questions.json` at line {e.lineno}, col {e.colno}: {e.msg}")
        return []

questions = load_questions()

# Sidebar Navigation & User Profile
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/markreciopro/shrm-study-app/main/assets/logo.png",
        use_column_width=True,
        caption="MAREC Insights • Workforce Intelligence"
    )
    st.markdown("### 🏆 Exam Prep Navigator")
    st.caption("Specialized for Luxury Resorts, Casinos & Hospitality Operations")
    st.markdown("---")
    
    st.write("**Candidate Rank:** Senior HR Strategist")
    st.write("**Target Certification:** SHRM-CP / CRME")
    st.write("**Domain Focus:** OSHA, DEI, Labor, Total Rewards")
    st.markdown("---")
    
    if questions:
        st.metric(label="Total Question Bank", value=f"{len(questions)} Questions", delta="100% Loaded 🌟")
    else:
        st.error("0 Questions Loaded")
    
    st.markdown("---")
    st.write("**System Health:** Operational 🚀")

# Hero Banner Header
st.markdown("""
    <div class="hero-banner">
        <h1 style="margin:0; font-size: 30px; font-weight: 700;">🏨 MAREC Insights | SHRM-CP Hospitality Odyssey</h1>
        <p style="margin:8px 0 0 0; font-size: 16px; opacity: 0.95;">
            Mastering 150 Hospitality Workforce Scenarios • OSHA • DEI • Labor Relations • Total Rewards
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

if not questions:
    st.warning("⚠️ No questions loaded. Please verify `questions.json` in your repository.")
else:
    # State Management for Question Carousel
    if 'q_index' not in st.session_state:
        st.session_state.q_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0

    current_q = questions[st.session_state.q_index]

    # Progress Indicator
    progress_val = (st.session_state.q_index + 1) / len(questions)
    st.progress(progress_val, text=f"Exam Progress: Question {st.session_state.q_index + 1} of {len(questions)}")

    # Main Question Container Card
    st.markdown('<div class="animated-card">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.subheader(f"📍 {current_q.get('chapter', 'Hospitality Operations')}")
        st.caption(f"**Item Type:** {current_q.get('type', 'SJI')} | 🎯 **Core Competency:** {current_q.get('competency', 'Business Acumen')}")
    with col_b:
        st.metric(label="Current Score", value=f"{st.session_state.score} XP")

    st.markdown("### 🏨 Operational Scenario Challenge:")
    st.info(current_q['scenario'])

    # Audio TTS Synthesis
    if st.button("🔊 Read Scenario Aloud"):
        try:
            tts = gTTS(text=current_q['scenario'], lang='en', slow=False)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format='audio/mp3', autoplay=True)
        except Exception as e:
            st.warning("Audio synthesis note: Ensure `gTTS` is installed in `requirements.txt`.")

    # Options Interactive Form
    form_key = f"form_{st.session_state.q_index}"
    with st.form(key=form_key):
        selected_option = st.radio(
            "Select your best operational or strategic HR recommendation:",
            current_q['options'],
            key=f"radio_{st.session_state.q_index}"
        )
        
        submitted = st.form_submit_button("Submit Answer 🎯")

        if submitted:
            selected_idx = ord(selected_option[0]) - ord('A')
            
            if selected_idx == current_q['correct']:
                st.session_state.score += 10
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

    st.markdown('</div>', unsafe_allow_html=True)

    # Carousel Navigation Controls
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        if st.session_state.q_index > 0:
            if st.button("⬅️ Previous Question"):
                st.session_state.q_index -= 1
                st.rerun()
    with col3:
        if st.session_state.q_index < len(questions) - 1:
            if st.button("Next Question ➡️"):
                st.session_state.q_index += 1
                st.rerun()
