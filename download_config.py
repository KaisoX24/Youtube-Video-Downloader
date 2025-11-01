import streamlit as st
import yt_dlp
import os

def download_youtube_video(url,output_path='downloads'):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    final_filepath=None

    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s', 
        'noplaylist': True,
        'writedescription': False, 
        'noprogress': False,    
        'quiet': True,       
    }

    try:
        st.info(f"Currently given URL: {url}")
        with st.spinner('Downloading the video'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                final_filepath = ydl.prepare_filename(info_dict)
        st.success("Download complete on the server.")
        return final_filepath
    except yt_dlp.utils.DownloadError as de:
        st.error(de)
        return None
    except Exception as e:
        st.error(e)
        return None
    
