import streamlit as st
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

# Embedded Question Bank (No external JSON file required!)
@st.cache_data
def load_questions():
    return [
        {
            "type": "Situational Judgment Item (SJI)",
            "chapter": "Hospitality Labor Economics & Overtime Control",
            "scenario": "A 2,000-room Las Vegas casino resort experiences a sudden 30% spike in weekend occupancy due to an unannounced convention booking. Front Desk and Housekeeping shift managers immediately call in off-duty staff on double-time overtime without clearing floor schedules. How should the HR Director intervene to manage labor costs without hurting guest service standards?",
            "options": [
                "A) Require department managers to utilize flexible cross-trained banquet and pool staff on straight-time hours before approving emergency overtime.",
                "B) Freeze all incoming guest check-ins until regular shift workers arrive on Monday.",
                "C) Automatically deny all overtime pay requests submitted by shift supervisors after the weekend.",
                "D) Require guests to clean their own rooms during peak occupancy periods."
            ],
            "correct": 0,
            "explanation": "Strategic HR balances guest service with labor expense by deploying cross-trained utility pools on regular pay bands before resorting to costly penalty overtime rates.",
            "memory_anchor": "🏨 Like pulling cross-trained pool staff to work front desk check-in when a 10-bus tour group arrives at once—uses regular pay instead of paying double overtime!",
            "competency": "Business Acumen & Workforce Analytics"
        },
        {
            "type": "Situational Judgment Item (SJI)",
            "chapter": "Resort Collective Bargaining & Union Grievances",
            "scenario": "During peak dinner service in a resort's primary steakhouse, a Food & Beverage manager assigns a non-union supervisor to clear dining tables because three busboys called in sick. The union shop steward files a formal Step-1 grievance alleging bargaining unit infringement. How should HR handle the response?",
            "options": [
                "A) Review the Collective Bargaining Agreement (CBA) emergency clauses, meet with the steward, and enforce proper bargaining unit work definitions while addressing staffing coverage.",
                "B) Fire the shop steward for interfering with peak dinner service.",
                "C) Ignore the grievance since guest service takes priority over written labor union contracts.",
                "D) Transfer all non-union supervisors to off-site administrative roles."
            ],
            "correct": 0,
            "explanation": "CBA terms are legally binding agreements. HR must maintain operational trust by strictly respecting bargaining unit work definitions while utilizing contractual emergency or call-in provisions.",
            "memory_anchor": "🤝 Like referees in sports: managers can't run onto the field and play for the team. HR must follow the contract rulebook so the union doesn't penalty-flag the resort!",
            "competency": "Labor & Employee Relations"
        },
        {
            "type": "Knowledge Item",
            "chapter": "Workplace Safety & Resort EHS",
            "scenario": "Under OSHA guidelines, what protocol must a resort hotel execute before maintenance engineers perform repairs inside confined industrial laundry equipment or walk-in freezers?",
            "options": [
                "A) Lockout/Tagout (LOTO) Energy Control Procedures",
                "B) General Liability Audit Clearance",
                "C) Guest Experience Exemption Filing",
                "D) Annual Hazard Communication Posting"
            ],
            "correct": 0,
            "explanation": "OSHA's Lockout/Tagout standard prevents accidental machinery re-energization during maintenance in hazardous or confined resort spaces.",
            "memory_anchor": "🔑 Putting an actual padlock on the freezer or washer power switch and keeping the key in your pocket so nobody turns it on while you are fixing it!",
            "competency": "Workplace Safety & Risk Management"
        },
        {
            "type": "Situational Judgment Item (SJI)",
            "chapter": "AI Scheduling & Workforce Intelligence",
            "scenario": "A luxury boutique hotel deploys an automated AI shift-scheduling tool linked to the Property Management System (PMS). Room attendants report that the AI regularly schedules 15 check-out room cleans in a single 4-hour window, leading to severe fatigue. How should HR guide management?",
            "options": [
                "A) Audit the AI algorithm's workload inputs against realistic housekeeping physical standards and adjust parameters with the software vendor.",
                "B) Instruct room attendants to work faster to meet the automated system outputs.",
                "C) Deactivate the entire automated PMS system and return to hand-written schedules.",
                "D) Discipline room attendants who fail to complete the 15 rooms."
            ],
            "correct": 0,
            "explanation": "AI scheduling tools must be continuously validated against real-world human physical capabilities and operational standards to prevent burnout and safety hazards.",
            "memory_anchor": "🤖 A computer doesn't know how heavy a king-size mattress is! HR must adjust the software settings when the robot gives humans impossible deadlines.",
            "competency": "Critical Evaluation & AI Governance"
        }
    ]

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
    st.error("⚠️ Question bank is empty.")
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
