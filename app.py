import streamlit as st

st.set_page_config(page_title="Worker Participation Guide", layout="wide")

st.title("Step-by-step guide for Worker Participation")

steps = [
    ("Step 1: Identify the Model for Worker Involvement", """
There are several models of involvement:
1) Designer representing workers
2) Designer consulting workers
3) Workers participating in the design process
4) Workers as designers

Choose based on project goals, culture, and readiness.
"""),
    ("Step 2: Determine the Approach for Collecting Data and Insights", """
Choose among:
1) Empirical
2) Experimental
3) Scenario-based

Can be combined depending on depth and complexity.
"""),
    ("Step 3: Decide on the Mode of Worker Participation", """
1) Direct participation
2) Indirect participation

Choice depends on scale, feasibility, and structures.
"""),
    ("Step 4: Choose the Specific Method for Worker Participation", """
Options include:
1) Co-design
2) Value co-creation
3) Resonant co-creation
4) Lead user innovation
5) Living labs
6) Explainable AI (XAI)

Select based on goals and context.
"""),
    ("Step 5: Consider Contextual Factors", """
Consider:
- National labor laws
- Organizational policies
- Management approach
- Past research and evaluations
"""),
    ("Step 6: Employee Education and Training", """
Provide training in:
- Communication
- Decision-making
- Problem-solving
- Design thinking
"""),
    ("Step 7: Mentoring and Peer Learning", """
Establish:
- Mentorship programs
- Peer-learning exchanges

Encourages sustained engagement and innovation.
"""),
    ("Step 8: Feedback and Communication Channels", """
Establish formal feedback channels:
- Suggestion systems
- Digital platforms
- Regular meetings

Ensure closed-loop communication.
"""),
    ("Step 9: Codetermination and Work Councils", """
Integrate with formal structures:
- Codetermination
- Work councils

Enhances legitimacy and effectiveness.
""")
]

for title, content in steps:
    with st.expander(title):
        st.markdown(content)
        
with st.expander("Descriptive summary of each method in Step 4"):
    st.markdown("### Co-Design")
    st.image("assets/Codesign.png", caption="Co-Design", width=378)

    st.markdown("### Value Co-Creation")
    st.image("assets/Value_Co_Creation.png", caption="Value Co-Creation", width=378)

    st.markdown("### Resonant Co-Creation")
    st.image("assets/Resonant_Co_Creation.png", caption="Resonant Co-Creation", width=378)

    st.markdown("### Lead User Innovation")
    st.image("assets/Lead_User_Innovation.png", caption="Lead User Innovation", width=378)

    st.markdown("### Living Labs")
    st.image("assets/Living_Lab.png", caption="Living Lab", width=378)

with st.expander("Use Case: Designing a Scheduling System"):
    st.markdown("### Step 1: Identify the Model for Worker Involvement")
    st.write("Recocomended model: Workers participating in the design process or workers as designers (for high trust and autonomy 
    environments")

    st.markdown("### Step 2: Determine the Approach for Collecting Data and Insights")
    st.write("Combine empirical (interviews), scenario-based (mock-ups), and experimental (pilot testing) methods.")

    st.markdown("### Step 3: Decide on the Mode of Worker Participation")
    st.write("Prefer direct participation via workshops or co-design sessions; use indirect participation where needed.")

    st.markdown("### Step 4: Choose the Specific Method for Worker Participation")
    st.write("Apply co-design, value co-creation, and lead user innovation approaches.")

    st.markdown("### Step 5: Consider Contextual Factors")
    st.write("Respect labor laws, union rules, organizational culture, and technology constraints.")

    st.markdown("### Step 6: Employee Education and Training")
    st.write("Train workers in scheduling principles and design thinking.")

    st.markdown("### Step 7: Mentoring and Peer Learning")
    st.write("Encourage mentoring and peer review of early prototypes.")

    st.markdown("### Step 8: Feedback and Communication Channels")
    st.write("Use digital forms, feedback loops, and discussion sessions.")

    st.markdown("### Step 9: Codetermination and Work Councils")
    st.write("Integrate worker-designed components with formal participation bodies.")


    st.markdown("### Explainable AI (XAI)")
    st.image("assets/Explainable_AI.png", caption="Explainable AI", width=378)


