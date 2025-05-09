import streamlit as st

def render_job(title, company, location, date_range, bullets, skills):
    st.markdown(f"""

                **{title} @ {company}, {location}**

                *{date_range}*

                """)

    for bullet in bullets:
        st.markdown(f"- {bullet}")

    st.markdown(f"**Key Skills:** {', '.join(skills)}")
    st.markdown("---")
