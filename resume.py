import streamlit as st
from components.resume_blocks import render_job, render_education

tab0, tab1, tab2, tab3, tab4 = st.tabs(["Summary", "Professional Experience", "Education", "Skills", "Download"])

with tab0:
    st.header("Summary")

    st.markdown("""
                My career has followed an evolving path — from education and client management to data science
                — always centered around communication, systems thinking, and problem-solving.

                I began my professional journey in the U.S. after earning a BA in Spanish with a minor in Political Science
                from the University of North Georgia. Early roles as a Project Manager
                at Awana Global and later as an Account Manager at Mission Safe gave me firsthand experience managing clients,
                coordinating logistics, and driving program growth. I learned how to align teams,
                communicate across stakeholders, and deliver measurable results — including increased participation
                and revenue growth.

                Driven by a desire to work internationally, I moved to Shanghai,
                where I pursued a Master's in Applied Linguistics at Shanghai Jiao Tong University.
                There, I deepened my interest in research, statistics, and computational methods,
                publishing several papers and completing a thesis on language acquisition in young learners.
                As my exposure to data grew, so did my interest in using it beyond academia.

                In 2021, I formalized that interest by completing
                Le Wagon's data science bootcamp, where I gained hands-on training in Python, SQL, machine learning,
                and data engineering. This opened the door to a new chapter as a Data Analyst at Cages Hospitality Group,
                where I transform business data into insights that drive operations, marketing, and strategy.
                I've led initiatives that automated reporting, optimized inventory management,
                and helped cross-functional teams make data-informed decisions using dashboards and deep-dive analyses.

                Alongside that, I also taught part-time with Le Wagon, mentoring aspiring data professionals in Python,
                machine learning, and data visualization — reinforcing my strength in translating complex ideas into clear,
                actionable knowledge. Through each chapter — from education to data — I've stayed focused on building meaningful systems,
                empowering others with information, and using data to make better decisions.
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

    # Le Wagon
    render_education(
        degree="Certificate",
        major="Data Science",
        school="Le Wagon",
        gpa="",
        location="Shanghai, China",
        date_range="Jun 2021 - Aug 2021",
        bullets=["**Topics and Tools**: Git, SQL, Python, Pandas, Numpy, Scikit-learn, Tensorflow, Plotly, Streamlit, Google Cloud Platform.",
                 "**Modules:** Statistics, Linear Algebra, Machine Learning, Data Processing, Data Analysis, Data Visualization, NLP, Deep Learning, Data Engineering."]
                 )

    # Jiaotong
    render_education(
        degree="Masters of Arts",
        major="Applied Linguistsics",
        school="Shanghai Jiaotong University",
        gpa="**GPA:** 3.9",
        location="Shanghai, China",
        date_range="Sep 2018 - Mar 2021",
        bullets=["**Relevant Courses:** Statistics, Data Processing with R, Scientific Research Methods, Computational Linguistics",
                 "**Publications:** 3 conference papers, 2 journal publications",
                 "**Thesis:** The Fluctation Hypothesis in Chinese Young Learners"],
    )

    # UNG
    render_education(
        degree="Bachelor of Arts",
        major="Spanish",
        school="University of North Georgia",
        gpa="**GPA:** 3.4",
        location="Dahlonega, GA, USA",
        date_range="Aug 2007 - May 2013",
        bullets=["**Minor**: Political Science",
                 "**Relevant Courses:** Statistics, Economics, International Relations",
                 "**Clubs:** Spanish Language Honor Society, Rotaract Club Officer, Latin American Student Association Officer"],
    )

with tab3:
    st.header("Skills")

    # CSS for tag-style skills
    st.markdown("""
    <style>
    .skill-tag {
        display: inline-block;
        background-color: #eef2f7;
        border-radius: 16px;
        padding: 6px 14px;
        margin: 4px 6px 4px 0;
        font-size: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    # Grouped skill categories
    skills_data = {
        "Analytical & Technical": [
            "Python", "SQL", "Data Analysis", "Business Analysis",
            "Data Cleaning", "Data Visualization", "Dashboarding", "Git"
        ],
        "Tools & Platforms": [
            "Metabase", "Github", "Excel", "Jupyter Lab", "VSCode"],
        "Soft Skills & Language": [
            "Communication", "Teamwork", "Problem Solving", "Critical Thinking",
            "English (Native)", "Spanish (Fluent)", "Chinese (Intermediate)"
        ]
    }

    # Layout: 3 columns
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    # Render each skill group in a separate column
    for col, (category, skill_list) in zip(columns, skills_data.items()):
        with col:
            st.markdown(f"**{category}**")
            st.markdown(
                "".join([f"<span class='skill-tag'>{skill}</span>" for skill in skill_list]),
                unsafe_allow_html=True
            )
with tab4:
    st.header("Download Resume")

    with open("assets/resume_phillip_haberman.pdf", "rb") as f:
        pdf_bytes = f.read()
        st.download_button(
            label="Download PDF",
            data=pdf_bytes,
            file_name="resume_phillip_haberman.pdf",
            mime="application/pdf",
            help="Click to download my resume in PDF format."
        )
