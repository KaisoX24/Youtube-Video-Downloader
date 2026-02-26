import streamlit as st
from download import download_youtube_video,convert_mp4_to_mp3,meta_info
import os
import zipfile
import io

def download_one_file(batch_file,mime_type):
    if st.session_state.single_file_buffer is None:
        with open(batch_file,'rb')as f:
            st.session_state.single_file_buffer=f.read()
            st.session_state.single_file_name=os.path.basename(batch_file)
    st.download_button(
        label=":green[Download File]",
        data=st.session_state.single_file_buffer,
        file_name=st.session_state.single_file_name,
        mime=mime_type,
        
    )

def create_zip_buffer(batch_files):
    zip_buffer = io.BytesIO()

    with zipfile.ZipFile(zip_buffer, "w", zipfile.ZIP_DEFLATED) as zipf:
        for fpath in batch_files:
            if os.path.exists(fpath):
                with open(fpath, "rb") as f:
                    zipf.writestr(os.path.basename(fpath), f.read())

    zip_buffer.seek(0)
    return zip_buffer

st.title(":green[📹 Download BETA V]")
col1,col2=st.columns(2)
choice = st.sidebar.selectbox("Options:", ['Youtube Files', 'Video Files'])

# ---- session state init ----
if "vid_thumb" not in st.session_state:
    st.session_state.vid_thumb=None

if 'vid_title' not in st.session_state:
    st.session_state.vid_title=None

if "downloaded_file_path" not in st.session_state:
    st.session_state.downloaded_file_path = None

if "single_file_buffer" not in st.session_state:
    st.session_state.single_file_buffer = None

if 'single_file_name' not in st.session_state:
    st.session_state.single_file_name = None

if "mime_type" not in st.session_state:
    st.session_state.mime_type = None

if "batch_files" not in st.session_state:
    st.session_state.batch_files = []

if "zip_buffer" not in st.session_state:
    st.session_state.zip_buffer = None


if choice == 'Youtube Files':
    video_url = st.sidebar.text_area("Enter the YouTube video URL (one per line):","")
    url_jobs=[perurl.strip() for perurl in video_url.split('\n') if perurl.strip()]
    vid_res=None
    aud_quality=None
    
    output_format = None

    if url_jobs:
        output_format = st.sidebar.radio("Mp4 or Mp3?", ['mp4', 'mp3'])
        if output_format=='mp4':
            vid_res=st.sidebar.selectbox("Select Resolution:",['Best','480P','720P','1080P'])
        else:
            aud_quality=st.sidebar.selectbox("Audio Quality:",['128k','192k','256k','320k'])

    button = None
    if url_jobs and output_format:
        if output_format == 'mp4':
            st.session_state.mime_type = "video/mp4"
        else:
            st.session_state.mime_type = "audio/mpeg"

        button = st.sidebar.button("Start Download",type='primary')

        if button:
            st.session_state.single_file_buffer = None
            st.session_state.single_file_name = None
            st.session_state.batch_files = []
            st.session_state.zip_buffer=None

            for url in url_jobs:
                try:
                    with col1:
                        meta_data=meta_info(url)
                        st.session_state.vid_thumb=meta_data.get('thumbnail')
                        st.session_state.vid_title=meta_data.get('title')
                        st.image(st.session_state.vid_thumb,caption=st.session_state.vid_title,width=300)
                    with col2:
                        path = download_youtube_video(
                            url=url,
                            selected_res=vid_res or 'Best',
                            audio_quality=aud_quality or '192k',
                            file_type=output_format
                        )
                        st.write('---')
                        if path:
                            st.session_state.batch_files.append(path)
                except Exception as e:
                    st.warning(f"Failed for {e}")


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
        download_one_file(st.session_state.downloaded_file_path,st.session_state.mime_type)

# ---- render download ----
if len(st.session_state.batch_files)==1:
    download_one_file(st.session_state.batch_files[0],st.session_state.mime_type)
    os.remove(st.session_state.batch_files[0])
    st.session_state.batch_files = []
    
elif len(st.session_state.batch_files)>1:
    if st.session_state.zip_buffer is None:
        st.session_state.zip_buffer = create_zip_buffer(st.session_state.batch_files)

        for fpath in st.session_state.batch_files:
            if os.path.exists(fpath):
                os.remove(fpath)

        st.session_state.batch_files = []
        
    st.download_button(
        label="📦 Download All as ZIP",
        data=st.session_state.zip_buffer,
        file_name="downloads.zip",
        mime="application/zip"
    )
