import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="SHRM-CP HR Odyssey: Gamified Exam Prep",
    page_icon="🏆",
    layout="wide",
)

# Initialize Session State for Game Progression
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

# Comprehensive Question Bank (SJIs and Knowledge Items)
QUESTIONS = [
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Chapter 1: Total Rewards & Turnover Crisis",
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
            "The correct answer is C. Modern workforce demands and global"
            " shifts require flexibility to maintain engagement and reduce"
            " turnover. Offering flexible schedule options directly addresses"
            " the root cause while remaining competitive."
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
                "A) Advise managers to develop and oversee programs for their"
                " respective departments[cite: 4]."
            ),
            (
                "B) Issue a memo to employees that outlines the program and"
                " expectations[cite: 4]."
            ),
            (
                "C) Work with stakeholders to implement a strategy across the"
                " organization[cite: 4]."
            ),
            (
                "D) Hire a consultant skilled in this area to lead the program"
                " and implementation[cite: 4]."
            ),
        ],
        "correct": 2,
        "explanation": (
            "The correct answer is C. Strategic HR initiatives require cross-functional"
            " stakeholder alignment and organizational-wide integration rather"
            " than siloed department execution or top-down memos alone."
        ),
        "competency": "Leadership & Navigation",
    },
    {
        "type": "Knowledge Item",
        "chapter": "Chapter 3: Talent Acquisition & Onboarding",
        "scenario": (
            "A regional hospitality property is preparing to onboard a large"
            " wave of seasonal staff. According to SHRM best practice, what"
            " is the primary factor to establish early trust and productivity"
            "[cite: 10]?"
        ),
        "options": [
            "A) Ensure an onboarding plan is in place[cite: 10].",
            "B) Require immediate weekend shifts without prior notice.",
            "C) Delay benefits enrollment until contracts conclude.",
            "D) Minimize orientation time to put staff on the floor faster.",
        ],
        "correct": 0,
        "explanation": (
            "The correct answer is A. Ensuring an onboarding plan is in place"
            " is correct because it sets seasonal staff up for success with a"
            " solid onboarding experience, providing the resources and tools"
            " they need upfront[cite: 10]."
        ),
        "competency": "People / HR Expertise",
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Chapter 4: Employee Relations & Performance Management",
        "scenario": (
            "An HR recruiter with four years of high performance experiences a"
            " sudden drop in engagement and output following a denied promotion"
            "[cite: 7, 8]. The recruiter feels the evaluation process was"
            " unfair and that their supervisor is unreceptive[cite: 8]. After"
            " investigating, what should the HR manager do to resolve the issue"
            "[cite: 8]?"
        ),
        "options": [
            (
                "A) Inform the recruiter's supervisor about the recruiter's"
                " opinions and advise the supervisor to meet with the"
                " recruiter[cite: 9]."
            ),
            (
                "B) Send the recruiter resources for in-house skills training"
                " to help improve."
            ),
            (
                "C) Reassign the recruiter to a different hiring manager"
                " immediately."
            ),
            (
                "D) Issue a formal written warning regarding declining"
                " response times."
            ),
        ],
        "correct": 0,
        "explanation": (
            "The correct answer is A. Addressing communication breakdowns"
            " collaboratively by bridging dialogue between the employee and"
            " supervisor restores trust and targets the root cause of the"
            " grievance."
        ),
        "competency": "Ethical Practice & Consultation",
    },
    {
        "type": "Knowledge Item",
        "chapter": "Chapter 5: Workforce Planning & Metrics",
        "scenario": (
            "When calculating the cost-per-hire metric for an organization,"
            " which of the following expenses should typically be excluded"
            " from internal recruitment cost calculations?"
        ),
        "options": [
            "A) Recruiter salaries and benefits.",
            "B) Advertising and job board posting fees.",
            (
                "C) Lost productivity of existing staff during vacancy"
                " periods."
            ),
            "D) Third-party agency search fees.",
        ],
        "correct": 2,
        "explanation": (
            "The correct answer is C. While lost productivity represents a"
            " business impact of a vacancy, standard cost-per-hire formulas"
            " focus on direct internal and external recruitment expenditures"
            " rather than indirect productivity loss."
        ),
        "competency": "Business Acumen",
    },
]

# Sidebar - Gamified Status Dashboard
st.sidebar.title("🎮 HR Odyssey Dashboard")
st.sidebar.markdown(f"**Consultant:** Senior HR Strategist")
st.sidebar.markdown(f"**XP Earned:** `{st.session_state.xp} XP`")
st.sidebar.progress(st.session_state.morale / 100)
st.sidebar.markdown(f"❤️ **Team Morale:** `{st.session_state.morale}%`")
st.sidebar.markdown("---")
st.sidebar.info(
    "Tip: Answer carefully! Correct choices boost your consulting reputation"
    " and unlock advanced SHRM exam scenarios."
)

# Main Title & Story Header
st.title("🏆 SHRM-CP Exam Prep: The Corporate Odyssey")
st.markdown(
    "Welcome to your interactive prep journey. Navigate real-world HR"
    " scenarios, master the SHRM BASK competencies, and conquer the exam!"
)
st.markdown("---")

# Quiz Logic
if st.session_state.step < len(QUESTIONS):
  q = QUESTIONS[st.session_state.step]

  st.subheader(f"{q['chapter']} — *{q['type']}*")
  st.info(f"**Core Competency Focus:** {q['competency']}")

  st.write(f"### Scenario / Question:")
  st.write(q["scenario"])

  # Form for answering
  with st.form(f"question_form_{st.session_state.step}"):
    choice = st.radio("Select your best HR action:", q["options"])
    submitted = st.form_submit_button("Submit Decision")

    if submitted:
      selected_index = q["options"].index(choice)
      st.session_state.quiz_submitted = True
      st.session_state.selected_index = selected_index

  if st.session_state.get("quiz_submitted", False):
    selected_index = st.session_state.selected_index
    if selected_index == q["correct"]:
      st.success("✅ **Brilliant Decision!** Strategic alignment achieved.")
      if not st.session_state.get("scored_current", False):
        st.session_state.score += 1
        st.session_state.xp += 150
        st.session_state.scored_current = True
    else:
      st.error("❌ **Suboptimal Choice.** This could increase organizational friction.")
      if not st.session_state.get("scored_current", False):
        st.session_state.morale = max(0, st.session_state.morale - 15)
        st.session_state.scored_current = True

    st.markdown("### 💡 Expert Rationale:")
    st.write(q["explanation"])

    if st.button("Proceed to Next Challenge ➡️"):
      st.session_state.step += 1
      st.session_state.quiz_submitted = False
      st.session_state.scored_current = False
      st.rerun()

else:
  # Completion Screen
  st.balloons()
  st.success("🎉 **Congratulations! You have completed the HR Odyssey Bootcamp!**")
  st.markdown(f"### Final Score: `{st.session_state.score}/{len(QUESTIONS)}`")
  st.markdown(f"### Total XP Accumulated: `{st.session_state.xp} XP`")

  if st.session_state.morale > 70:
    st.info(
        "🌟 **Evaluation:** Exceptional judgment! You are displaying the"
        " strategic mindset of a certified SHRM-CP professional ready for exam"
        " day."
    )
  else:
    st.warning(
        "⚠️ **Evaluation:** You passed the simulation, but review your"
        " situational judgment rationale around stakeholder alignment and"
        " employee relations."
    )

  if st.button("🔄 Restart Journey"):
    st.session_state.step = 0
    st.session_state.score = 0
    st.session_state.xp = 0
    st.session_state.morale = 100
    st.session_state.quiz_submitted = False
    st.rerun()
