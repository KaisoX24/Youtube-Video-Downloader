import streamlit as st
from download import download_youtube_video
import os

st.title("📹 Streamlit Video Downloader")

video_url = st.sidebar.text_input("Enter the YouTube video URL:", "")
button = st.sidebar.button("Start Download")

# Session state to persist file
if "downloaded_file_path" not in st.session_state:
    st.session_state.downloaded_file_path = None

if video_url and button:
    st.session_state.downloaded_file_path = download_youtube_video(video_url)

# Only show download button if file exists
if st.session_state.downloaded_file_path and os.path.exists(st.session_state.downloaded_file_path):
    with open(st.session_state.downloaded_file_path, "rb") as f:
        video_bytes = f.read()

    file_name = os.path.basename(st.session_state.downloaded_file_path)

    if st.download_button(
        label="💾 Click to Download Video",
        data=video_bytes,
        file_name=file_name,
        mime="video/mp4"
    ):
        # ✅ delete AFTER user downloads
        os.remove(st.session_state.downloaded_file_path)
        st.session_state.downloaded_file_path = None
        st.success("✅ Download completed and file cleaned up.")

