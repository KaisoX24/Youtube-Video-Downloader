import yt_dlp
import os
import streamlit as st
import ffmpeg
import time

def meta_info(url):
    meta_opts={
        'skip_download':True,
        'quiet':True,
    }
    with yt_dlp.YoutubeDL(meta_opts) as mydl:
        info_dict = mydl.extract_info(url, download=False)
        return info_dict     
    

def progress_hook(d, progress_bar, status_text, state):
    now = time.time()

    if now - state["last_update"] < 0.2:
        return  

    state["last_update"] = now

    if d["status"] == "downloading":
        downloaded = d.get("downloaded_bytes", 0)
        total = d.get("total_bytes") or d.get("total_bytes_estimate")

        if total:
            percent = downloaded / total
            progress_bar.progress(min(percent, 1.0))
            percent_text = f"{percent*100:.1f}%"
        else:
            percent_text = "Calculating..."

        speed = d.get("speed") or 0
        eta = d.get("eta")

        status_text.text(
            f"{percent_text} | "
            f"{downloaded/1e6:.1f} MB | "
            f"{speed/1e6:.1f} MB/s | "
            f"ETA: {eta if eta else 'N/A'}"
        )

def download_youtube_video(url,selected_res='Best',audio_quality='192k', file_type='mp4', output_path="downloads"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    final_filepath = None

    Format_maps={
        'Best':'bestvideo+bestaudio/best',
        '480P':'bestvideo[height<=480]+bestaudio/best',
        '720P':'bestvideo[height<=720]+bestaudio/best',
        '1080P':'bestvideo[height<=1080]+bestaudio/best'
    }
    Aud_maps={
        '128k':'128',
        '192k':'192',
        '256k':'256',
        '320k':'320'
    }

    # ---- base options ----
    ydl_opts = {
        'outtmpl': f'{output_path}/%(title).200s_%(id)s.%(ext)s',
        'restrictfilenames': True,
        'noplaylist': True,
        'verbose': True,
    }
    

    
    # ---- pipeline switch ----
    if file_type == "mp4":
        ydl_opts.update({
            'format': Format_maps[selected_res],
            'merge_output_format': 'mp4',
        })

    elif file_type == "mp3":
        ydl_opts.update({
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': Aud_maps[audio_quality],
            }],
        })

    try:
        with st.spinner("Downloading..."):
            

            st.info(f"Currently given URL: {url}")
            progress_bar = st.progress(0)
            status_text = st.empty()
            state = {"last_update": 0}
            ydl_opts["progress_hooks"] = [
            lambda d: progress_hook(d, progress_bar, status_text,state)
                        ]
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(url, download=True)
                base_filename = ydl.prepare_filename(info_dict)
                if file_type == "mp3":
                    final_filepath = os.path.splitext(base_filename)[0] + ".mp3"
                else:
                    final_filepath = base_filename
            st.toast("Download is Complete On the server",icon='✅',duration='short')
            return final_filepath

    except yt_dlp.utils.DownloadError as de:
        st.error(f"Download error: {str(de)}")
        return None
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None

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
