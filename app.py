import streamlit as st
from download_config import download_youtube_video,convert_mp4_to_mp3
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
elif choice == 'Video Files':
    uploaded_file = st.sidebar.file_uploader("Upload Your video file:",type=['mp4', 'mkv'])
    st.session_state.mime_type = "audio/mpeg"

    if uploaded_file is not None:
        temp_input_path = os.path.join(
            "uploads",
            uploaded_file.name
        )
        os.makedirs("uploads", exist_ok=True)
        with open(temp_input_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        # ---- convert ----
        st.session_state.downloaded_file_path = convert_mp4_to_mp3(
            temp_input_path
        )
        os.remove(temp_input_path)

# ---- render download ----
if (
    st.session_state.downloaded_file_path
    and os.path.exists(st.session_state.downloaded_file_path)
):
    with open(st.session_state.downloaded_file_path, "rb") as f:
        data = f.read()

    file_name = os.path.basename(st.session_state.downloaded_file_path)

    os.remove(st.session_state.downloaded_file_path)
    st.session_state.downloaded_file_path = None

    st.download_button(
        label="💾 Click to Download",
        data=data,
        file_name=file_name,
        mime=st.session_state.mime_type
    )

