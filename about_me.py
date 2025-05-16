import streamlit as st

# About Me content
about_me = """
<div style='font-size:18px; line-height:1.5;'>
Hi, I’m <strong>Phillip Haberman</strong> — a data analyst with experience turning messy data into meaningful insights.
I specialize in <strong>Python</strong>, <strong>SQL</strong>, and <strong>BI tools</strong>,
with a strong track record in the <strong>hospitality and restaurant industry</strong>.

Whether it’s uncovering trends, building dashboards, or improving operations, I love using data to solve real-world problems.

Outside of work, I enjoy reading, playing softball, and spending time with my wife and daughter.
We love being outdoors, discovering new foods, and exploring new places together.

This site is where I share projects, ideas, and experiments as I grow my skills and explore new challenges in analytics.
</div>
"""

st.title("About Me")

st.divider

st.markdown(about_me, unsafe_allow_html=True)
