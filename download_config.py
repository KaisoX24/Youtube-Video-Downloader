import yt_dlp
import os
import streamlit as st
import ffmpeg

def download_youtube_video(url, file_type, output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    final_filepath = None

    # ---- base options ----
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'noplaylist': True,
        'writedescription': False,
        'verbose': True,
        'quiet': False,
        'noprogress': False,
    }

    # ---- pipeline switch ----
    if file_type == "mp4":
        ydl_opts.update({
            'format': 'bestvideo+bestaudio/best',
            'merge_output_format': 'mp4',
        })

    elif file_type == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        })

    try:
        st.info(f"Currently given URL: {url}")
        with st.spinner('Downloading...'):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)

                base_filename = ydl.prepare_filename(info_dict)

                if file_type == "mp3":
                    final_filepath = os.path.splitext(base_filename)[0] + ".mp3"
                else:
                    final_filepath = base_filename

        st.success("Download complete on the server.")
        return final_filepath

    except yt_dlp.utils.DownloadError as de:
        st.error(f"Download error: {str(de)}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

import ffmpeg
import os

def convert_mp4_to_mp3(input_file):
    """
    Convert a video (.mp4) to mp3 audio using ffmpeg-python.
    Returns the output mp3 path.
    Requires FFmpeg installed on the system.
    """

    if not os.path.exists(input_file):
        raise FileNotFoundError("Input file does not exist")

    base, _ = os.path.splitext(input_file)
    output_file = base + ".mp3"

    (
        ffmpeg
        .input(input_file)
        .output(output_file, acodec="mp3")
        .run()
    )

    return output_file
