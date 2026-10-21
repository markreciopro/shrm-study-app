import streamlit as st
import json
from gtts import gTTS
from io import BytesIO

# Page Configuration
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP & CRME Hospitality Masterclass",
    page_icon="🏨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom High-Contrast CSS for Pristine Readability & Luxury Resort Theme
st.markdown("""
    <style>
    /* High-Contrast Color Palette & Luxury Resort Glassmorphism */
    @keyframes fadeIn {
        0% { opacity: 0; transform: translateY(10px); }
        100% { opacity: 1; transform: translateY(0); }
    }

    .stApp {
        background: linear-gradient(135deg, #0a192f 0%, #172a45 50%, #1f4068 100%);
        color: #ffffff !important;
        font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* Main Content Card Container with High Contrast */
    .masterclass-card {
        animation: fadeIn 0.5s ease-out;
        background: rgba(15, 23, 42, 0.85);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(100, 255, 218, 0.3);
        border-radius: 16px;
        padding: 30px;
        margin-bottom: 24px;
        box-shadow: 0 12px 40px 0 rgba(0, 0, 0, 0.5);
    }

    .hero-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 30px;
        border-radius: 16px;
        color: #ffffff;
        border: 1px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 8px 32px rgba(0,0,0,0.4);
    }

    /* High Visibility Typography & Labels */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown {
        color: #ffffff !important;
    }

    .stRadio label p {
        color: #e2e8f0 !important;
        font-size: 16px !important;
        font-weight: 500 !important;
    }

    /* Stunning Custom Buttons */
    .stButton>button {
        border-radius: 10px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px !important;
        background: linear-gradient(90deg, #00b4d8 0%, #0077b6 100%) !important;
        color: #ffffff !important;
        border: none !important;
        padding: 10px 24px !important;
        box-shadow: 0 4px 12px rgba(0, 180, 216, 0.4) !important;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(0, 180, 216, 0.7) !important;
        background: linear-gradient(90deg, #90e0ef 0%, #00b4d8 100%) !important;
        color: #0a192f !important;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #070d1b !important;
        border-right: 1px solid rgba(255, 255, 255, 0.1);
    }

    /* Info / Success / Error box overrides for high contrast */
    .stAlert {
        background-color: rgba(30, 41, 59, 0.9) !important;
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
    }
    </style>
""", unsafe_allow_html=True)

# Safe Loader for questions.json
@st.cache_data
def load_questions():
    try:
        with open("questions.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ `questions.json` not found in repository.")
        return []
    except json.JSONDecodeError as e:
        st.error(f"⚠️ Syntax error in `questions.json` at line {e.lineno}: {e.msg}")
        return []

questions = load_questions()

# Sidebar Navigation & User Profile
with st.sidebar:
    st.image(
        "https://raw.githubusercontent.com/markreciopro/shrm-study-app/main/assets/logo.png",
        use_column_width=True,
        caption="MAREC Insights • Workforce Intelligence"
    )
    st.markdown("### 🏆 Exam Masterclass Navigator")
    st.caption("Specialized for Luxury Resorts, Casinos & SHRM-CP Success")
    st.markdown("---")
    
    st.write("**Candidate:** Mark Anthony Recio, MBA")
    st.write("**Target Credential:** SHRM-CP / CRME")
    st.write("**Core Focus:** BASK Competencies, OSHA, DEI, Labor, Total Rewards")
    st.markdown("---")
    
    if questions:
        st.metric(label="Master Question Bank", value=f"{len(questions)} Questions", delta="100% Loaded 🌟")
    else:
        st.error("0 Questions Loaded")
    
    st.markdown("---")
    st.write("**System Status:** Operational 🚀")

# Hero Banner Header
st.markdown("""
    <div class="hero-header">
        <h1 style="margin:0; font-size: 28px; font-weight: 700; color: #ffffff;">🏨 MAREC Insights | SHRM-CP Hospitality Masterclass</h1>
        <p style="margin:8px 0 0 0; font-size: 15px; color: #cbd5e1;">
            Mastering 150 Rigorous SHRM-BASK Scenarios, Exam Terminology, Real-World Examples & Memory Anchors
        </p>
    </div>
""", unsafe_allow_html=True)

st.write("")

if not questions:
    st.warning("⚠️ No questions loaded. Please verify `questions.json` in your repository.")
else:
    if 'q_index' not in st.session_state:
        st.session_state.q_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0

    current_q = questions[st.session_state.q_index]

    # Progress Indicator
    progress_val = (st.session_state.q_index + 1) / len(questions)
    st.progress(progress_val, text=f"Exam Progress: Question {st.session_state.q_index + 1} of {len(questions)}")

    # Main Card Container
    st.markdown('<div class="masterclass-card">', unsafe_allow_html=True)
    
    col_a, col_b = st.columns([3, 1])
    with col_a:
        st.subheader(f"📍 {current_q.get('chapter', 'Hospitality Operations')}")
        st.markdown(f"**Item Type:** `{current_q.get('type', 'SJI')}` | 🎯 **SHRM Competency:** `{current_q.get('competency', 'Business Acumen')}`")
    with col_b:
        st.metric(label="Total XP Score", value=f"{st.session_state.score} XP")

    st.markdown("### 🏨 Exam Scenario Challenge:")
    st.info(current_q['scenario'])

    # Audio TTS Reader
    if st.button("🔊 Read Scenario Aloud"):
        try:
            tts = gTTS(text=current_q['scenario'], lang='en', slow=False)
            audio_fp = BytesIO()
            tts.write_to_fp(audio_fp)
            audio_fp.seek(0)
            st.audio(audio_fp, format='audio/mp3', autoplay=True)
        except Exception as e:
            st.warning("Audio synthesis note: Ensure `gTTS` is installed in `requirements.txt`.")

    # Interactive Options Form
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
            st.markdown("### 💡 Strategic Rationale & SHRM-CP Terminology")
            st.write(current_q['explanation'])

            st.markdown("### 🧠 Memory Anchor & Practical Example")
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
