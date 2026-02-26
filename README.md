# 📹 Streamlit Media Downloader (Download BETA V)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.30%2B-red)
![yt-dlp](https://img.shields.io/badge/yt--dlp-Latest-green)
![FFmpeg](https://img.shields.io/badge/FFmpeg-Required-orange)

A powerful, web-based media tool built with **Streamlit** and **yt-dlp**. This application allows users to download high-quality videos and audio from YouTube, process batch downloads, and convert local video files to MP3 format.

## 🚀 Features

### 1. YouTube Downloader
* **Video Support:** Download videos in **MP4** format with selectable resolutions (`1080p`, `720p`, `480p`, `Best Available`).
* **Audio Support:** Extract audio in **MP3** format with selectable bitrates (`320k`, `256k`, `192k`, `128k`).
* **Batch Processing:** Enter multiple URLs (one per line) to download multiple files at once.
* **Smart Zipping:** Automatically bundles multiple downloads into a single `.zip` file for easy downloading.
* **Metadata Display:** Shows video thumbnails and titles before downloading.
* **Real-time Progress:** Displays download speed, ETA, and file size during the process.

### 2. Video Converter
* **Local File Support:** Upload video files (`.mp4`, `.mkv`) directly from your computer.
* **Audio Extraction:** Converts uploaded videos to high-quality MP3 audio using FFmpeg.

---

## 🛠️ Prerequisites

To run this application, you must have **Python** installed. Additionally, **FFmpeg** is required for audio conversion and merging video streams.

### Installing FFmpeg (System Level)
* **Windows:** [Download FFmpeg](https://ffmpeg.org/download.html), extract it, and add the `bin` folder to your System PATH variables.
* **Mac:** `brew install ffmpeg`
* **Linux (Ubuntu/Debian):** `sudo apt update && sudo apt install ffmpeg`

---

## 📦 Installation

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/yourusername/your-repo-name.git](https://github.com/yourusername/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment (Optional but Recommended)**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # Mac/Linux
    source venv/bin/activate
    ```

3.  **Install Python dependencies**
    Create a `requirements.txt` file (or use the command below) with the following libraries:
    ```bash
    pip install streamlit yt-dlp ffmpeg-python
    ```

---

## ▶️ Usage

1.  Run the Streamlit application:
    ```bash
    streamlit run main.py
    ```

2.  The app will open in your default web browser (usually at `http://localhost:8501`).

3.  **For YouTube:**
    * Select "Youtube Files" from the sidebar.
    * Paste URLs (one per line).
    * Choose MP4 or MP3 and select your quality settings.
    * Click "Start Download".

4.  **For Local Conversion:**
    * Select "Video Files" from the sidebar.
    * Upload your video file.
    * Wait for the conversion to finish and click the download button.

---

## 📂 Project Structure

```text
├── main.py              # Main application entry point (UI logic)
├── download.py          # Core logic for yt-dlp and ffmpeg operations
├── downloads/           # Directory where downloaded files are stored
├── uploads/             # Temporary directory for uploaded files
└── README.md            # Project documentation

> **Note:**  
> You must have **FFmpeg** installed on your system for `yt-dlp` to work properly.  
> - Windows users can download from: https://ffmpeg.org/download.html  
> - After installation, make sure it’s added to your system PATH.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the link displayed in the terminal (usually `http://localhost:8501`) in your browser.

---

## 🧑‍💻 Author

**Pramit Acharjya**  
✨ Passionate about AI, automation, and building practical tools.  

📺 YouTube: [Kaiso Gaming & Tech](https://www.youtube.com/@KaisoGaming_AT)  
💻 GitHub: [@KaisoX24](https://github.com/KaisoX24)

---

## ⭐ Support

If you find this project useful, please **⭐ star this repo** to support future development!
