import streamlit as st

st.title('Projects')

st.divider()

with st.container(border=False):
    row1_col1, row1_col2, row1_col3 = st.columns(3)

    with row1_col1:
        st.subheader("Menu Engineering")
        st.image("assets/menu_eng.jpg", use_container_width=True)
        st.caption("A Streamlit app that helps restaurant managers categorize and visualize menu item performance using sales and cost data. Includes built-in filters and an embedded YouTube demo walkthrough.")
        st.markdown("#python  #menuengineering #restaurantyanalytics")
        st.link_button(label="See Project", url="https://www.youtube.com/watch?v=wOUKxcne4tY", type="primary")

    with row1_col2:
        st.subheader("Deploying Metabase with Docker")
        st.image("assets/docker.jpg", use_container_width=True)
        st.caption("A technical walkthrough of deploying Metabase using Docker and connecting it to a Google BigQuery database. Includes setup, authentication, and dashboard creation.")
        st.markdown("#metabase #docker #bigquery")
        st.link_button(label="See Project", url="https://medium.com/@pjhab2020/deploying-metabase-with-docker-and-setting-up-google-bigquery-connection-5c8e7dfa5840", type="primary")

    with row1_col3:
        st.subheader("Reporting with Google Sheets")
        st.image("assets/reports.jpg", use_container_width=True)
        st.caption("A project focused on building dynamic, professional reports using Google Sheets for data and Google Docs for polished presentation.")
        st.markdown("#google-sheets #google-docs #reporting")
        st.link_button(label="See Project", url="https://medium.com/@pjhab2020/how-to-build-a-simple-shareable-report-with-google-sheets-and-docs-9e8faab12898", type="primary")

st.divider()

with st.container(border=False):
    row1_col1, row1_col2, row1_col3 = st.columns(3)

    with row1_col1:
        st.subheader("Market Basket Analysis")
        st.image("assets/market_basket.jpg", use_container_width=True)
        st.caption("A project using association rule mining (Apriori algorithm) to uncover product combinations frequently purchased together. Helps businesses optimize promotions and cross-selling strategies.")
        st.markdown("#marketbasketanalysis #apriori #dataanalysis")
        st.link_button(label="See Project", url="https://github.com/phaberman/Market-Basket-Analysis-Project", type="primary")

    with row1_col2:
        st.subheader("Metabase Sales Dashboard (Coming Soon)")
        st.image("assets/dashboard.jpg", use_container_width=True)
        st.caption("An interactive dashboard built in Metabase that visualizes sales performance across categories, locations, and time periods. Designed to surface trends and support operational decision-making.")
        st.markdown("#metabase #salesdashboard #sql")
        st.link_button(label="See Project", url="", type="primary")

    with row1_col3:
        st.subheader("Varaince Root-Cause Analysis (Coming Soon)")
        st.image("assets/inventory.jpg", use_container_width=True)
        st.caption("A diagnostic dashboard built in Metabase to explore mismatches between recorded and actual inventory. Helps identify stock control issues and reduce waste using filters and variance analysis.")
        st.markdown("#metabase #inventory-management #sql")
        st.link_button(label="See Project", url="", type="primary")
