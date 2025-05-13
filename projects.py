import streamlit as st

st.header("Projects")

# Row 1
row1_col1, row1_col2, row1_col3 = st.columns(3, gap="large")

with row1_col1:
    with st.container():
        st.subheader("Menu Engineering App with Streamlit")
        menu_engineering_url = "https://www.youtube.com/watch?v=wOUKxcne4tY"
        st.link_button(label='Click here to view the project', url=menu_engineering_url)

with row1_col2:
    with st.container():
        st.subheader("Deploying Metabase with Docker and Google BigQuery")
        deploy_mb_url = "https://medium.com/@pjhab2020/deploying-metabase-with-docker-and-setting-up-google-bigquery-connection-5c8e7dfa5840"
        st.link_button(label='Click here to view the project', url=deploy_mb_url)

with row1_col3:
    with st.container():
        st.subheader("Shareable Reports with Google Sheets and Docs")
        shareable_reports_url = "https://medium.com/@pjhab2020/how-to-build-a-simple-shareable-report-with-google-sheets-and-docs-9e8faab12898"
        st.link_button(label='Click here to view the project', url=shareable_reports_url)

# Row 2
row2_col1, row2_col2, row2_col3 = st.columns(3, gap="large")

with row2_col1:
    with st.container():
        st.subheader("Stay tuned...")

with row2_col2:
    with st.container():
        st.subheader("Stay tuned...")

with row2_col3:
    with st.container():
        st.subheader("Stay tuned...")
