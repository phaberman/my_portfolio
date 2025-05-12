import streamlit as st

st.header("Projects")

# Menu Engineering App
# st.markdown("---")

# st.subheader("Menu Engineering App (built with Streamlit)")
# menu_engineering_URL = "https://www.youtube.com/watch?v=wOUKxcne4tY"
# st.video(menu_engineering_URL)

# st.markdown("---")

# Row 1
row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    with st.container():
        st.subheader("Menu Engineering App")
        st.video("https://www.youtube.com/watch?v=wOUKxcne4tY")
        st.caption("A Streamlit app for menu engineering, built with Python.")

with row1_col2:
    with st.container():
        st.subheader("Stay tuned...")

with row1_col3:
    with st.container():
        st.subheader("Stay tuned...")

# Row 2
row2_col1, row2_col2, row2_col3 = st.columns(3)
with row2_col1:
    with st.container():
        st.subheader("Stay tuned...")
with row2_col2:
    with st.container():
        st.subheader("Stay tuned...")
with row2_col3:
    with st.container():
        st.subheader("Stay tuned...")
