import streamlit as st
from download import download_youtube_video
import os

st.title("📹 Streamlit Video Downloader")

choice = st.sidebar.selectbox("Options:", ['Youtube Files', 'Video Files'])

# ---- session state init ----
if "downloaded_file_path" not in st.session_state:
    st.session_state.downloaded_file_path = None
if "mime_type" not in st.session_state:
    st.session_state.mime_type = None

if choice == 'Youtube Files':
    video_url = st.sidebar.text_input("Enter the YouTube video URL:", "")

    output_format = None
    if video_url:
        output_format = st.sidebar.radio("Mp4 or Mp3?", ['mp4', 'mp3'])

    button = st.sidebar.button("Start Download")

    if video_url and output_format and button:
        if output_format == 'mp4':
            st.session_state.mime_type = "video/mp4"
        else:
            st.session_state.mime_type = "audio/mpeg"

        st.session_state.downloaded_file_path = download_youtube_video(
            video_url, output_format
        )

# ---- render download ----
if (
    st.session_state.downloaded_file_path
    and os.path.exists(st.session_state.downloaded_file_path)
):
    with open(st.session_state.downloaded_file_path, "rb") as f:
        data = f.read()

    file_name = os.path.basename(st.session_state.downloaded_file_path)

    # deterministic cleanup
    os.remove(st.session_state.downloaded_file_path)
    st.session_state.downloaded_file_path = None

    st.download_button(
        label="💾 Click to Download",
        data=data,
        file_name=file_name,
        mime=st.session_state.mime_type
    )
