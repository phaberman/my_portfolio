import streamlit as st
import base64

st.title("Social Links")

st.divider()

# Load and encode image
def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Paths and links
icon_paths = {
    "GitHub": "assets/github.png",
    "LinkedIn": "assets/linkedin.png",
    "Medium": "assets/medium.png"
}

social_links = {
    "GitHub": "https://github.com/phaberman",
    "LinkedIn": "https://www.linkedin.com/in/phillip-haberman/",
    "Medium": "https://medium.com/@pjhab2020"
}

# Create evenly spaced columns
cols = st.columns(len(social_links))

# Loop through and display icons
for i, (name, link) in enumerate(social_links.items()):
    with cols[i]:
        img_base64 = get_image_base64(icon_paths[name])
        st.markdown(
            f"""
            <div style="text-align: center;">
                <a href="{link}" target="_blank">
                    <img src="data:image/png;base64,{img_base64}" width="48" />
                    <div style="font-size: 14px; margin-top: 4px;">{name}</div>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )
