import streamlit as st

st.set_page_config(layout='centered')

# Pages
about_me_page = st.Page("about_me.py", title="About Me")
resume_page = st.Page("resume.py", title="Resume")
project_page = st.Page("projects.py", title="Projects")
blog_page = st.Page("blog.py", title="Blog")
social_page = st.Page("social.py", title="Social")

# Navigation
pg = st.navigation([about_me_page, resume_page, project_page, blog_page, social_page])
pg.run()
