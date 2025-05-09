import streamlit as st
from components.resume_blocks import render_job

tab0, tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Professional Experience", "Education", "Skills", "Languages"])

with tab0:
    st.header("Summary")

    st.markdown("""

                My career began in **education** and **project management**, where I led teams, built training programs, and managed key client relationships. Over time, I was drawn to the power of **data** to drive decisions and solve real-world problems, which led me to transition into analytics.

                Since **2021**, I’ve worked as a **Data Analyst** at *Cages Hospitality Group* in Shanghai, where I help streamline operations and boost profitability through **data-driven insights**. I build automated reports, dashboards, and conduct deep-dive analyses using **SQL**, **Python**, and **BI tools** — all to support faster, smarter decisions across departments.

                In parallel, I taught part-time with *Le Wagon*, mentoring students in **data science** and **machine learning**. That teaching experience strengthened my ability to **communicate complex ideas clearly** — a skill I carry into every analysis and recommendation I make today.
                """)

with tab1:
    st.header("Professional Experience")

    # Cages Hospitality Group
    render_job(
        title="Data Analyst",
        company="Cages Hospitality Group",
        location="Shanghai, China",
        date_range="Sep 2021 - Present",
        bullets=[
            "Delivered actionable insights on inventory, sales, marketing, and customer behavior, helping reduce operational costs and boost profitability.",
            "Automated reports using SQL, Python, and BI tools to track  and improve team efficiency.",
            "Built dashboards to support marketing, HR, finance, and operations enabling faster, data-informed decisions.",
            "Conducted deep-dive analyses on sales, inventory, and customer trends to improve operational efficiency and profitability.",
            "Presented insights and recommendations directly to leadership for cross-functional initiatives and strategic improvements."
        ],
        skills=["SQL", "Python", "Data Cleaning", "Business Intelligence", "Data Visualization"]
    )

    # Le Wagon
    render_job(
        title="Data Science Instructor (Part-Time)",
        company="Le Wagon",
        location="Remote",
        date_range="Oct 2021 - Jan 2023",
        bullets=[
            "Taught courses on SQL, Python, Data Analysis, and Machine Learning.",
            "Guided students in creating capstone projects including chatbots and recommendation systems.",
             "Achieved 5.0/5.0 NPS score.",
        ],
        skills=["SQL", "Python", "Communication", "Machine Learning", "Teaching"]
    )

    # Web English
    render_job(
        title="Head ESL Teacher",
        company="Web International Englsih",
        location="Shanghai, China",
        date_range="Apr 2016 - Mar 2018",
        bullets=["Led a high-performing teaching team with strong retention and a 4.9/5.0 student satisfaction rating.",
                 "Contributed to curriculum development and teacher training.",
                 "Conducted teacher training sessions and workshops to improve teaching quality."
                 ],
        skills=["Teaching", "Leadership", "Curriculum Development", "Training", "Cross-Cultural Communication"]
    )

    # Mission Safe
    render_job(
        title="Account Manager",
        company="Mission Safe",
        location="Atlanta, GA",
        date_range="Apr 2015 - Apr 2016",
        bullets=["Implemented CRM tools to improve client engagement and sales tracking.",
                 "Boosted customer satisfaction and contributed to a 7% quarterly revenue increase.",
                 "Managed a portfolio of 50+ key clients, ensuring high levels of customer satisfaction and retention."],
        skills=["CRM", "Sales", "Customer Engagement", "Client Management", "Revenue Growth"]
    )

    # Awana
    render_job(
        title="Project Manager",
        company="Awana Global",
        location="Atlanta, GA",
        date_range="May 2013 - Apr 2015",
        bullets=["Developed regional partnerships, increasing training program participation by 50%."
                 "Managed logistics and stakeholder communication for regional programs.",
                 "Help raise over $100,000 in funding for training programs through communication with key financial donors.",
                 "Supported in the creation and implementation of a new training program for 200+ teachers in the region."
                 ],
        skills=["Project Management", "Stakeholder Communication", "Fundraising", "Training Program Development", "Logistics Management"]
    )

with tab2:
    st.header("Education")
with tab3:
    st.header("Skills")
with tab4:
    st.header("Languages")
