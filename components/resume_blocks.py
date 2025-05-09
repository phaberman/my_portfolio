import streamlit as st

# Professional Experience
def render_job(title, company, location, date_range, bullets, skills):
    st.markdown(f"""

                **{title} @ {company}**

                **{location}**

                *{date_range}*

                """)

    for bullet in bullets:
        st.markdown(f"- {bullet}")

    st.markdown(f"**Key Skills:** {', '.join(skills)}")
    st.markdown("---")

# Education
def render_education(degree, major, school, location, date_range, gpa, bullets):
    st.markdown(f"""

                **{degree} in {major} @ {school}**

                **{location}**

                {gpa}

                *{date_range}*

                """)

    for bullet in bullets:
        st.markdown(f"- {bullet}")

    st.markdown("---")
