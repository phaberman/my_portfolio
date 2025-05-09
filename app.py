import streamlit as st

# Pages
about_me_page = st.Page("about_me.py", title="About Me")
resume_page = st.Page("resume.py", title="Resume")
project_page = st.Page("projects.py", title="Projects")
blog_page = st.Page("blog.py", title="Blog")
contact_page = st.Page("contact.py", title="Contact Me")

# Navigation
pg = st.navigation([about_me_page, resume_page, project_page, blog_page, contact_page])
pg.run()
