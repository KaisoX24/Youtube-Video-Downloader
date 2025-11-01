# 📼 YouTube Video Downloader

A simple **Streamlit web app** that allows users to download YouTube videos directly by just pasting the video URL.  
Built using **Python**, **Streamlit**, and **yt-dlp** for fast and reliable downloads.

---

## 🚀 Features

- 🎯 Download YouTube videos in the **best available quality**  
- ⚡ Uses `yt-dlp` for **high performance and reliability**  
- 🧩 Simple and modern **Streamlit interface**  
- 📁 Automatically removes temporary files after download  
- 🖥️ Works locally — **no external API keys required**

---

## 🧠 How It Works

1. Enter a valid **YouTube video URL** in the sidebar.  
2. Click **Start Download**.  
3. Wait until the video is processed.  
4. Click the **Download button** to save it to your device.

---

## 🛠️ Installation

### 1. Clone the repository
```bash
git clone https://github.com/KaisoX24/Youtube-Video-Downloader.git
cd Youtube-Video-Downloader
```

### 2. Create a virtual environment (optional but recommended)
```bash
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Linux/Mac
```

### 3. Install the dependencies
```bash
pip install -r requirements.txt
```

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

## 📂 Project Structure

```
📁 youtube-video-downloader
 ┣ 📜 app.py
 ┣ 📜 download_config.py
 ┣ 📜 requirements.txt
 ┣ 📁 downloads/
 ┗ 📜 README.md
```

---

## 📦 Requirements

- Python 3.8 or higher  
- Streamlit  
- yt-dlp  
- FFmpeg (system dependency)

### Example `requirements.txt`
```
streamlit
yt-dlp
```

---

## ⚠️ Disclaimer

> This project is intended **for educational purposes only**.  
> Please ensure you comply with YouTube’s Terms of Service.  
> Do **not** use this tool to download copyrighted content without permission.

---

## 🧑‍💻 Author

**Pramit Acharjya**  
✨ Passionate about AI, automation, and building practical tools.  

📺 YouTube: [Kaiso Gaming & Tech](https://www.youtube.com/@kaisogamingandtech)  
💻 GitHub: [@KaisoX24](https://github.com/KaisoX24)

---

## ⭐ Support

If you find this project useful, please **⭐ star this repo** to support future development!
