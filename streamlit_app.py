import json
import os
import streamlit as st

# Page Configuration & Metadata
st.set_page_config(
    page_title="MAREC Insights | SHRM-CP HR Odyssey",
    page_icon="🦜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# MAREC Insights Brand Assets
LOGO_URL = "https://raw.githubusercontent.com/markreciopro/marec_insights/main/Gemini_Generated_Image_noss7snoss7snoss.jpg"

# Custom CSS for MAREC Insights Branding & Custom Background
st.markdown(
    f"""
    <style>
    /* Main Background Styling */
    .stApp {{
        background-color: #f8fafc;
    }}
    
    /* Sidebar Customization */
    [data-testid="stSidebar"] {{
        background-color: #0f172a !important;
        color: #f8fafc !important;
    }}
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p, [data-testid="stSidebar"] div {{
        color: #f8fafc !important;
    }}
    
    /* MAREC Insights Custom Header Card */
    .brand-card {{
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
        border-left: 6px solid #0ea5e9;
        padding: 24px;
        border-radius: 12px;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }}
    .brand-card h1 {{
        color: #ffffff !important;
        font-size: 2.2rem;
        font-weight: 700;
        margin: 0;
    }}
    .brand-card p {{
        color: #38bdf8 !important;
        font-size: 1.1rem;
        margin-top: 6px;
        margin-bottom: 0;
    }}

    /* Question Box Styling */
    .question-box {{
        background-color: #ffffff;
        border-radius: 12px;
        padding: 24px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
    }}

    /* Custom Streamlit Buttons */
    .stButton>button {{
        background: linear-gradient(135deg, #0ea5e9 0%, #0369a1 100%);
        color: white !important;
        border-radius: 8px;
        font-weight: 600;
        font-size: 1rem;
        padding: 0.6rem 1.4rem;
        border: none;
        transition: all 0.3s ease;
    }}
    .stButton>button:hover {{
        background: linear-gradient(135deg, #0284c7 0%, #075985 100%);
        box-shadow: 0 4px 12px rgba(14, 165, 233, 0.3);
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Load Question Bank (Reads questions.json if available, otherwise uses built-in set)
FALLBACK_QUESTIONS = [
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Chapter 1: Total Rewards & Workplace Retention",
        "scenario": (
            "A chief human resource officer is evaluating the company's total"
            " rewards strategy after experiencing higher than normal turnover"
            " due to a global shift in work styles[cite: 3]. Which approach"
            " should the company take to retain and attract talent[cite: 3]?"
        ),
        "options": [
            "A) Reinforce strict operational policies and procedures[cite: 3].",
            "B) Participate in competitive salary and benefits surveys[cite: 3].",
            (
                "C) Offer flexible schedule and hybrid work options where"
                " feasible[cite: 3]."
            ),
            "D) Eliminate voluntary benefit plans to cut overhead[cite: 3].",
        ],
        "correct": 2,
        "explanation": (
            "Offering flexible schedule options directly addresses the root"
            " cause of modern turnover while maintaining market competitiveness"
            " and employee autonomy."
        ),
        "competency": "Relationship Management & Consultation",
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Chapter 2: Corporate Social Responsibility",
        "scenario": (
            "Which action should an HR manager take to implement a newly"
            " developed corporate social responsibility and sustainability"
            " program[cite: 4]?"
        ),
        "options": [
            (
                "A) Advise department managers to independently develop"
                " programs for their teams[cite: 4]."
            ),
            (
                "B) Issue an all-employee memo outlining the program and"
                " general expectations[cite: 4]."
            ),
            (
                "C) Work collaboratively with key stakeholders to implement a"
                " strategy across the organization[cite: 4]."
            ),
            (
                "D) Hire an external consultant exclusively to lead the program"
                " rollout[cite: 4]."
            ),
        ],
        "correct": 2,
        "explanation": (
            "Strategic HR initiatives require cross-functional stakeholder"
            " alignment and organization-wide integration rather than isolated"
            " department efforts or simple top-down memos."
        ),
        "competency": "Leadership & Navigation",
    },
    {
        "type": "Knowledge Item",
        "chapter": "Chapter 3: Strategic Onboarding & Orientation",
        "scenario": (
            "A resort property is preparing to onboard a large cohort of"
            " seasonal staff for peak convention season. According to SHRM best"
            " practice, what is the most critical priority to establish trust and"
            " productivity early[cite: 10]?"
        ),
        "options": [
            "A) Ensure a structured onboarding plan is in place[cite: 10].",
            "B) Assign mandatory weekend overtime shifts without prior notice.",
            "C) Delay health benefits registration until contract completion.",
            (
                "D) Streamline orientation to get staff working on the floor"
                " faster."
            ),
        ],
        "correct": 0,
        "explanation": (
            "A well-structured onboarding plan provides seasonal staff with the"
            " clarity, tools, and support needed to build organizational trust"
            " and drive peak performance[cite: 10]."
        ),
        "competency": "People / HR Expertise",
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Chapter 4: Employee Grievances & Performance Management",
        "scenario": (
            "An HR recruiter with four years of strong performance experiences"
            " a sudden drop in productivity following a passed-over promotion"
            "[cite: 7, 8]. The recruiter feels the process was unfair and that"
            " their manager is unreceptive[cite: 8]. What should the HR manager"
            " do to resolve the issue[cite: 8]?"
        ),
        "options": [
            (
                "A) Inform the recruiter's supervisor of the concerns and"
                " facilitate a structured meeting between them[cite: 9]."
            ),
            (
                "B) Send the recruiter links to self-paced skill development"
                " modules."
            ),
            (
                "C) Immediately reassign the recruiter to a different"
                " department manager."
            ),
            (
                "D) Issue a formal written warning regarding declining email"
                " response times."
            ),
        ],
        "correct": 0,
        "explanation": (
            "Bridging communication between the employee and manager directly"
            " targets the root cause of the grievance, restoring trust and"
            " supporting mutual accountability."
        ),
        "competency": "Ethical Practice & Consultation",
    },
    {
        "type": "Knowledge Item",
        "chapter": "Chapter 5: Workforce Intelligence & Metrics",
        "scenario": (
            "When calculating standard Cost-Per-Hire (CPH) for an organizational"
            " audit, which expense should be excluded from recruitment"
            " costs?"
        ),
        "options": [
            "A) Recruiter salaries and administrative overhead.",
            "B) Third-party job board posting fees.",
            "C) Estimated lost productivity of team during vacancy.",
            "D) External executive search firm fees.",
        ],
        "correct": 2,
        "explanation": (
            "Standard CPH calculations focus exclusively on direct internal and"
            " external sourcing costs rather than indirect productivity losses."
        ),
        "competency": "Business Acumen & Analytics",
    },
]


@st.cache_data
def load_question_bank():
  if os.path.exists("questions.json"):
    try:
      with open("questions.json", "r") as f:
        data = json.load(f)
        if data and isinstance(data, list):
          return data
    except Exception:
      pass
  return FALLBACK_QUESTIONS


QUESTIONS = load_question_bank()

# Initialize Game Session State
if "step" not in st.session_state:
  st.session_state.step = 0
if "score" not in st.session_state:
  st.session_state.score = 0
if "xp" not in st.session_state:
  st.session_state.xp = 0
if "morale" not in st.session_state:
  st.session_state.morale = 100
if "quiz_submitted" not in st.session_state:
  st.session_state.quiz_submitted = False

# Sidebar with Logo & Gamified Metrics
with st.sidebar:
  try:
    st.image(
        LOGO_URL,
        caption="MAREC Insights Workforce Intelligence",
        use_container_width=True,
    )
  except Exception:
    st.title("🦜 MAREC Insights")

  st.markdown("### 🏆 Exam Prep Navigator")
  st.markdown("**Consultant Rank:** Senior HR Strategist")
  st.markdown(f"**XP Accumulated:** `{st.session_state.xp} XP`")
  st.markdown(f"**Total Loaded Items:** `{len(QUESTIONS)} Questions`")

  # Morale Progress Bar
  st.markdown("---")
  st.markdown(f"**Team Morale:** `{st.session_state.morale}%`")
  st.progress(st.session_state.morale / 100)

  st.markdown("---")
  st.info(
      "💡 **SHRM SJI Strategy:** Look for options that prioritize root-cause"
      " analysis, stakeholder alignment, and sustainable policy over quick"
      " punitive steps."
  )

# Main Banner Area
st.markdown(
    """
    <div class="brand-card">
        <h1>MAREC Insights | SHRM-CP HR Odyssey</h1>
        <p>Workforce Intelligence & Behavioral Competency Simulator</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# App Navigation / Game Engine Logic
if st.session_state.step < len(QUESTIONS):
  q = QUESTIONS[st.session_state.step]

  st.markdown(
      f"### Question {st.session_state.step + 1} of {len(QUESTIONS)}:"
      f" {q.get('chapter', 'SHRM BASK Focus')}"
  )
  st.write(f"**Item Type:** `{q.get('type', 'SHRM Exam Question')}`")
  st.info(f"🎯 **Core Competency:** {q.get('competency', 'HR Leadership')}")

  # Scenario Card
  st.markdown(
      f"""
    <div class="question-box">
        <h4>Scenario Challenge:</h4>
        <p style="font-size: 1.1rem; color: #1e293b;">{q['scenario']}</p>
    </div>
    """,
      unsafe_allow_html=True,
  )

  # Form Submission
  with st.form(f"question_form_{st.session_state.step}"):
    choice = st.radio("Select the most effective HR response:", q["options"])
    submitted = st.form_submit_button("Submit Strategic Decision")

    if submitted:
      selected_index = q["options"].index(choice)
      st.session_state.quiz_submitted = True
      st.session_state.selected_index = selected_index

  # Answer Feedback Logic
  if st.session_state.get("quiz_submitted", False):
    selected_index = st.session_state.selected_index
    if selected_index == q["correct"]:
      st.success("✅ **Strategic Alignment Achieved!** Exemplary SHRM decision.")
      if not st.session_state.get("scored_current", False):
        st.session_state.score += 1
        st.session_state.xp += 250
        st.session_state.scored_current = True
    else:
      st.error(
          "❌ **Suboptimal Choice.** This action risks organizational friction"
          " or skips vital stakeholder alignment."
      )
      if not st.session_state.get("scored_current", False):
        st.session_state.morale = max(0, st.session_state.morale - 15)
        st.session_state.scored_current = True

    # Expert Rationale Card
    st.markdown("---")
    st.markdown("### 💡 Expert Rationale & SHRM Best Practice:")
    st.write(q["explanation"])

    if st.button("Proceed to Next Challenge ➡️"):
      st.session_state.step += 1
      st.session_state.quiz_submitted = False
      st.session_state.scored_current = False
      st.rerun()

else:
  # Final Assessment Screen
  st.balloons()
  st.success("🎉 **Congratulations! You completed the SHRM-CP HR Odyssey!**")

  col1, col2 = st.columns(2)
  with col1:
    st.metric("Final Score", f"{st.session_state.score} / {len(QUESTIONS)}")
  with col2:
    st.metric("Total XP Earned", f"{st.session_state.xp} XP")

  if st.session_state.morale >= 70:
    st.info(
        "🌟 **Evaluation:** Outstanding performance! Your strategic vision and"
        " judgment align with SHRM-CP standards."
    )
  else:
    st.warning(
        "⚠️ **Evaluation:** Simulation completed. Review key behavioral"
        " competencies in Consultation and Leadership to boost your exam day"
        " score."
    )

  if st.button("🔄 Restart Practice Simulator"):
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.xp = 0
    st.session_state.morale = 100
    st.session_state.quiz_submitted = False
    st.rerun()
