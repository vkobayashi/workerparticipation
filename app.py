import streamlit as st

st.set_page_config(page_title="Worker Participation Guide", layout="wide")

st.title("Guidebook for Worker Participation")

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
### Co-Design
![Co-Design](./assets/Codesign.png)
st.image("assets/Codesign.png", caption="Co-Design")

### Value Co-Creation
![Value Co-Creation](assets/Value_Co_Creation.png)

### Resonant Co-Creation
![Resonant Co-Creation](assets/Resonant_Co_Creation.png)

### Lead User Innovation
![Lead User Innovation](assets/Lead_User_Innovation.png)

### Living Labs
![Living Lab](assets/Living_Lab.png)

### Explainable AI (XAI)
![Explainable AI](assets/Explainable_AI.png)

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
