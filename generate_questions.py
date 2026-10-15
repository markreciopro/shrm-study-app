import json

questions = [
    # --- 1 to 20 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Total Rewards & Retention Strategy",
        "scenario": "A chief human resource officer is evaluating the company's total rewards strategy after experiencing higher than normal turnover due to a global shift in work styles. Which approach should the company take to retain and attract talent?",
        "options": [
            "A) Reinforce strict operational policies and procedures.",
            "B) Participate in competitive salary and benefits surveys.",
            "C) Offer flexible schedule and hybrid work options where feasible.",
            "D) Eliminate voluntary benefit plans to cut overhead."
        ],
        "correct": 2,
        "explanation": "Offering flexible schedule options directly addresses the root cause of modern turnover while maintaining market competitiveness and employee autonomy.",
        "competency": "Relationship Management & Consultation"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Corporate Social Responsibility",
        "scenario": "Which action should an HR manager take to implement a newly developed corporate social responsibility and sustainability program?",
        "options": [
            "A) Advise department managers to independently develop programs for their teams.",
            "B) Issue an all-employee memo outlining the program and general expectations.",
            "C) Work collaboratively with key stakeholders to implement a strategy across the organization.",
            "D) Hire an external consultant exclusively to lead the program rollout."
        ],
        "correct": 2,
        "explanation": "Strategic HR initiatives require cross-functional stakeholder alignment and organization-wide integration rather than isolated department efforts or simple top-down memos.",
        "competency": "Leadership & Navigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Onboarding & Orientation",
        "scenario": "A resort property is preparing to onboard a large cohort of seasonal staff for peak convention season. According to SHRM best practice, what is the most critical priority to establish trust and productivity early?",
        "options": [
            "A) Ensure a structured onboarding plan is in place.",
            "B) Assign mandatory weekend overtime shifts without prior notice.",
            "C) Delay health benefits registration until contract completion.",
            "D) Streamline orientation to get staff working on the floor faster."
        ],
        "correct": 0,
        "explanation": "A well-structured onboarding plan provides seasonal staff with the clarity, tools, and support needed to build organizational trust and drive peak performance.",
        "competency": "People / HR Expertise"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Grievances & Performance Management",
        "scenario": "An HR recruiter with four years of strong performance experiences a sudden drop in productivity following a passed-over promotion. The recruiter feels the process was unfair and that their manager is unreceptive. What should the HR manager do to resolve the issue?",
        "options": [
            "A) Inform the recruiter's supervisor of the concerns and facilitate a structured meeting between them.",
            "B) Send the recruiter links to self-paced skill development modules.",
            "C) Immediately reassign the recruiter to a different department manager.",
            "D) Issue a formal written warning regarding declining email response times."
        ],
        "correct": 0,
        "explanation": "Bridging communication between the employee and manager directly targets the root cause of the grievance, restoring trust and supporting mutual accountability.",
        "competency": "Ethical Practice & Consultation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Workforce Intelligence & Metrics",
        "scenario": "When calculating standard Cost-Per-Hire (CPH) for an organizational audit, which expense should be excluded from recruitment costs?",
        "options": [
            "A) Recruiter salaries and administrative overhead.",
            "B) Third-party job board posting fees.",
            "C) Estimated lost productivity of team during vacancy.",
            "D) External executive search firm fees."
        ],
        "correct": 2,
        "explanation": "Standard CPH calculations focus exclusively on direct internal and external sourcing costs rather than indirect productivity losses.",
        "competency": "Business Acumen & Analytics"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Employment Law & Compliance",
        "scenario": "Under the Fair Labor Standards Act (FLSA), which primary criteria must be met for an employee to be classified as exempt under the administrative exemption?",
        "options": [
            "A) Paid on a salary basis at or above the threshold and primary duty includes exercise of discretion regarding matters of significance.",
            "B) Works more than 40 hours per week and manages at least two full-time employees.",
            "C) Holds a bachelor's degree in business administration or related field.",
            "D) Receives commission pay exceeding 50% of total annual compensation."
        ],
        "correct": 0,
        "explanation": "FLSA administrative exemption requires meeting the minimum salary threshold, salary basis test, and primary duties involving independent discretion on significant business matters.",
        "competency": "HR Expertise (Workplace)"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Diversity, Equity & Inclusion (DEI)",
        "scenario": "During a leadership meeting, department heads express concern that a newly proposed diversity mentoring initiative will lead to reverse discrimination. How should the HR Director respond?",
        "options": [
            "A) Cancel the initiative to avoid leadership friction and potential employee discontent.",
            "B) Present data on how inclusive talent development drives innovation, organizational agility, and market performance.",
            "C) Mandate that all managers attend compulsory diversity sensitivity training immediately.",
            "D) Limit program participation strictly to entry-level individual contributors."
        ],
        "correct": 1,
        "explanation": "Effective HR leaders use data-driven business cases to align leadership, demystify DEI programs, and highlight organizational benefits.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Acquisition Strategy",
        "scenario": "Which sourcing technique involves identifying potential high-performing candidates who are not actively seeking new employment?",
        "options": [
            "A) Passive candidate recruitment",
            "B) Inbound applicant tracking",
            "C) Contingent labor staffing",
            "D) Open job fair sourcing"
        ],
        "correct": 0,
        "explanation": "Passive candidate sourcing targets employed professionals who aren't active job seekers, expanding talent quality for critical roles.",
        "competency": "People / Talent Sourcing"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Change Management & Organizational Design",
        "scenario": "An organization is restructuring its operations team to move from regional units to centralized cross-functional project squads. Frontline supervisors are resisting the transition. What is HR's best initial action?",
        "options": [
            "A) Escalate supervisor resistance directly to executive leadership for disciplinary review.",
            "B) Conduct stakeholder alignment sessions with supervisors to clarify role expectations and address specific operational concerns.",
            "C) Postpone the restructuring rollout by 12 months.",
            "D) Issue standardized job descriptions without holding discussion meetings."
        ],
        "correct": 1,
        "explanation": "Change management requires active stakeholder engagement and clear communication to resolve ambiguity and foster buy-in.",
        "competency": "Leadership & Navigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Risk Management & Safety",
        "scenario": "Under OSHA guidelines, what is the primary obligation of the General Duty Clause for employers?",
        "options": [
            "A) Provide a workplace free from recognized hazards that cause or are likely to cause death or serious physical harm.",
            "B) Provide comprehensive medical coverage for all workplace injuries regardless of fault.",
            "C) Inspect all physical facilities on a bi-weekly basis with certified external inspectors.",
            "D) Restrict employees from working shifts exceeding 10 hours per day."
        ],
        "correct": 0,
        "explanation": "OSHA's General Duty Clause mandates that employers maintain a workplace free from recognized safety and health hazards.",
        "competency": "Workplace Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Learning & Development Strategies",
        "scenario": "When conducting a Needs Assessment for organizational training, which step must HR complete first to ensure alignment with business goals?",
        "options": [
            "A) Organizational analysis to identify strategic goals and operational priorities.",
            "B) Individual performance appraisal reviews across all business units.",
            "C) Selecting external training vendors and software platforms.",
            "D) Administering employee satisfaction surveys regarding preferred learning styles."
        ],
        "correct": 0,
        "explanation": "A training needs assessment begins with organizational analysis to align training interventions with corporate objectives and strategic initiatives.",
        "competency": "People / Learning & Development"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Engagement & Retention",
        "scenario": "An HR Manager notices that exit interview data for software engineers shows a consistent complaint: lack of professional growth opportunities. How should HR address this systemic issue?",
        "options": [
            "A) Partner with engineering leadership to design dual-career ladders and technical leadership pathways.",
            "B) Increase starting base salaries for all newly hired software engineers by 15%.",
            "C) Require departing employees to complete a second, detailed exit survey.",
            "D) Conduct mandatory stay interviews only for high-performing senior executives."
        ],
        "correct": 0,
        "explanation": "Dual-career ladders allow individual contributors to advance professionally and financially without having to move into administrative management roles.",
        "competency": "Relationship Management & Talent Strategy"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Compensation",
        "scenario": "In job evaluation methodology, which non-quantitative method involves comparing whole jobs against each other based on their overall worth to the organization?",
        "options": [
            "A) Job Ranking Method",
            "B) Point-Factor Method",
            "C) Factor Comparison Method",
            "D) Market Pay Pricing Method"
        ],
        "correct": 0,
        "explanation": "The Job Ranking Method is a qualitative, whole-job evaluation technique where jobs are ordered sequentially from highest to lowest value.",
        "competency": "HR Expertise (Total Rewards)"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Labor & Employee Relations",
        "scenario": "During a union organizing campaign, a department supervisor asks an HR professional if they can inform employees about the negative aspects of unionization. How should HR advise the supervisor under TIPSS guidelines?",
        "options": [
            "A) Supervisors may share facts, opinions, and personal experiences, but must strictly avoid Threats, Interrogations, Promises, or Surveillance (TIPS).",
            "B) Supervisors are legally prohibited from speaking about unions under any circumstances.",
            "C) Supervisors may promise wage increases if employees vote against union representation.",
            "D) Supervisors should conduct one-on-one interrogations to identify union organizers."
        ],
        "correct": 0,
        "explanation": "Under the NLRA, management may share factual information and opinions (TIPS rule) as long as they do not Threaten, Interrogate, Promise, or Spy.",
        "competency": "Workplace / Employee & Labor Relations"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Organizational Structure & Design",
        "scenario": "Which organizational structure groups employees by both functional specialty and project product lines, leading to a dual-chain of command?",
        "options": [
            "A) Matrix Structure",
            "B) Divisional Structure",
            "C) Functional Structure",
            "D) Geographic Structure"
        ],
        "correct": 0,
        "explanation": "A Matrix structure overlay creates dual reporting relationships, balancing functional expertise with project agility.",
        "competency": "Structure & HR Service Delivery"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Ethics & Professional Conduct",
        "scenario": "An HR specialist discovers that a hiring manager routinely passes over qualified older candidates for entry-level tech roles in favor of recent college graduates. What is HR's immediate duty?",
        "options": [
            "A) Audit the department's hiring records and review compliance under the Age Discrimination in Employment Act (ADEA) with leadership.",
            "B) Ignore the pattern since entry-level roles naturally favor younger candidates.",
            "C) Inform affected applicants directly so they can file private lawsuits.",
            "D) Reassign the hiring manager to non-hiring administrative duties without investigation."
        ],
        "correct": 0,
        "explanation": "HR must enforce compliance with federal anti-discrimination laws like ADEA (protecting workers 40+) through impartial audits and management counsel.",
        "competency": "Ethical Practice"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Global HR & Talent Management",
        "scenario": "Which international compensation approach compensates expatriate employees by maintaining their home-country purchasing power?",
        "options": [
            "A) Balance Sheet Approach",
            "B) Local Market Rate Approach",
            "C) Lump-Sum Allowance Method",
            "D) Global Tiered Salary Model"
        ],
        "correct": 0,
        "explanation": "The Balance Sheet Approach ensures expatriates experience neither financial gain nor loss regarding standard of living during global assignments.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Performance Management Strategy",
        "scenario": "A company is transitioning from annual performance reviews to continuous feedback and monthly check-ins. Managers report feeling overwhelmed by the administrative burden. How should HR assist?",
        "options": [
            "A) Provide lightweight check-in templates, automated calendar reminders, and concise manager coaching modules.",
            "B) Revert immediately back to the traditional once-a-year review system.",
            "C) Make monthly check-ins optional for all department supervisors.",
            "D) Penalize managers who miss monthly feedback submissions by withholding bonuses."
        ],
        "correct": 0,
        "explanation": "HR supports operational change by reducing administrative friction through simple tools, training, and streamlined workflows.",
        "competency": "Consultation & Enablement"
    },
    {
        "type": "Knowledge Item",
        "chapter": "HR Technology & Analytics",
        "scenario": "What is the primary benefit of deploying a unified Human Resource Information System (HRIS) across an enterprise?",
        "options": [
            "A) Centralized data management, streamlined employee self-service, and improved data-driven decision analytics.",
            "B) Eliminating the need for dedicated HR business partners in business units.",
            "C) Automatic compliance guarantees with all state and federal labor laws.",
            "D) Replacing line managers' involvement in employee performance evaluations."
        ],
        "correct": 0,
        "explanation": "An HRIS integrates employee data streams, automates routine operational tasks, and provides analytics for strategic workforce decisions.",
        "competency": "Business Acumen & HR Systems"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workforce Planning & Succession",
        "scenario": "A critical executive announces an unexpected retirement in 30 days, and no internal successor has been identified. What should HR prioritize in the short term?",
        "options": [
            "A) Implement an emergency knowledge-transfer protocol while launching an interim leadership plan and target executive search.",
            "B) Promote the most senior manager in the department regardless of technical readiness.",
            "C) Freeze all department operations until a permanent replacement is hired.",
            "D) Ask the retiring executive to stay indefinitely without an exit contract."
        ],
        "correct": 0,
        "explanation": "Unplanned executive departures require immediate risk mitigation through knowledge capture, temporary leadership stability, and parallel executive sourcing.",
        "competency": "Critical Evaluation & Talent Strategy"
    },

    # --- 21 to 40 ---
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Employment Law & Equal Opportunity",
        "scenario": "Under Title VII of the Civil Rights Act of 1964, which employer practice is prohibited unless justified by a Bona Fide Occupational Qualification (BFOQ)?",
        "options": [
            "A) Disparate treatment discrimination based on race, color, religion, sex, or national origin.",
            "B) Implementing mandatory background checks for all applicants.",
            "C) Requiring physical agility tests for heavy labor roles.",
            "D) Offering higher compensation based on geographic cost-of-living differences."
        ],
        "correct": 0,
        "explanation": "Title VII prohibits discrimination based on protected classes unless a narrow BFOQ exemption applies (note: race can never be a BFOQ).",
        "competency": "HR Expertise (Workplace Compliance)"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Health, Safety & Wellness",
        "scenario": "An employee requests a standing desk as a reasonable accommodation under the Americans with Disabilities Act (ADA) for a medical back condition. The supervisor denies it, claiming it exceeds the team's office supply budget. What should HR do?",
        "options": [
            "A) Overrule the supervisor and initiate the interactive process to evaluate the ADA accommodation request objectively.",
            "B) Support the supervisor's decision to preserve department budget constraints.",
            "C) Tell the employee to purchase their own standing desk and bring it to work.",
            "D) Transfer the employee to a work-from-home role immediately without medical documentation."
        ],
        "correct": 0,
        "explanation": "ADA compliance requires engaging in an interactive process to assess accommodations; department budget limits rarely satisfy the high threshold for 'undue hardship.'",
        "competency": "Consultation & Legal Compliance"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Sourcing & Selection",
        "scenario": "What is the primary statistical indicator used to evaluate whether a selection test or interview process disproportionately screens out protected groups under the EEOC Uniform Guidelines?",
        "options": [
            "A) Four-Fifths (80%) Rule",
            "B) Standard Deviation Variance Test",
            "C) Pearson Correlation Coefficient",
            "D) Cronbach's Alpha Reliability Metric"
        ],
        "correct": 0,
        "explanation": "The Four-Fifths Rule compares selection rates for protected groups against the highest selection rate group to determine potential adverse impact.",
        "competency": "Critical Evaluation & Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Compensation & Pay Equity",
        "scenario": "An internal compensation audit reveals that female managers in a hospitality unit earn 12% less on average than male managers in identical roles with similar tenure. How should HR respond?",
        "options": [
            "A) Conduct a comprehensive regression analysis controlling for performance, tenure, and scope, and adjust salaries where pay gaps are unjustified.",
            "B) Wait until the annual performance review cycle to address pay differences gradually.",
            "C) Inform affected female managers that market rates varied at their time of hire.",
            "D) Freeze salaries for male managers until parity is naturally achieved."
        ],
        "correct": 0,
        "explanation": "Unexplained pay disparities pose significant legal and ethical risks; HR must analyze contributing factors and make targeted equity adjustments.",
        "competency": "Business Acumen & Total Rewards"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Management & HR Alignment",
        "scenario": "Which strategic framework analyzes internal Strengths and Weaknesses along with external Opportunities and Threats to guide HR strategy formulation?",
        "options": [
            "A) SWOT Analysis",
            "B) PESTLE Analysis",
            "C) Porter's Five Forces",
            "D) Balanced Scorecard"
        ],
        "correct": 0,
        "explanation": "SWOT Analysis evaluates internal organizational capabilities (S/W) against external environment dynamics (O/T).",
        "competency": "Leadership & Navigation"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Organizational Culture & Employee Morale",
        "scenario": "Following a rapid corporate acquisition, employees at the acquired firm report high anxiety and fear of layoffs, causing productivity to decline sharply. What is HR's priority?",
        "options": [
            "A) Launch a transparent cross-organizational communication strategy and host open town hall forums with executive leaders.",
            "B) Send an automated email advising employees to focus on daily tasks.",
            "C) Offer voluntary severance packages to anyone expressing concern.",
            "D) Delay all integration announcements until decisions are 100% finalized."
        ],
        "correct": 0,
        "explanation": "Proactive, transparent communication during M&A integration reduces uncertainty, retains key talent, and stabilizes employee morale.",
        "competency": "Relationship Management & Communication"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Labor Relations & Union Regulations",
        "scenario": "Under the National Labor Relations Act (NLRA), what term describes concerted employee activities protected regardless of whether a workplace is unionized?",
        "options": [
            "A) Protected Concerted Activity",
            "B) Collective Bargaining Exemption",
            "C) Mandatory Grievance Arbitration",
            "D) Closed Shop Enforcement"
        ],
        "correct": 0,
        "explanation": "NLRA Section 7 protects employees who discuss wages, working conditions, or safety concerns collectively, even in non-union environments.",
        "competency": "Workplace / Labor Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Learning & Development Implementation",
        "scenario": "A company invests in a state-of-the-art Learning Management System (LMS), but employee completion rates for mandatory compliance courses remain below 35%. How should HR address low adoption?",
        "options": [
            "A) Audit user experience, integrate micro-learning modules, and align completion with performance incentives.",
            "B) Make uncompleted courses grounds for immediate termination.",
            "C) Double the length of training modules to cover topics in greater depth.",
            "D) Abandon digital learning and return exclusively to in-person classroom seminars."
        ],
        "correct": 0,
        "explanation": "Low training adoption is best remedied by improving accessibility, shortening content delivery (micro-learning), and building manager accountability.",
        "competency": "Consultation & L&D"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Risk Management & Business Continuity",
        "scenario": "Which document outlines an organization's protocols for maintaining vital operational functions during an emergency or disaster?",
        "options": [
            "A) Business Continuity Plan (BCP)",
            "B) Equal Employment Opportunity Plan (EEOP)",
            "C) Key Performance Indicator Dashboard (KPI)",
            "D) Standard Operating Procedure (SOP)"
        ],
        "correct": 0,
        "explanation": "A Business Continuity Plan ensures essential functions continue during crises, protecting human capital and operational assets.",
        "competency": "Risk Management"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Performance Management & Accountability",
        "scenario": "A high-performing sales executive consistently violates internal expense reporting policies and submits late reports. The sales VP excuses the behavior due to revenue performance. How should HR advise?",
        "options": [
            "A) Partner with the VP to enforce policy compliance consistently across all staff, emphasizing ethical standards over sales revenue.",
            "B) Create a custom policy exemption exclusively for top revenue generators.",
            "C) Secretly approve the late expense reports without notifying finance.",
            "D) Publicly reprimand the sales executive in an all-staff newsletter."
        ],
        "correct": 0,
        "explanation": "Ethical practice requires consistent enforcement of company policies regardless of an individual's sales performance or rank.",
        "competency": "Ethical Practice & Leadership"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Leave Administration",
        "scenario": "Under the Family and Medical Leave Act (FMLA), how many weeks of job-protected, unpaid leave are eligible employees entitled to per 12-month period for qualifying family/medical reasons?",
        "options": [
            "A) 12 weeks",
            "B) 16 weeks",
            "C) 26 weeks",
            "D) 8 weeks"
        ],
        "correct": 0,
        "explanation": "FMLA provides up to 12 workweeks of unpaid, job-protected leave per year for qualifying reasons (and up to 26 weeks for military caregiver leave).",
        "competency": "HR Compliance & Benefits"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Global Mobility & Talent Strategy",
        "scenario": "An international hotel group is sending a senior manager on a 2-year assignment to launch a new resort in Asia. The manager experiences severe culture shock and performance drops. What should HR have provided pre-departure?",
        "options": [
            "A) Comprehensive cross-cultural immersion training and ongoing host-country mentoring support.",
            "B) A financial bonus paid entirely upfront prior to departure.",
            "C) Instructions to enforce home-country workplace norms without alteration.",
            "D) A guarantee of permanent promotion upon assignment completion."
        ],
        "correct": 0,
        "explanation": "Cross-cultural preparation and local mentorship mitigate assignment failure rates and support expatriate adaptation.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Analytics & Metrics",
        "scenario": "Which key HR metric measures the total voluntary and involuntary separations of employees over a specific period relative to average workforce headcount?",
        "options": [
            "A) Turnover Rate",
            "B) Absenteesim Rate",
            "C) Yield Ratio",
            "D) Time-to-Fill"
        ],
        "correct": 0,
        "explanation": "Turnover rate measures workforce attrition rate over a defined period.",
        "competency": "Business Acumen & Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Harassment & Conduct",
        "scenario": "An employee submits an anonymous complaint stating that a manager makes inappropriate sexual comments during team offsites. What is HR's mandatory first step?",
        "options": [
            "A) Initiate an immediate, objective, and confidential internal investigation regardless of the complaint's anonymity.",
            "B) Dismiss the complaint because it was submitted anonymously.",
            "C) Confront the manager directly in front of the entire team.",
            "D) Reassign the reporting employee to a different shift immediately."
        ],
        "correct": 0,
        "explanation": "HR has a legal obligation to promptly investigate harassment allegations, even when received anonymously.",
        "competency": "Ethical Practice & Risk Mitigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Employee Benefits & Retirement",
        "scenario": "Under ERISA regulations, which document must employers provide to plan participants detailing employee benefit plan features, funding, and rights?",
        "options": [
            "A) Summary Plan Description (SPD)",
            "B) Form 5500 Annual Audit Report",
            "C) COBRA Election Notice",
            "D) W-4 Tax Withholding Certificate"
        ],
        "correct": 0,
        "explanation": "ERISA mandates that employers issue a Summary Plan Description (SPD) to clearly explain benefit plan rules and participant rights.",
        "competency": "Total Rewards Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Strategic Workforce Planning",
        "scenario": "A company plans to automate 30% of its customer support functions over the next two years. What proactive strategy should HR implement for affected staff?",
        "options": [
            "A) Develop a skill gap analysis and establish internal reskilling and career transition pathways for vulnerable workers.",
            "B) Terminate all customer support staff immediately to accelerate technology adoption.",
            "C) Keep automation plans confidential until implementation week.",
            "D) Reduce customer support wages to balance automation investments."
        ],
        "correct": 0,
        "explanation": "Strategic HR manages technological disruption through workforce transition planning, reskilling, and empathetic change management.",
        "competency": "Consultation & Workforce Planning"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Job Analysis & Competency Modeling",
        "scenario": "Which process systematically gathers information about job duties, tasks, responsibilities, and required Knowledge, Skills, Abilities, and Other characteristics (KSAOs)?",
        "options": [
            "A) Job Analysis",
            "B) Job Evaluation",
            "C) Performance Appraisal",
            "D) Succession Planning"
        ],
        "correct": 0,
        "explanation": "Job Analysis provides the foundation for job descriptions, compensation structures, and legally defensible selection criteria.",
        "competency": "HR Expertise (People)"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Conflict Resolution & Negotiation",
        "scenario": "Two department directors are locked in a public dispute over resource allocation for key strategic projects, halting cross-team collaboration. How should the HR Business Partner intervene?",
        "options": [
            "A) Facilitate a interest-based negotiation session focused on shared organizational goals and mutual priorities.",
            "B) Side with the director whose department generates higher revenue.",
            "C) Escalate the dispute directly to the CEO without speaking to either director.",
            "D) Reallocate budget away from both departments as a penalty."
        ],
        "correct": 0,
        "explanation": "Interest-based negotiation focuses on underlying organizational needs rather than personal positions, restoring collaborative momentum.",
        "competency": "Relationship Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Safety Regulations",
        "scenario": "Under the Worker Adjustment and Retraining Notification (WARN) Act, covered employers must provide advance written notice of plant closings or mass layoffs of at least how many calendar days?",
        "options": [
            "A) 60 days",
            "B) 30 days",
            "C) 90 days",
            "D) 14 days"
        ],
        "correct": 0,
        "explanation": "The WARN Act requires qualifying employers (100+ employees) to give at least 60 days' written notice before mass layoffs or plant closings.",
        "competency": "Workplace Law Compliance"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Wage & Hour Regulations",
        "scenario": "Under the Fair Labor Standards Act (FLSA), how must overtime pay be calculated for non-exempt employees who work more than 40 hours in a single workweek?",
        "options": [
            "A) At a rate not less than one and one-half times the employee's regular rate of pay for all hours worked over 40.",
            "B) At double the regular rate of pay for any hours worked on weekends or holidays.",
            "C) At a flat bonus rate determined at the discretion of department management.",
            "D) Based on average bi-weekly hours, allowing hours to balance across two weeks."
        ],
        "correct": 0,
        "explanation": "FLSA requires overtime pay at 1.5 times the regular rate of pay for non-exempt workers for hours exceeding 40 in a standard 7-day workweek.",
        "competency": "HR Compliance & Total Rewards"
    },

    # --- 41 to 60 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Management & Succession Planning",
        "scenario": "An organization is creating a 9-Box Grid matrix for succession planning. Department leaders classify 80% of their staff as 'High Potential / High Performance' (Top Right Box). How should HR guide leaders to calibrate fairly?",
        "options": [
            "A) Facilitate executive calibration sessions using objective behavioral benchmarks and performance distribution guidelines.",
            "B) Accept all manager ratings without challenge to preserve positive manager relationships.",
            "C) Arbitrarily move 50% of employees into lower performance quadrants.",
            "D) Eliminate the 9-Box tool and use subjective tenure lists instead."
        ],
        "correct": 0,
        "explanation": "Succession calibration sessions prevent manager inflation and ensure consistent, objective evaluation standards across divisions.",
        "competency": "Critical Evaluation & Talent Strategy"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Employee Relations & Disciplinary Procedures",
        "scenario": "Which concept in progressive discipline ensures that employees are given clear notice of standards, an opportunity to correct behavior, and consistent enforcement?",
        "options": [
            "A) Due Process",
            "B) Constructive Discharge",
            "C) Employment-at-Will",
            "D) Summary Dismissal"
        ],
        "correct": 0,
        "explanation": "Due Process ensures fairness in disciplinary procedures, giving employees clear warnings, objective reviews, and time to remedy performance gaps.",
        "competency": "Workplace / Employee Relations"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Accommodation & Religious Expression",
        "scenario": "An employee requests schedule adjustments to observe religious Sabbath days. The shift manager objects, claiming it complicates weekly scheduling for other staff. What should HR do?",
        "options": [
            "A) Initiate the interactive accommodation process under Title VII to grant the request unless it creates genuine undue hardship.",
            "B) Deny the request immediately to avoid giving special scheduling privileges to one employee.",
            "C) Require the employee to secure their own voluntary shift swaps indefinitely without HR oversight.",
            "D) Instruct the employee to choose between their job schedule and religious practices."
        ],
        "correct": 0,
        "explanation": "Title VII mandates reasonable accommodation for sincerely held religious beliefs unless the employer proves undue hardship (a higher burden than administrative inconvenience).",
        "competency": "Ethical Practice & Diversity"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Management & Metrics",
        "scenario": "Which business framework measures organizational performance across four perspectives: Financial, Customer, Internal Business Processes, and Learning & Growth?",
        "options": [
            "A) Balanced Scorecard",
            "B) McKinsey 7S Model",
            "C) Six Sigma Framework",
            "D) Porter's Value Chain"
        ],
        "correct": 0,
        "explanation": "The Balanced Scorecard translates strategic goals into balanced performance metrics across operational, human capital, financial, and customer dimensions.",
        "competency": "Business Acumen & Strategic Alignment"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Organizational Restructuring & Layoffs",
        "scenario": "A company must execute a 15% reduction in force (RIF) due to financial hardship. How should HR ensure the selection process is legally defensible and non-discriminatory?",
        "options": [
            "A) Conduct an adverse impact analysis on proposed layoff lists and base selection on objective, documented business criteria.",
            "B) Allow department heads to select employees for termination based on subjective personal preferences.",
            "C) Target only senior, higher-salaried workers to achieve cost reduction targets faster.",
            "D) Use tenure as the sole criterion without evaluating critical skills needed for future operations."
        ],
        "correct": 0,
        "explanation": "Executing a RIF safely requires objective criteria, thorough adverse impact statistical testing, and alignment with future operational requirements.",
        "competency": "Risk Management & Employment Law"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Acquisition & Selection Testing",
        "scenario": "What type of validity measures how thoroughly a test or assessment samples the specific knowledge and skills required to perform a job?",
        "options": [
            "A) Content Validity",
            "B) Construct Validity",
            "C) Criterion Validity",
            "D) Concurrent Validity"
        ],
        "correct": 0,
        "explanation": "Content Validity confirms that test items directly represent the actual duties, skills, or knowledge required on the job.",
        "competency": "Talent Sourcing & Selection"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Compensation Strategy & Market Benchmarking",
        "scenario": "An organization's compensation philosophy aims to 'Lead the Market' (75th percentile). However, current salary survey audits show base pay has fallen to the 40th percentile. What should HR recommend?",
        "options": [
            "A) Present a phased compensation adjustment strategy to executive leadership to align pay scales with market positioning.",
            "B) Change the stated compensation philosophy on paper to reflect the lower 40th percentile market rate.",
            "C) Discontinue participating in external compensation surveys.",
            "D) Pay mandatory annual bonuses to executive staff only."
        ],
        "correct": 0,
        "explanation": "When actual pay lags behind market positioning strategy, HR must present a business case and phased budget plan to restore market competitiveness.",
        "competency": "Total Rewards Strategy"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Health & Safety Compliance",
        "scenario": "Which federal law governs employee benefit plans and sets minimum standards for health, pension, and welfare plans in private industry?",
        "options": [
            "A) Employee Retirement Income Security Act (ERISA)",
            "B) Consolidated Omnibus Budget Reconciliation Act (COBRA)",
            "C) Health Insurance Portability and Accountability Act (HIPAA)",
            "D) Age Discrimination in Employment Act (ADEA)"
        ],
        "correct": 0,
        "explanation": "ERISA establishes standards of conduct for plan fiduciaries and protects plan participants' health and retirement benefit rights.",
        "competency": "Total Rewards & Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Engagement & Survey Action",
        "scenario": "Annual engagement survey results show high satisfaction with pay but extremely low scores for direct supervisor communication. What is HR's best next step?",
        "options": [
            "A) Conduct focus groups to gather qualitative context and launch targeted supervisory communication coaching.",
            "B) Re-administer the engagement survey immediately until scores improve.",
            "C) Increase employee bonuses to boost overall satisfaction scores.",
            "D) Reprimand all line supervisors during executive staff meetings."
        ],
        "correct": 0,
        "explanation": "Survey data requires qualitative follow-up (focus groups) to understand root causes and targeted development interventions to drive real behavior change.",
        "competency": "Relationship Management & L&D"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Organizational Development & Learning",
        "scenario": "In adult learning theory (Andragogy), what is a fundamental characteristic of adult learners compared to traditional students?",
        "options": [
            "A) Adult learners are problem-centered, self-directed, and draw heavily on past life experiences.",
            "B) Adult learners prefer passive lecture formats over experiential learning.",
            "C) Adult learners are primarily motivated by external rewards rather than intrinsic goals.",
            "D) Adult learners learn best when topics lack immediate practical application."
        ],
        "correct": 0,
        "explanation": "Malcolm Knowles' theory of Andragogy highlights that adults need self-direction, practical relevance, and application to real-world problems.",
        "competency": "People / L&D"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Investigation & Conflicting Accounts",
        "scenario": "During an investigation into workplace bullying, the accused manager and the complaining employee offer completely contradictory accounts with no eyewitnesses. How should HR evaluate credibility?",
        "options": [
            "A) Assess witness credibility factors including plausibility, demeanor, motive to falsify, and corroborating indirect evidence.",
            "B) Automatically side with the manager due to organizational rank.",
            "C) Close the investigation immediately without making findings due to lack of direct eyewitnesses.",
            "D) Terminate both employees to eliminate team disruption."
        ],
        "correct": 0,
        "explanation": "EEOC guidelines direct investigators to weigh credibility factors (plausibility, motives, indirect patterns) when accounts directly conflict.",
        "competency": "Ethical Practice & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Employment Law",
        "scenario": "Which law protects military service members' reemployment rights upon returning from active duty and prohibits employment discrimination based on military service?",
        "options": [
            "A) Uniformed Services Employment and Reemployment Rights Act (USERRA)",
            "B) Vietnam Era Veterans' Readjustment Assistance Act (VEVRAA)",
            "C) Federal Employees' Compensation Act (FECA)",
            "D) National Defense Authorization Act (NDAA)"
        ],
        "correct": 0,
        "explanation": "USERRA protects civilian job rights and benefits for veterans and members of the Reserve and National Guard upon returning from military service.",
        "competency": "Workplace Law Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Diversity, Equity & Inclusion Strategy",
        "scenario": "A company wants to increase minority representation in senior leadership positions. What strategy is most sustainable and legally sound under SHRM best practices?",
        "options": [
            "A) Expand executive sourcing pipelines, create inclusive leadership development programs, and address unconscious bias in promotion criteria.",
            "B) Set rigid hiring quotas that reserve senior roles exclusively for specific demographic groups.",
            "C) Lower candidate qualification requirements for diversity candidates.",
            "D) Restrict non-minority employees from applying to internal leadership openings."
        ],
        "correct": 0,
        "explanation": "Sustainable DEI strategies focus on broadening sourcing pipelines, equitable development, and eliminating bias, rather than unlawful hiring quotas.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Sourcing & Analytics",
        "scenario": "Which metric evaluates the effectiveness of specific recruitment channels by calculating the proportion of candidates moving from one stage of the hiring funnel to the next?",
        "options": [
            "A) Yield Ratio",
            "B) Cost-Per-Hire",
            "C) Acceptance Rate",
            "D) Retention Index"
        ],
        "correct": 0,
        "explanation": "Yield Ratios measure candidate conversion efficiency across recruitment funnel stages (e.g., applicants to interviewed, interviewed to offered).",
        "competency": "Business Acumen & Sourcing"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Policy & Remote Work",
        "scenario": "Remote employees report feeling burnt out due to expectations of answering messages after standard working hours. How should HR intervene?",
        "options": [
            "A) Establish clear organizational 'Right to Disconnect' communication guidelines with leadership support and set realistic response expectations.",
            "B) Ignore the feedback since remote work offers inherent flexibility.",
            "C) Require all remote workers to return to the physical office immediately.",
            "D) Disable company email servers at 5:00 PM every day."
        ],
        "correct": 0,
        "explanation": "Mitigating remote burnout requires cultural norms and communication boundaries that protect employee wellness while maintaining flexibility.",
        "competency": "Consultation & Employee Well-being"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Global HR Administration",
        "scenario": "In global HR management, what term refers to the practice of customizing HR policies to fit the legal, cultural, and market norms of specific host countries?",
        "options": [
            "A) Localization Strategy",
            "B) Ethnocentric Staffing Strategy",
            "C) Standardized Enterprise Rollout",
            "D) Centralized Sourcing Framework"
        ],
        "correct": 0,
        "explanation": "Localization adapts practices to align with local laws, cultural nuances, and operational realities in host country environments.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "HR Analytics & Strategic Business Partnering",
        "scenario": "The Finance VP asks HR to cut 10% of the training budget to offset short-term revenue shortfalls. How should the HR Leader respond strategically?",
        "options": [
            "A) Present business impact data showing how targeted training directly drives revenue, productivity, and retention, while identifying low-impact areas for optimization.",
            "B) Refuse to make any cuts and cut off communication with Finance.",
            "C) Agree immediately to cut all leadership development programs without evaluating impact.",
            "D) Shift the entire training budget into general administrative overhead."
        ],
        "correct": 0,
        "explanation": "Strategic HR partners use financial acumen and ROI data to protect business-critical talent investments while partnering on efficiency.",
        "competency": "Business Acumen & Leadership"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Compensation Structure & Pay Ranges",
        "scenario": "In pay structure design, what is the term for the numerical difference between the minimum and maximum pay rates of a given salary grade, divided by the minimum rate?",
        "options": [
            "A) Range Spread",
            "B) Compa-Ratio",
            "C) Pay Grade Overlap",
            "D) Salary Midpoint Variance"
        ],
        "correct": 0,
        "explanation": "Range Spread measures the width of a pay range from minimum to maximum, expressed as a percentage of the minimum.",
        "competency": "Total Rewards Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Labor Relations & Contract Negotiations",
        "scenario": "During collective bargaining negotiations, union representatives demand a 10% wage increase, while management offers 1%. Negotiations reach a deadlock. What mechanism should HR recommend?",
        "options": [
            "A) Engage a neutral third-party mediator to facilitate dialogue and discover compromise solutions.",
            "B) Advise management to unilaterally impose the 1% offer immediately.",
            "C) File criminal charges against union negotiators.",
            "D) Replace all bargaining committee members with external managers."
        ],
        "correct": 0,
        "explanation": "Mediation brings a neutral third party to help deadlock parties re-engage constructively and negotiate voluntary agreements.",
        "competency": "Workplace / Labor Relations"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Employment Compliance & COBRA",
        "scenario": "Under the Consolidated Omnibus Budget Reconciliation Act (COBRA), what is the standard continuation coverage period for an employee who experiences a qualifying event such as voluntary or involuntary termination (other than gross misconduct)?",
        "options": [
            "A) 18 months",
            "B) 36 months",
            "C) 12 months",
            "D) 24 months"
        ],
        "correct": 0,
        "explanation": "COBRA grants qualified beneficiaries up to 18 months of continued group health insurance coverage following termination or reduction of hours.",
        "competency": "Total Rewards & Health Compliance"
    },

    # --- 61 to 80 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Organizational Culture & Value Alignment",
        "scenario": "A newly appointed CEO introduces a core value of 'Radical Innovation.' However, middle management continues punishing employees whose experimental projects fail. How should HR align performance systems with the new strategy?",
        "options": [
            "A) Redesign performance evaluations and reward systems to recognize calculated risk-taking, continuous learning, and innovation process milestones.",
            "B) Fire all middle managers who penalize failed projects.",
            "C) Advise the CEO to drop 'Radical Innovation' from corporate values.",
            "D) Issue disciplinary warnings to employees whose experimental projects fail."
        ],
        "correct": 0,
        "explanation": "Culture change requires aligning performance incentives, recognition systems, and psychological safety with organizational values.",
        "competency": "Leadership & Organizational Development"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Sourcing & Interviewing Techniques",
        "scenario": "Which structured interviewing format asks candidates to describe past experiences using the Situation, Task, Action, and Result (STAR) model?",
        "options": [
            "A) Behavioral Interviewing",
            "B) Stress Interviewing",
            "C) Hypothetical Scenario Interviewing",
            "D) Unstructured Exploratory Interviewing"
        ],
        "correct": 0,
        "explanation": "Behavioral interviewing operates on the premise that past behavior predicts future performance, utilizing the STAR technique.",
        "competency": "Talent Acquisition & Selection"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Health, Safety & Ergonomics",
        "scenario": "A manufacturing facility experiences an uptick in repetitive strain injuries among assembly workers. What is HR's best initial interdisciplinary action?",
        "options": [
            "A) Partner with safety officers to conduct ergonomic workplace assessments, redesign workstations, and introduce structured rotation schedules.",
            "B) Mandatory overtime to make up for lost production speed.",
            "C) Require injured workers to sign waivers before returning to their stations.",
            "D) Replace assembly workers with temporary contract labor immediately."
        ],
        "correct": 0,
        "explanation": "Ergonomic interventions, job rotation, and engineering controls directly address root causes of repetitive workplace injuries.",
        "competency": "Workplace Safety & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Anti-Discrimination Law",
        "scenario": "Under the Age Discrimination in Employment Act (ADEA), at what age do employees gain protection against employment discrimination?",
        "options": [
            "A) 40 years of age and older",
            "B) 50 years of age and older",
            "C) 62 years of age and older",
            "D) 35 years of age and older"
        ],
        "correct": 0,
        "explanation": "The ADEA explicitly protects workers who are 40 years of age or older from age-based employment discrimination.",
        "competency": "HR Compliance & Workplace Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Performance Appraisals & Managerial Bias",
        "scenario": "During annual evaluations, an HR audit reveals that a line manager rated every team member as 'Average' (3 out of 5) despite widely varying individual outputs. Which rating error has occurred?",
        "options": [
            "A) Central Tendency Error",
            "B) Halo / Horn Effect",
            "C) Leniency Error",
            "D) Recency Bias"
        ],
        "correct": 0,
        "explanation": "Central Tendency Error occurs when raters grade all employees near the midpoint of the scale to avoid making difficult performance distinctions.",
        "competency": "Critical Evaluation & Performance Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Workforce Sourcing",
        "scenario": "What term describes the strategic practice of moving specific business processes or operations to an external service provider in a nearby country?",
        "options": [
            "A) Nearshoring",
            "B) Offshoring",
            "C) Onshoring",
            "D) Co-sourcing"
        ],
        "correct": 0,
        "explanation": "Nearshoring transfers business processes to nearby countries, maintaining time zone proximity and cultural alignment while reducing costs.",
        "competency": "Global Effectiveness & Sourcing"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Conflict & Communication",
        "scenario": "An employee submits a formal complaint stating their supervisor sends non-urgent work emails past midnight and demands immediate responses. How should HR intervene?",
        "options": [
            "A) Establish clear team communication boundaries, counsel the supervisor on off-hours expectations, and reinforce work-life balance policies.",
            "B) Advise the employee to turn off their personal phone and ignore all supervisor communications indefinitely.",
            "C) Fire the supervisor immediately for creating a hostile work environment.",
            "D) Reclassify the employee as exempt under FLSA to eliminate working-hour boundaries."
        ],
        "correct": 0,
        "explanation": "Resolving off-hours communication friction requires setting explicit management guidelines and protecting non-exempt working hours.",
        "competency": "Relationship Management & Compliance"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Incentive Design",
        "scenario": "Which variable pay strategy rewards employees based on organizational cost savings or productivity improvements relative to a baseline standard?",
        "options": [
            "A) Gainsharing Plan",
            "B) Profit-Sharing Plan",
            "C) Discretionary Bonus Model",
            "D) Individual Commission Plan"
        ],
        "correct": 0,
        "explanation": "Gainsharing ties financial incentives directly to operational efficiency, cost reductions, or productivity improvements achieved by a team.",
        "competency": "Total Rewards & Incentives"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Change Management & Technology Adoption",
        "scenario": "A company launches a new AI-powered HR self-service portal, but frontline staff continue calling HR representatives for basic balance inquiries. How should HR drive self-service adoption?",
        "options": [
            "A) Conduct short user-friendly demonstrations, enlist peer technology champions, and simplify system login access.",
            "B) Block all incoming telephone calls to the HR service center.",
            "C) Issue formal warnings to employees who phone HR directly.",
            "D) Deactivate the AI self-service portal and return to manual processing."
        ],
        "correct": 0,
        "explanation": "Driving technology adoption requires reducing user friction, active enablement, and positive peer change advocates.",
        "competency": "Consultation & Enablement"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Employee Medical Privacy",
        "scenario": "Under the Health Insurance Portability and Accountability Act (HIPAA), how must employers store employee medical records relative to standard personnel files?",
        "options": [
            "A) Medical records must be kept completely separate from standard personnel files in secure, restricted-access storage.",
            "B) Integrated inside the main personnel file behind a red tab.",
            "C) Stored at an offsite law firm's archive location.",
            "D) Destroyed within 30 days of employee termination."
        ],
        "correct": 0,
        "explanation": "HIPAA and ADA require medical information to be maintained in confidential files separate from routine personnel records.",
        "competency": "Compliance & Privacy"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workforce Analytics & Attrition Planning",
        "scenario": "A financial services firm observes an increase in voluntary turnover among mid-career women leaders. What analytical step should HR take first?",
        "options": [
            "A) Conduct a segmented exit interview and stay interview audit to identify specific push and pull retention factors.",
            "B) Immediately offer a flat salary raise to all remaining female mid-level staff.",
            "C) Assume the turnover is purely due to external market pay rates.",
            "D) Replace departing managers with external recruits without analyzing cause."
        ],
        "correct": 0,
        "explanation": "Segmented analytics (exit/stay data) reveal specific root causes behind demographic attrition trends before costly interventions are deployed.",
        "competency": "Critical Evaluation & Analytics"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Immigration Law Compliance",
        "scenario": "Under Federal immigration law, within how many business days of an employee's first day of work for pay must Section 2 of Form I-9 be completed?",
        "options": [
            "A) Within 3 business days",
            "B) On the candidate's first hour of work",
            "C) Within 10 business days",
            "D) Within 30 calendar days"
        ],
        "correct": 0,
        "explanation": "Federal law mandates that employers inspect identity and employment authorization documents and complete Section 2 of Form I-9 within 3 business days of hire.",
        "competency": "Workplace Law Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Ethical Leadership & Whistleblower Protection",
        "scenario": "An employee reports to HR that their finance manager is falsifying quarterly revenue numbers. Two days later, the manager demotes the employee. What is HR's immediate requirement?",
        "options": [
            "A) Halt the demotion immediately, initiate a non-retaliation protection protocol, and conduct an independent investigation.",
            "B) Allow the demotion to stand until the finance investigation completes in 6 months.",
            "C) Inform the finance manager who submitted the anonymous report.",
            "D) Advise the employee to resign and seek employment elsewhere."
        ],
        "correct": 0,
        "explanation": "Whistleblower protections demand immediate intervention to prevent adverse retaliatory actions while claims are objectively investigated.",
        "competency": "Ethical Practice & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Organizational Learning & Knowledge Transfer",
        "scenario": "Which knowledge management practice pairs senior technical experts with junior staff to transfer implicit knowledge and institutional wisdom?",
        "options": [
            "A) Mentorship and Shadowing Programs",
            "B) Asynchronous LMS Modules",
            "C) Standard Operating Manual Reading",
            "D) Exit Survey Archiving"
        ],
        "correct": 0,
        "explanation": "Tacit knowledge (contextual wisdom) is best transferred through direct interpersonal mentoring, coaching, and job shadowing.",
        "competency": "People / Learning & Development"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Labor Relations & Workplace Grievance",
        "scenario": "A union shop steward files a step-1 grievance alleging that overtime distribution violates the collective bargaining agreement (CBA). How should HR respond at step 1?",
        "options": [
            "A) Review payroll logs against CBA provisions, meet with the supervisor, and issue a written factual determination within CBA timelines.",
            "B) Deny the grievance automatically without reviewing the CBA text.",
            "C) Refer the case directly to external federal arbitration.",
            "D) Cancel all scheduled overtime shifts for the department indefinitely."
        ],
        "correct": 0,
        "explanation": "Step-1 grievance handling requires strict adherence to CBA contractual guidelines, objective factual audit, and timely formal communication.",
        "competency": "Workplace / Labor Relations"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Compensation Benchmarking Metrics",
        "scenario": "Which metric compares an individual employee's salary to the midpoint of their assigned pay range?",
        "options": [
            "A) Compa-Ratio",
            "B) Range Spread",
            "C) Midpoint Progression Rate",
            "D) Market Parity Percentile"
        ],
        "correct": 0,
        "explanation": "Compa-Ratio = (Employee Salary / Pay Range Midpoint). A ratio of 1.0 indicates the employee is paid exactly at midpoint.",
        "competency": "Total Rewards Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Sourcing & Inclusive Sourcing",
        "scenario": "An engineering division's talent acquisition funnel shows a high candidate drop-off rate among diverse applicants at the technical coding screen stage. What should HR do?",
        "options": [
            "A) Review the coding assessment for cultural bias, validate job relevance, and train assessors on structured scoring rubrics.",
            "B) Remove coding screens entirely for all technical candidates.",
            "C) Discontinue tracking diversity metrics across the hiring funnel.",
            "D) Pass candidates through to final interviews regardless of test scores."
        ],
        "correct": 0,
        "explanation": "Auditing assessment tools ensures selection criteria are job-related, non-discriminatory, and measure true job competencies.",
        "competency": "Talent Strategy & Diversity"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Pay Legislation",
        "scenario": "Under the Equal Pay Act of 1963, wage differentials between men and women in the same establishment performing equal work are permitted under which exception?",
        "options": [
            "A) Seniority system, merit system, or factor other than sex (such as quantity or quality of production).",
            "B) Negotiated initial salary expectations at time of hire.",
            "C) Department budget limitations.",
            "D) Family marital status or head-of-household needs."
        ],
        "correct": 0,
        "explanation": "The Equal Pay Act permits pay variances based on seniority, merit, production quantity/quality, or factors other than sex.",
        "competency": "Compliance & Total Rewards"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Global HR & Cross-Border Compliance",
        "scenario": "A multinational firm expands into Europe and plans to implement U.S. employment-at-will contracts across European subsidiaries. How should global HR advise leadership?",
        "options": [
            "A) Advise that European labor laws strictly prohibit at-will employment and mandate statutory notice periods and severance frameworks.",
            "B) Proceed with U.S. at-will contracts since corporate headquarters is located in the U.S.",
            "C) Ask employees to waive local country labor law rights in writing.",
            "D) Classify all European workers as independent contractors to bypass local employment law."
        ],
        "correct": 0,
        "explanation": "Global HR must respect local host-country statutory labor protections, as local jurisdiction rules override home-country policies.",
        "competency": "Global & Cultural Effectiveness"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Retirement Regulations & ERISA",
        "scenario": "Under ERISA regulations, what is the term for an employee's non-forfeitable right to ownership of employer-contributed funds in a retirement plan over time?",
        "options": [
            "A) Vesting",
            "B) Portability",
            "C) Distribution",
            "D) Commutation"
        ],
        "correct": 0,
        "explanation": "Vesting refers to the legal right of an employee to retain employer-contributed benefits according to a set schedule.",
        "competency": "Total Rewards & Compliance"
    },

    # --- 81 to 100 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Strategic HR Leadership & Board Alignment",
        "scenario": "The Board of Directors requests an HR presentation on talent risks for an upcoming expansion. Instead of presenting traditional turnover percentages, what should HR highlight?",
        "options": [
            "A) Critical talent gap metrics, leadership bench depth, revenue impact of key vacancies, and strategic mitigation plans.",
            "B) Detailed employee attendance records from the past 12 months.",
            "C) Raw operational headcount charts without strategic context.",
            "D) Expense receipts for recent company social events."
        ],
        "correct": 0,
        "explanation": "Executive boards require business-aligned metrics showing how talent risks directly affect revenue, operational capability, and expansion readiness.",
        "competency": "Business Acumen & Leadership"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Workforce Analytics & Predictive Modeling",
        "scenario": "Which statistical technique uses historical employee data to forecast future workforce behaviors, such as identifying employees at high risk of voluntary turnover?",
        "options": [
            "A) Predictive Analytics",
            "B) Descriptive Analytics",
            "C) Benchmark Profiling",
            "D) Qualitative Exit Auditing"
        ],
        "correct": 0,
        "explanation": "Predictive analytics applies algorithms and historical patterns to forecast future talent outcomes and proactive intervention points.",
        "competency": "Critical Evaluation & Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Harassment & Retaliation",
        "scenario": "An employee who filed a harassment complaint receives a lower performance rating three weeks later from the accused manager. What action should HR take immediately?",
        "options": [
            "A) Freeze the performance appraisal, investigate potential retaliation, and conduct an independent review of the rating.",
            "B) Approve the appraisal since managers have absolute discretion over performance ratings.",
            "C) Instruct the employee to accept the rating to avoid further workplace conflict.",
            "D) Transfer the employee to a lower-paying shift."
        ],
        "correct": 0,
        "explanation": "HR must act quickly to stop potential retaliation against complainants and ensure performance evaluations remain impartial.",
        "competency": "Ethical Practice & Risk Mitigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Benefit Types",
        "scenario": "Which voluntary employee benefit allows workers to contribute pre-tax dollars to cover qualified medical expenses, operating under a strict annual 'use-it-or-lose-it' or limited rollover rule?",
        "options": [
            "A) Flexible Spending Account (FSA)",
            "B) Health Savings Account (HSA)",
            "C) Health Reimbursement Arrangement (HRA)",
            "D) Disability Insurance Indemnity"
        ],
        "correct": 0,
        "explanation": "Healthcare FSAs are employer-established pre-tax accounts governed by IRS rules, including annual contribution caps and 'use-it-or-lose-it' provisions.",
        "competency": "Total Rewards Administration"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Labor Relations & Workplace Safety",
        "scenario": "Employees refuse to work on a specialized machine, claiming standard safety guards were removed during repairs. How should HR and management respond under OSHA regulations?",
        "options": [
            "A) Halt operations on the machine immediately, inspect safety guards, address valid hazards, and ensure non-retaliation for safety concerns.",
            "B) Terminate the employees immediately for insubordination and refusal to work.",
            "C) Order non-technical office staff to operate the machine instead.",
            "D) Deduct safety inspection fees from the employees' paychecks."
        ],
        "correct": 0,
        "explanation": "OSHA protects workers' rights to refuse unsafe work when there is a reasonable belief of imminent danger or severe physical injury.",
        "competency": "Workplace Safety & Compliance"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Acquisition & Candidate Experience",
        "scenario": "What metric evaluates candidate perception of the hiring process by asking 'How likely are you to recommend our job application process to a colleague?'",
        "options": [
            "A) Candidate Net Promoter Score (cNPS)",
            "B) Quality-of-Hire Index",
            "C) Applicant Conversion Rate",
            "D) Offer Acceptance Ratio"
        ],
        "correct": 0,
        "explanation": "cNPS measures candidate satisfaction and brand reputation throughout the recruitment journey.",
        "competency": "Talent Sourcing & Branding"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Change Management & Corporate Restructuring",
        "scenario": "During an enterprise ERP software implementation, frontline supervisors skip training sessions and instruct staff to continue manual record-keeping. How should HR address this resistance?",
        "options": [
            "A) Engage supervisors in feedback sessions, demonstrate how the ERP solves their operational pain points, and align system usage with supervisor evaluations.",
            "B) Cancel the software rollout completely.",
            "C) Issue formal letters of reprimand without explaining the benefits of the technology.",
            "D) Pay supervisors extra cash bonuses for attending software training."
        ],
        "correct": 0,
        "explanation": "Effective change management overcomes user resistance by clarifying benefits (WIIFM - What's In It For Me) and establishing manager accountability.",
        "competency": "Consultation & Leadership"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Labor Relations & NLRA",
        "scenario": "What is the term for a clause in a collective bargaining agreement requiring union dues or equivalent service fees to be deducted directly from employees' wages?",
        "options": [
            "A) Dues Checkoff Clause",
            "B) Closed Shop Mandate",
            "C) Arbitral Settlement Right",
            "D) Merit Escalation Provision"
        ],
        "correct": 0,
        "explanation": "A dues checkoff clause authorizes employers to automatically deduct union dues from paycheck wages upon written employee consent.",
        "competency": "Workplace / Labor Relations"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Diversity, Equity & Inclusive Leadership",
        "scenario": "An employee who uses gender-neutral pronouns reports that team colleagues repeatedly and deliberately misgender them during group meetings. How should HR handle this situation?",
        "options": [
            "A) Meet with team leadership to enforce inclusive conduct guidelines, address intentional misgendering as a policy issue, and offer educational resources.",
            "B) Tell the complaining employee not to take workplace conversations personally.",
            "C) Move the complaining employee to an isolated solo assignment.",
            "D) Postpone all diversity discussions until the annual review cycle."
        ],
        "correct": 0,
        "explanation": "Respecting personal identity and enforcing workplace conduct guidelines fosters psychological safety and aligns with inclusive organizational practices.",
        "competency": "Ethical Practice & Diversity"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Military Leave & USERRA",
        "scenario": "Under USERRA guidelines, returning service members are entitled to reemployment in the job position they would have attained had they remained continuously employed. What is this concept called?",
        "options": [
            "A) Escalator Principle",
            "B) Step-Up Progression",
            "C) Retroactive Seniority Rule",
            "D) Continuous Tenure Guarantee"
        ],
        "correct": 0,
        "explanation": "The Escalator Principle ensures returning service members advance in pay, status, and seniority as if they had never left for military service.",
        "competency": "Workplace Law Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Performance Management & Underperformance",
        "scenario": "A tenured employee's work output drops significantly following personal life hardship. The supervisor wants to terminate the employee immediately. What should HR advise?",
        "options": [
            "A) Recommend supportive interventions (EAP resources, ADA/FMLA review if applicable) alongside a clear Performance Improvement Plan (PIP).",
            "B) Approve immediate termination without reviewing leave options or performance history.",
            "C) Demote the employee without prior notice or discussion.",
            "D) Reassign the employee's entire workload to peers permanently."
        ],
        "correct": 0,
        "explanation": "HR balances compassionate employee support (EAP, statutory leave options) with structured performance management frameworks.",
        "competency": "Relationship Management & Compliance"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Organizational Design & Span of Control",
        "scenario": "Which term describes the number of direct subordinates a single manager can supervise effectively?",
        "options": [
            "A) Span of Control",
            "B) Chain of Command",
            "C) Unity of Command",
            "D) Functional Breadth"
        ],
        "correct": 0,
        "explanation": "Span of Control defines the ratio of direct reports to a supervisor, influencing operational agility and organizational hierarchy.",
        "competency": "Structure & HR Service Delivery"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Global Mobility & Tax Equalization",
        "scenario": "An international assignee complains that their local tax burden in their host country significantly reduces their net take-home pay compared to home peers. How should HR structure compensation?",
        "options": [
            "A) Implement a Tax Equalization policy ensuring the employee pays no more or less tax than they would have in their home country.",
            "B) Instruct the employee to pay host country taxes out-of-pocket without assistance.",
            "C) End the international assignment immediately and recall the worker.",
            "D) Double the base salary to cover all estimated personal expenses."
        ],
        "correct": 0,
        "explanation": "Tax Equalization policy neutralizes tax differences for international assignees, ensuring compensation remains equitable during global transfers.",
        "competency": "Global Effectiveness & Total Rewards"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Opportunity & EEOC",
        "scenario": "Under EEOC regulations, how many calendar days does an employee generally have to file a charge of employment discrimination from the date of the alleged incident?",
        "options": [
            "A) 180 calendar days (extended to 300 days if state laws apply)",
            "B) 60 calendar days",
            "C) 365 calendar days in all jurisdictions",
            "D) 30 calendar days"
        ],
        "correct": 0,
        "explanation": "EEOC charges must generally be filed within 180 days, extended to 300 days if covered by a state or local anti-discrimination agency (FEPAs).",
        "competency": "Compliance & Workplace Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Compensation Benchmarking & Broadbanding",
        "scenario": "An organization is consolidating 15 narrow pay grades into 4 wide salary bands ('Broadbanding'). Managers express concern that this will eliminate clear progression steps. How should HR clarify?",
        "options": [
            "A) Explain how broadbanding provides greater pay flexibility, supports lateral skill development, and aligns pay with broader competencies.",
            "B) Abandon broadbanding and create 10 additional narrow grades.",
            "C) Tell managers that pay ranges will no longer be monitored.",
            "D) Require all employees to accept a flat salary freeze."
        ],
        "correct": 0,
        "explanation": "Broadbanding simplifies compensation structures, encouraging lateral career development, cross-functional agility, and flexible skill growth.",
        "competency": "Total Rewards Strategy"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic HR Frameworks",
        "scenario": "In Ulrich's HR Business Partner model, which role focuses primarily on aligning HR strategy with business goals and operational priorities?",
        "options": [
            "A) Strategic Partner",
            "B) Administrative Expert",
            "C) Employee Champion",
            "D) Change Agent"
        ],
        "correct": 0,
        "explanation": "Dave Ulrich's model identifies the Strategic Partner role as the key driver aligning HR initiatives directly with business objectives.",
        "competency": "Leadership & Business Acumen"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Wellness & Productivity",
        "scenario": "An organization notices rising health insurance premiums driven by chronic stress-related medical claims. How should HR address this systemic wellness risk?",
        "options": [
            "A) Launch a holistic wellness initiative including EAP support, stress management workshops, flexible work schedules, and preventive care incentives.",
            "B) Increase health insurance deductible costs for employees with stress claims.",
            "C) Cancel group health insurance coverage altogether.",
            "D) Ban employees from discussing stress at work."
        ],
        "correct": 0,
        "explanation": "Holistic employee wellness strategies mitigate chronic health risks, reduce long-term benefit costs, and improve workplace productivity.",
        "competency": "Total Rewards & Employee Health"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Job Analysis Data Collection",
        "scenario": "Which job analysis data collection method is best suited for high-volume, highly repetitive physical tasks where direct observation provides objective operational metrics?",
        "options": [
            "A) Direct Observation & Time-Motion Study",
            "B) Structured Open-Ended Interviews",
            "C) Narrative Self-Report Diaries",
            "D) External Panel Discussion"
        ],
        "correct": 0,
        "explanation": "Direct observation and time-motion studies effectively capture physical tasks, cycle times, and operational duties for repetitive roles.",
        "competency": "People / Job Design"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Ethics & Executive Coaching",
        "scenario": "A newly hired executive suggests using confidential client lists from their previous employer to gain a competitive sales edge. How should the HR Leader respond?",
        "options": [
            "A) Advise the executive against using former employer assets, highlighting legal non-disclosure boundaries, trade secret laws, and ethical standards.",
            "B) Encourage the executive to use the lists as long as no paper copies exist.",
            "C) Ignore the suggestion and hope sales leadership takes care of it.",
            "D) Report the executive to external media immediately."
        ],
        "correct": 0,
        "explanation": "HR safeguards corporate ethics and legal compliance by proactively preventing intellectual property violations and trade secret misuse.",
        "competency": "Ethical Practice & Consultation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Employment Compliance & Worker Classification",
        "scenario": "When applying the IRS 20-factor behavioral and financial control test, which factor strongly indicates that a worker is an employee rather than an independent contractor?",
        "options": [
            "A) The employer sets the specific work hours, provides tools/equipment, and controls how tasks are performed.",
            "B) The worker realizes a direct profit or loss based on business expense management.",
            "C) The worker advertises their services openly to the general public.",
            "D) The worker is paid a flat project fee upon completion of deliverables."
        ],
        "correct": 0,
        "explanation": "Behavioral and financial control over how, when, and where work is executed indicates an employer-employee relationship rather than contractor status.",
        "competency": "HR Compliance & Workforce Planning"
    },

    # --- 101 to 120 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Sourcing & AI Selection Bias",
        "scenario": "An organization deploys an automated AI resume-screening software to screen applicants. An internal audit reveals that qualified female engineering candidates are being systematically scored lower by the algorithm. What should HR do immediately?",
        "options": [
            "A) Suspend the AI tool immediately, conduct an algorithmic bias audit, and adjust training datasets to ensure adverse impact standards are met.",
            "B) Continue using the software but manually lower passing score thresholds for women candidates.",
            "C) Keep using the AI tool as-is since algorithms are assumed to be objective.",
            "D) Require candidates to remove gender markers from their resumes permanently."
        ],
        "correct": 0,
        "explanation": "HR must monitor technological tools for adverse impact and suspend biased algorithms to remain compliant with federal anti-discrimination guidelines.",
        "competency": "Critical Evaluation & Talent Sourcing"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Executive Compensation",
        "scenario": "Which long-term incentive (LTI) vehicle gives executive participants the right to purchase corporate stock at a set grant price within a specified future timeframe?",
        "options": [
            "A) Stock Options",
            "B) Restricted Stock Units (RSUs)",
            "C) Phantom Stock Units",
            "D) Profit-Sharing Grants"
        ],
        "correct": 0,
        "explanation": "Stock options grant executives the right to purchase company shares at a fixed strike price within a designated exercise window.",
        "competency": "Total Rewards & Strategy"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Health & Substance Abuse",
        "scenario": "A safety-sensitive heavy machinery operator exhibits slurred speech and unsteadiness on the job. How should HR instruct the supervisor under reasonable suspicion policies?",
        "options": [
            "A) Remove the employee from safety-sensitive duties immediately and coordinate confidential reasonable-suspicion drug/alcohol testing per policy.",
            "B) Send the employee back to work with a bottle of water.",
            "C) Instruct the supervisor to fire the employee on the spot without testing.",
            "D) Wait until the end of the 8-hour shift to evaluate the employee's behavior again."
        ],
        "correct": 0,
        "explanation": "Safety protocols require immediate removal from hazard-prone tasks and mandatory, objective testing following documented reasonable suspicion.",
        "competency": "Workplace Safety & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Leave Law & FMLA",
        "scenario": "An employee eligible for FMLA requests 6 weeks of leave to care for a spouse with a serious medical condition. Can the employer require the employee to submit a medical certification from a healthcare provider?",
        "options": [
            "A) Yes, the employer may require medical certification within 15 calendar days of the request.",
            "B) No, medical certifications are prohibited under federal privacy laws.",
            "C) Yes, but only if the employee has been with the company for longer than 5 years.",
            "D) No, written requests from the employee are automatically binding without medical proof."
        ],
        "correct": 0,
        "explanation": "FMLA permits employers to require medical certification supporting the need for leave, typically allowing employees 15 calendar days to provide documentation.",
        "competency": "Workplace Law Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Engagement & Remote Hybrid Management",
        "scenario": "Managers report that remote workers on hybrid teams are missing out on key informal project updates discussed during ad-hoc office conversations. What should HR recommend?",
        "options": [
            "A) Standardize asynchronous digital communication channels and require managers to document all operational decisions in accessible project hubs.",
            "B) Require all remote workers to work on-site 5 days a week.",
            "C) Ban in-person office discussions altogether.",
            "D) Separate remote and in-office staff into separate business divisions."
        ],
        "correct": 0,
        "explanation": "Effective hybrid workforce management requires intentional asynchronous communication structures to ensure equal information access across locations.",
        "competency": "Consultation & Structure"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Organizational Development & Culture",
        "scenario": "According to Edgar Schein's model of organizational culture, which layer includes visible structures, processes, dress codes, and observable behaviors?",
        "options": [
            "A) Artifacts",
            "B) Espoused Values",
            "C) Basic Underlying Assumptions",
            "D) Subconscious Norms"
        ],
        "correct": 0,
        "explanation": "Schein's cultural hierarchy categorizes physical environments, dress codes, and surface behaviors as visible 'Artifacts.'",
        "competency": "People / Organizational Design"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Accommodations & Pregnancy Rights",
        "scenario": "Under the Pregnant Workers Fairness Act (PWFA), a pregnant employee requests temporary exemption from heavy lifting duties. The supervisor demands medical proof of total disability before adjusting duties. What should HR clarify?",
        "options": [
            "A) Clarify that PWFA requires reasonable accommodations for known limitations related to pregnancy without requiring full disability status.",
            "B) Agree with the supervisor that full disability certification is required before making adjustments.",
            "C) Place the employee on forced unpaid leave until post-delivery.",
            "D) Reclassify the pregnant worker as a temporary contractor."
        ],
        "correct": 0,
        "explanation": "The PWFA requires employers to provide reasonable accommodations for pregnancy-related limitations unless doing so imposes an undue hardship.",
        "competency": "HR Compliance & Workplace Law"
    },
    {
        "type": "Knowledge Item",
        "chapter": "HR Metrics & Financial Literacy",
        "scenario": "Which financial metric measures total organizational revenue minus operating expenses, divided by total full-time equivalent (FTE) headcount?",
        "options": [
            "A) Revenue per FTE",
            "B) Profit Margin Variance",
            "C) Human Capital ROI",
            "D) Labor Cost Factor"
        ],
        "correct": 0,
        "explanation": "Revenue per FTE evaluates human capital productivity by calculating top-line revenue generated per full-time employee.",
        "competency": "Business Acumen & Analytics"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Onboarding & Time-to-Productivity",
        "scenario": "A financial firm notices new hires take 9 months on average to reach standard sales quotas compared to an industry benchmark of 4 months. How should HR intervene?",
        "options": [
            "A) Redesign the onboarding curriculum to incorporate phased practical simulations, peer coaching, and 30-60-90 day milestone checks.",
            "B) Fire sales hires who do not hit full quota within 30 days.",
            "C) Lower sales quotas across all regions to match the slower onboarding pace.",
            "D) Eliminate orientation sessions and assign recruits directly to cold-calling duties."
        ],
        "correct": 0,
        "explanation": "Accelerating time-to-productivity requires structured learning paths, practical application benchmarks, and active mentorship during early tenure.",
        "competency": "Talent Strategy & L&D"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Pay Transparency Legislation",
        "scenario": "Which recent statutory requirement in multiple U.S. states mandates that employers publish salary ranges in external job postings?",
        "options": [
            "A) Pay Transparency Laws",
            "B) Equal Opportunity Mandates",
            "C) ERISA Disclosure Provisions",
            "D) Fair Labor Standard Range Rules"
        ],
        "correct": 0,
        "explanation": "State and local pay transparency statutes mandate disclosing expected compensation ranges on public job postings to eliminate historic wage disparities.",
        "competency": "Total Rewards & Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Health, Safety & Mental Health",
        "scenario": "Employees in a high-volume call center report severe burnout and anxiety, leading to an increase in unscheduled short-term sick leave. What strategy should HR execute?",
        "options": [
            "A) Partner with leadership to review call quotas, introduce mental health support through EAPs, and provide stress-resilience training.",
            "B) Require employees to present doctor notes for single-day absences.",
            "C) Discipline employees who take short-term sick leave for mental health reasons.",
            "D) Replace phone representatives with offshore automated voice bots."
        ],
        "correct": 0,
        "explanation": "Addressing operational burnout requires evaluating workload factors, expanding access to supportive resources (EAP), and fostering wellness.",
        "competency": "Employee Engagement & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Global Mobility & Visas",
        "scenario": "Which U.S. non-immigrant visa category allows foreign national professionals with specialized knowledge in specialty occupations to work in the United States?",
        "options": [
            "A) H-1B Visa",
            "B) L-1 Visa",
            "C) J-1 Visa",
            "D) B-1 Visa"
        ],
        "correct": 0,
        "explanation": "The H-1B visa enables U.S. employers to employ foreign workers in specialty occupations requiring theoretical or technical expertise.",
        "competency": "Global Effectiveness & Sourcing"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Ethics & Nepotism Policies",
        "scenario": "A senior Director recommends hiring their daughter for an open manager position within their direct reporting hierarchy. How should HR navigate this conflict of interest?",
        "options": [
            "A) Enforce anti-nepotism policies by requiring candidates to go through independent screening and ensuring no direct reporting line exists.",
            "B) Approve the hire immediately to keep the Director happy.",
            "C) Disqualify the candidate automatically without evaluating their qualifications for non-reporting roles.",
            "D) Hide the family relationship from the rest of the executive team."
        ],
        "correct": 0,
        "explanation": "HR mitigates nepotism risks by preventing supervisory reporting lines between family members while maintaining fair consideration for non-conflicting roles.",
        "competency": "Ethical Practice"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Job Evaluation",
        "scenario": "In point-factor job evaluation systems, what term describes measurable job attributes such as skill, effort, responsibility, and working conditions?",
        "options": [
            "A) Compensable Factors",
            "B) Benchmark Criteria",
            "C) Job Ranking Dimensions",
            "D) Range Progression Variables"
        ],
        "correct": 0,
        "explanation": "Compensable factors are the specific attributes of a job that an organization values and is willing to pay for in a job evaluation model.",
        "competency": "Total Rewards Design"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Technology & Monitoring Privacy",
        "scenario": "An organization plans to install keystroke-logging software on remote workers' laptops. Employees express outrage over privacy intrusion. How should HR guide executive leadership?",
        "options": [
            "A) Recommend focusing metrics on task output rather than keystroke monitoring, while maintaining clear, transparent disclosure of any system monitoring policies.",
            "B) Install the logging software secretly without informing remote staff.",
            "C) Terminate any employee who voices concerns about electronic monitoring.",
            "D) Fire remote workers and replace them with on-site staff."
        ],
        "correct": 0,
        "explanation": "Trust and engagement decline under intrusive monitoring; HR advocates measuring objective performance outputs while ensuring policy transparency.",
        "competency": "Consultation & Ethical Practice"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Veterans Protection & Compliance",
        "scenario": "Which affirmative action program requirement applies to federal contractors under the Vietnam Era Veterans' Readjustment Assistance Act (VEVRAA)?",
        "options": [
            "A) Establishing annual hiring benchmarks for protected veterans.",
            "B) Offering mandatory military duty bonuses to all staff.",
            "C) Reserving 25% of all executive roles exclusively for military veterans.",
            "D) Reimbursing veterans for private health insurance costs."
        ],
        "correct": 0,
        "explanation": "VEVRAA requires covered federal contractors to take affirmative action to employ and advance qualified protected veterans, including establishing hiring benchmarks.",
        "competency": "Compliance & Workplace Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Strategic Workforce Planning & Skill Gaps",
        "scenario": "A 5-year business strategy requires transitioning from legacy IT systems to cloud technology. 60% of current IT staff lack cloud architecture skills. What strategy should HR execute?",
        "options": [
            "A) Design a blended build-buy-borrow talent plan: upskill existing IT staff, recruit cloud specialists, and utilize short-term consultants during transition.",
            "B) Terminate all legacy IT workers immediately.",
            "C) Postpone cloud transformation plans indefinitely.",
            "D) Force existing IT staff to learn cloud architecture without training resources."
        ],
        "correct": 0,
        "explanation": "A balanced workforce plan addresses skill transformation through internal development (build), targeted talent acquisition (buy), and contingent labor (borrow).",
        "competency": "Strategic Workforce Planning"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Employee Relations & Constructive Discharge",
        "scenario": "What legal concept occurs when an employer deliberately creates unbearable working conditions, forcing a reasonable employee to resign involuntarily?",
        "options": [
            "A) Constructive Discharge",
            "B) Summary Dismissal",
            "C) Reduction in Force",
            "D) Mutual Separation"
        ],
        "correct": 0,
        "explanation": "Constructive discharge occurs when forced resignation resulting from intolerable working conditions is treated legally as an involuntary termination.",
        "competency": "Workplace / Legal Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Labor Relations & Contract Administration",
        "scenario": "A supervisor reassigns weekend shift work without following the seniority-based posting protocol outlined in the collective bargaining agreement. How should HR resolve this?",
        "options": [
            "A) Direct the supervisor to adhere strictly to CBA seniority rules for shift postings and correct weekend assignments.",
            "B) Ignore the CBA rule if the supervisor prefers working with junior staff.",
            "C) Inform the union that company management is exempt from CBA guidelines.",
            "D) Discipline the senior workers for complaining about schedule rules."
        ],
        "correct": 0,
        "explanation": "CBA terms are legally binding agreements; HR ensures line management adheres strictly to contractual protocols to prevent grievances.",
        "competency": "Labor & Employee Relations"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Employment & Disability Law",
        "scenario": "Under the Americans with Disabilities Act (ADA), what is the threshold standard for an employer to legally deny a requested disability accommodation?",
        "options": [
            "A) Undue Hardship (demonstrating significant difficulty or expense relative to total operational resources).",
            "B) Departmental budget inconvenience.",
            "C) Minor preference objections from team co-workers.",
            "D) Any request exceeding $500 in total initial setup cost."
        ],
        "correct": 0,
        "explanation": "ADA mandates granting reasonable accommodations unless the employer proves that doing so imposes an 'Undue Hardship' involving significant difficulty or financial expenditure.",
        "competency": "HR Compliance & Workplace Law"
    },

    # --- 121 to 150 ---
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Ethics & Financial Integrity",
        "scenario": "An HR Manager discovers that a payroll administrator has been manually adjusting overtime hours for family members working in the warehouse. What is HR's mandatory first action?",
        "options": [
            "A) Suspend the administrator's payroll access immediately, conduct a complete payroll audit, and initiate formal disciplinary action.",
            "B) Issue an informal verbal reminder asking the administrator to stop the adjustments.",
            "C) Adjust warehouse hourly base pay rates to compensate for the discrepancies.",
            "D) Wait until the end of the fiscal year to audit the payroll discrepancy."
        ],
        "correct": 0,
        "explanation": "Financial fraud and ethics violations require immediate access revocation, thorough factual auditing, and firm corrective action to safeguard organizational integrity.",
        "competency": "Ethical Practice & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Wage Garnishment",
        "scenario": "Under the Consumer Credit Protection Act (CCPA), what limit is placed on the maximum percentage of an employee's disposable earnings that can be garnished for ordinary consumer debts?",
        "options": [
            "A) 25% of disposable earnings",
            "B) 50% of disposable earnings",
            "C) 10% of gross earnings",
            "D) 75% of net earnings"
        ],
        "correct": 0,
        "explanation": "CCPA caps wage garnishment for ordinary consumer debts at 25% of an employee's weekly disposable earnings (or the amount exceeding 30 times federal minimum wage).",
        "competency": "Total Rewards & Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Sourcing & On-Demand Labor",
        "scenario": "To handle seasonal demand spikes, an enterprise property decides to utilize contingent gig workers alongside full-time staff. How should HR ensure seamless team integration?",
        "options": [
            "A) Establish clear role boundaries, provide targeted safety/systems orientation, and ensure compliance with worker classification guidelines.",
            "B) Restrict contingent workers from accessing operational tools or training manuals.",
            "C) Require contingent workers to perform full-time administrative duties without contract adjustments.",
            "D) Treat contingent workers as permanent staff for benefit plan enrollments."
        ],
        "correct": 0,
        "explanation": "Integrating contingent talent requires balancing clear role scope and safety orientation while maintaining strict statutory classification boundaries.",
        "competency": "Talent Acquisition & Workforce Planning"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Workplace Safety & Inspections",
        "scenario": "During an unannounced OSHA facility inspection, what is the preliminary step conducted by the OSHA compliance officer prior to walking through the physical job site?",
        "options": [
            "A) Opening Conference",
            "B) Closing Conference",
            "C) Formal Citation Issuance",
            "D) Post-Inspection Hearing"
        ],
        "correct": 0,
        "explanation": "OSHA inspections begin with an Opening Conference where the compliance officer presents credentials, explains inspection scope, and reviews safety records.",
        "competency": "Workplace Safety & Compliance"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Organizational Restructuring & Culture Alignment",
        "scenario": "A technology company merges two regional customer service divisions. Staff from Region A complain that Region B's team receives preferential scheduling. How should HR intervene?",
        "options": [
            "A) Standardize scheduling policies enterprise-wide, involve representative staff from both regions in the process, and communicate transparent criteria.",
            "B) Allow each regional manager to run scheduling under different rules indefinitely.",
            "C) Reprimand Region A staff for voicing complaints.",
            "D) Eliminate flexible scheduling options for all customer service teams."
        ],
        "correct": 0,
        "explanation": "Post-merger alignment demands harmonizing policies transparently with cross-regional stakeholder participation to build trust and equity.",
        "competency": "Relationship Management & Leadership"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Learning & Development Measurement",
        "scenario": "In Donald Kirkpatrick's Training Evaluation Model, which level evaluates the actual business impact and ROI resulting from a training program?",
        "options": [
            "A) Level 4: Results",
            "B) Level 1: Reaction",
            "C) Level 2: Learning",
            "D) Level 3: Behavior"
        ],
        "correct": 0,
        "explanation": "Kirkpatrick's Level 4 measures organizational results—such as increased revenue, lower error rates, cost savings, or higher productivity.",
        "competency": "People / Learning & Development"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Harassment & Mandatory Reporting",
        "scenario": "An employee tells an HR Business Partner during a casual coffee conversation that a senior manager made inappropriate physical contact, but begs HR 'not to do anything about it.' What must HR do?",
        "options": [
            "A) Explain that HR has a legal obligation to investigate potential safety and harassment issues, ensuring confidentiality and protection from retaliation.",
            "B) Promise to keep the disclosure completely secret and take zero action.",
            "C) Immediately fire the senior manager without conducting an investigation.",
            "D) Tell the employee to resolve the issue directly with the manager in private."
        ],
        "correct": 0,
        "explanation": "HR cannot grant absolute confidentiality when workplace harassment is reported; HR must investigate to protect employee safety and limit organizational liability.",
        "competency": "Ethical Practice & Risk Mitigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Deferred Compensation",
        "scenario": "Which non-qualified deferred compensation plan allows key executives to defer a portion of their executive salary or bonus earnings outside standard qualified plan caps?",
        "options": [
            "A) 409A Non-Qualified Deferred Compensation (NQDC) Plan",
            "B) 401(k) Safe Harbor Plan",
            "C) Simplified Employee Pension (SEP-IRA)",
            "D) SIMPLE IRA Framework"
        ],
        "correct": 0,
        "explanation": "IRS Section 409A governs Non-Qualified Deferred Compensation plans, enabling high-earning executives to defer compensation beyond standard tax-qualified plan limits.",
        "competency": "Total Rewards & Legal Rules"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Strategic HR Alignment & Data Analytics",
        "scenario": "An executive team questions whether investing in a employee wellness platform provides measurable financial value. How should the CHRO prove business impact?",
        "options": [
            "A) Present a longitudinal correlation study linking wellness engagement with lower absenteeism, reduced health claims, and improved retention rates.",
            "B) Provide qualitative testimonials from two happy employees.",
            "C) Argue that employee health cannot be measured numerically.",
            "D) Suggest cutting all employee benefit programs if ROI cannot be calculated instantly."
        ],
        "correct": 0,
        "explanation": "Strategic HR demonstrates business value by linking program participation metrics directly to operational key performance indicators (turnover, absenteeism, claim costs).",
        "competency": "Business Acumen & Analytics"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Opportunity & Genetic Privacy",
        "scenario": "Which federal statute prohibits employers from discriminating against employees or job applicants based on genetic information or family medical history?",
        "options": [
            "A) Genetic Information Nondiscrimination Act (GINA)",
            "B) Health Insurance Portability and Accountability Act (HIPAA)",
            "C) Americans with Disabilities Act (ADA)",
            "D) Equal Pay Act (EPA)"
        ],
        "correct": 0,
        "explanation": "GINA protects individuals from employment discrimination based on genetic testing results or family medical history.",
        "competency": "Compliance & Workplace Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Talent Retention & High-Potential Engagement",
        "scenario": "A key high-potential software architect receives a competitive external job offer with a 20% salary increase. How should HR work with leadership to evaluate a retention response?",
        "options": [
            "A) Assess the architect's total organizational impact, evaluate pay equity, explore career expansion opportunities, and present a balanced counteroffer if strategic.",
            "B) Match the external salary immediately without reviewing internal pay equity.",
            "C) Threaten legal action against the competitor firm.",
            "D) Escort the software architect off company property immediately."
        ],
        "correct": 0,
        "explanation": "Retaining critical talent requires evaluating holistic business impact, internal equity standards, and career pathing alongside financial counter-proposals.",
        "competency": "Talent Strategy & Total Rewards"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Labor Relations & Picketing Rules",
        "scenario": "In labor relations, what type of picketing targets a neutral secondary employer to force them to cease doing business with a primary employer involved in a labor dispute?",
        "options": [
            "A) Secondary Boycott / Picketing (Prohibited under Taft-Hartley)",
            "B) Primary Recognitional Picketing",
            "C) Informational Public Demonstration",
            "D) Work-to-Rule Grievance Strike"
        ],
        "correct": 0,
        "explanation": "Secondary boycotts or picketing against neutral third parties are illegal under the Taft-Hartley Act (LMRA).",
        "competency": "Workplace / Labor Relations"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Executive Leadership & SHRM Exam Mastery",
        "scenario": "An HR Director is preparing the strategic workforce roadmap for an upcoming multi-state expansion. What final guiding principle ensures long-term strategic success?",
        "options": [
            "A) Aligning human capital strategies directly with business goals, embedding compliance, fostering inclusive leadership, and using data-driven decision making.",
            "B) Operating HR as an isolated administrative enforcement department.",
            "C) Focusing exclusively on short-term recruitment costs while ignoring retention.",
            "D) Eliminating manager accountability for employee engagement."
        ],
        "correct": 0,
        "explanation": "True SHRM strategy unifies human capital execution with business goals, robust analytics, ethical leadership, and inclusive organizational culture.",
        "competency": "Strategic Leadership & Consultation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Sourcing & Recruitment Funnel",
        "scenario": "Which HR sourcing metric tracks the total duration from the date a job requisition is formally approved until a selected candidate accepts the job offer?",
        "options": [
            "A) Time-to-Fill",
            "B) Time-to-Start",
            "C) Cost-Per-Hire",
            "D) Candidate Sourcing Speed"
        ],
        "correct": 0,
        "explanation": "Time-to-Fill measures the operational efficiency of recruitment workflows from requisition opening to offer acceptance.",
        "competency": "Talent Acquisition & Sourcing"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Performance Management & Calibration",
        "scenario": "A regional business head inflates all performance appraisal scores across their division to ensure their managers qualify for higher annual bonuses. How should HR intervene?",
        "options": [
            "A) Require cross-divisional performance calibration panels to standardize evaluation benchmarks against objective performance criteria.",
            "B) Approve the inflated scores to maintain positive executive relations.",
            "C) Arbitrarily cut 20% from all employee bonus payouts.",
            "D) Cancel all performance appraisals for the division."
        ],
        "correct": 0,
        "explanation": "Performance calibration sessions eliminate manager rating bias and ensure equitable evaluation across business units.",
        "competency": "Critical Evaluation & Consultation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Opportunity & Title VII Exemptions",
        "scenario": "Which legal defense allows religious organizations to give employment preference to individuals of a particular religion for roles performing religious activities?",
        "options": [
            "A) Religious Organization Exemption",
            "B) Public Policy Exception",
            "C) Statutory Business Necessity Rule",
            "D) Affirmative Duty Exemption"
        ],
        "correct": 0,
        "explanation": "Title VII includes specific exemptions allowing religious institutions to consider religion as a qualifying hiring factor for mission-aligned roles.",
        "competency": "Compliance & Workplace Law"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Strategic Workforce Planning & Contingency",
        "scenario": "An enterprise company anticipates losing 25% of its senior leadership team to retirement within 3 years. What proactive step should HR initiate immediately?",
        "options": [
            "A) Build a comprehensive Succession Planning strategy integrated with leadership development programs and 9-box grid mapping.",
            "B) Wait until retirements occur to launch external executive searches.",
            "C) Mandatory retirement delays for all senior staff.",
            "D) Reclassify senior roles as entry-level positions."
        ],
        "correct": 0,
        "explanation": "Proactive succession planning builds internal bench strength and ensures business continuity prior to anticipated executive departures.",
        "competency": "Strategic Workforce Planning"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Wage & Hour Classifications",
        "scenario": "To qualify for the FLSA Executive Exemption, an employee must meet the salary threshold and fulfill which primary duty requirement?",
        "options": [
            "A) Regularly direct the work of two or more full-time employees and have authority to hire or fire (or give significant weight to recommendations).",
            "B) Possess an advanced academic degree in engineering or business.",
            "C) Spend at least 80% of working hours on manual production.",
            "D) Manage external client account contracts valued above $100,000."
        ],
        "correct": 0,
        "explanation": "The FLSA executive exemption requires supervising at least two full-time employees and holding meaningful authority over employment decisions.",
        "competency": "HR Compliance & Total Rewards"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Safety & Hazard Reporting",
        "scenario": "An employee reports a blocked fire exit in the main warehouse. The warehouse manager tells the employee to ignore it because contractors are moving pallets. What should HR do?",
        "options": [
            "A) Direct facility safety officers to clear the emergency exit route immediately and enforce OSHA exit access protocols.",
            "B) Wait until contractor work finishes at the end of the week.",
            "C) Advise the employee to use alternative secondary exits without taking action.",
            "D) Reprimand the employee for raising non-urgent concerns."
        ],
        "correct": 0,
        "explanation": "OSHA safety standards demand unobstructed access to all emergency egress routes at all times to prevent workplace hazards.",
        "competency": "Workplace Safety & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Total Rewards & Benefit Architecture",
        "scenario": "Which health insurance model features a network of healthcare providers where participants select a Primary Care Physician (PCP) to manage referrals to specialists?",
        "options": [
            "A) Health Maintenance Organization (HMO)",
            "B) Preferred Provider Organization (PPO)",
            "C) High Deductible Health Plan (HDHP)",
            "D) Indemnity Health Plan"
        ],
        "correct": 0,
        "explanation": "HMO plans restrict coverage to care from doctors who work for or contract with the HMO, relying on PCPs to gatekeep specialist referrals.",
        "competency": "Total Rewards & Benefits"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Employee Relations & Union Avoidance Ethics",
        "scenario": "During an active union organizing drive, management asks HR if they can promise staff a new fitness center if they vote against the union. How should HR advise?",
        "options": [
            "A) Advise that promising new benefits during an organizing campaign violates the NLRA as an illegal inducement (Promises under TIPS).",
            "B) Approve the promise as standard competitive marketing.",
            "C) Require staff to sign individual non-union contracts before building the center.",
            "D) Build the fitness center in secret without announcing it."
        ],
        "correct": 0,
        "explanation": "Under the NLRA (TIPS rule), management cannot Promise benefits or Threaten penalties to influence employee voting during union campaigns.",
        "competency": "Workplace / Labor Relations"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Equal Employment & Retaliation Protections",
        "scenario": "Under EEOC guidelines, what constitutes an adverse employment action in a statutory retaliation claim?",
        "options": [
            "A) Any action that would dissuade a reasonable worker from making or supporting a charge of discrimination.",
            "B) Only formal written termination or salary reduction.",
            "C) Reassigning an employee to a different desk within the same office pod.",
            "D) Offering voluntary professional development opportunities."
        ],
        "correct": 0,
        "explanation": "The Supreme Court (Burlington Northern standard) defined adverse retaliatory action broadly as anything likely to deter a reasonable worker from exercising rights.",
        "competency": "Compliance & Legal Protection"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Organizational Development & Culture Transformation",
        "scenario": "Following an organizational culture audit, leadership wants to transition from a top-down hierarchy to a collaborative agile environment. What should HR execute first?",
        "options": [
            "A) Align leadership practices, update competency models, redesign performance systems, and engage employees in co-creating agile norms.",
            "B) Replace all corporate job titles overnight without explaining changes.",
            "C) Eliminate all manager roles immediately.",
            "D) Force employees to work in open plan seating without process changes."
        ],
        "correct": 0,
        "explanation": "Cultural evolution requires aligning leadership behaviors, structural processes, and performance incentives with shared organizational values.",
        "competency": "Leadership & Navigation"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Strategic Management & PESTLE Analysis",
        "scenario": "Which strategic environmental scan evaluates Political, Economic, Social, Technological, Legal, and Environmental factors impacting an enterprise?",
        "options": [
            "A) PESTLE Analysis",
            "B) SWOT Analysis",
            "C) Porter's Five Forces",
            "D) Balanced Scorecard Grid"
        ],
        "correct": 0,
        "explanation": "PESTLE analysis systematically examines external macro-environmental forces influencing organizational strategy and risk.",
        "competency": "Business Acumen & Strategy"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Workplace Ethics & Conflict of Interest",
        "scenario": "An HR Manager discovers that a senior software engineer runs a side consulting firm that offers competing services to the company's direct clients. How should HR handle this situation?",
        "options": [
            "A) Review the company's Conflict of Interest and Non-Compete policies with legal counsel, initiate a formal review, and address policy non-compliance.",
            "B) Ignore the side business if the engineer's daily work output remains high.",
            "C) Ask the engineer to pay a percentage of side earnings to the company.",
            "D) Terminate the engineer immediately without reviewing signed employment agreements."
        ],
        "correct": 0,
        "explanation": "Conflicts of interest undermine organizational fiduciary duty and intellectual property security; HR must enforce policy compliance through structured legal protocols.",
        "competency": "Ethical Practice & Risk Management"
    },
    {
        "type": "Knowledge Item",
        "chapter": "Talent Sourcing & Employer Branding",
        "scenario": "What term defines the unique set of benefits, culture, and career growth commitments an employer offers employees in exchange for their skills and performance?",
        "options": [
            "A) Employer Value Proposition (EVP)",
            "B) Total Compensation Package",
            "C) Strategic Brand Equity",
            "D) Corporate Culture Standard"
        ],
        "correct": 0,
        "explanation": "An Employer Value Proposition (EVP) articulates the total employment experience and rewards offered to attract and retain talent.",
        "competency": "Talent Sourcing & Branding"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "HR Analytics & Data Privacy",
        "scenario": "An HR analytics team wants to publish employee turnover data by department. In small departments (under 5 staff), publishing data might reveal personal identity details. How should HR protect privacy?",
        "options": [
            "A) Aggregate small department data into broader divisional categories to maintain anonymity and comply with data privacy standards.",
            "B) Publish individual names alongside turnover records.",
            "C) Exclude small departments from all corporate reporting.",
            "D) Require employees in small teams to waive privacy rights."
        ],
        "correct": 0,
        "explanation": "Data governance and ethical HR analytics require data aggregation to prevent identifying individuals in small reporting cohorts.",
        "competency": "Critical Evaluation & Privacy"
    },
    {
        "type": "Knowledge Item",
        "chapter": "U.S. Leave Compliance & COBRA Notices",
        "scenario": "Upon a qualified event triggering COBRA, within how many days must an employer notify the health plan administrator?",
        "options": [
            "A) Within 30 days",
            "B) Within 14 days",
            "C) Within 60 days",
            "D) Within 90 days"
        ],
        "correct": 0,
        "explanation": "Employers must notify their group health plan administrator of qualifying events (termination, reduction in hours) within 30 days.",
        "competency": "HR Compliance & Total Rewards"
    },
    {
        "type": "Situational Judgment Item (SJI)",
        "chapter": "Global Leadership & Cultural Competency",
        "scenario": "An HR professional is designing a global performance review system for offices in Asia, Europe, and the U.S. Regional directors report that direct negative feedback is culturally offensive in certain regions. How should HR design the tool?",
        "options": [
            "A) Adapt feedback delivery guidelines to incorporate localized cultural nuances while maintaining consistent core evaluation standards.",
            "B) Force all global offices to adopt strict U.S. direct feedback norms without alteration.",
            "C) Eliminate performance evaluations in regions that prefer indirect communication.",
            "D) Allow each regional office to create completely unrelated rating systems."
        ],
        "correct": 0,
        "explanation": "Global HR effectiveness requires balancing enterprise-wide strategic alignment with local cultural adaptation (localization).",
        "competency": "Global & Cultural Effectiveness"
    }
]

# Write out to questions.json with indenting
with open("questions.json", "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully generated questions.json with {len(questions)} items!")
