import streamlit as st

# About Me content
about_me = """
<div style='font-size:18px; line-height:1.6;'>
Hi, I’m <strong>Phillip Haberman</strong> — a data analyst with 4 years of experience turning messy data into meaningful insights.
I specialize in <strong>Python</strong>, <strong>SQL</strong>, and <strong>BI tools</strong>, with a strong track record in the <strong>hospitality and restaurant industry</strong>.<br><br>

Whether it’s uncovering trends, building dashboards, or improving operations, I love using data to solve real-world problems.
<hr style='margin: 1em 0'>

Outside of work, I enjoy reading, playing softball, and spending time with my wife and daughter.
We love being outdoors, discovering new foods, and exploring new places together.
<hr style='margin: 1em 0'>

This site is where I share projects, ideas, and experiments as I grow my skills and explore new challenges in analytics.
</div>
"""

st.title("About Me")
st.markdown(about_me, unsafe_allow_html=True)
