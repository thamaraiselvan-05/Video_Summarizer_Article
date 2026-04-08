# 🎬 Video Insight Article Generator

An AI-powered web application that converts YouTube videos into structured articles and downloadable PDFs using transcript extraction and Generative AI.

---

## 🚀 Live Demo

🔗 https://video-summarizer-article.streamlit.app/

---

## 📌 Overview

This project extracts transcripts from YouTube videos and transforms them into well-structured, readable articles. It also allows users to download both the generated article and the transcript as professional PDF documents.

The application is designed to save time by converting long-form video content into concise, actionable insights.

---

## ✨ Features

* 🎥 Extract transcript from YouTube videos
* 🧠 Generate structured articles using AI
* 📄 Download article as PDF
* 📜 Download transcript as PDF
* 📺 Display video title and transcript preview
* 🎨 Clean and modern UI with soft blue theme
* 🔄 Persistent interface using session state (no reset on download)
* ⚠️ Error handling for unavailable transcripts

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI Model:** Groq (LLaMA-based models)
* **Transcript Extraction:** yt-dlp
* **PDF Generation:** FPDF
* **Styling:** Custom CSS + Google Fonts

---

## 🧠 How It Works

1. User enters a YouTube URL
2. Transcript is extracted using yt-dlp
3. AI processes transcript and generates structured article
4. Article and transcript are converted into PDFs
5. User can preview and download both outputs

---

## 📂 Project Structure

```
video_summarizer_article/
│
├── app.py                  # Main Streamlit app
├── transcript.py           # Extracts transcript using yt-dlp
├── article_generator.py    # Generates article using Groq API
├── pdf_generator.py        # Creates PDF files
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Installation & Setup

###  Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

###  Install Dependencies

```bash
pip install -r requirements.txt
```

---

###  Set API Key

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

---

###  Run the App

```bash
streamlit run app.py
```

---

## 🔒 Environment Variables

| Variable     | Description         |
| ------------ | ------------------- |
| GROQ_API_KEY | API key for Groq AI |

---

## ⚠️ Limitations

* Some videos may not provide transcripts due to:

  * Disabled captions
  * YouTube restrictions
  * Region limitations
* Performance depends on transcript availability

---

## 💡 Future Improvements

* 🎥 YouTube thumbnail preview
* 📊 Tabs UI (Transcript | Article | PDF)
* 🌍 Multi-language support
* 📈 Keyword extraction & insights
* 🎨 Advanced PDF styling (report format)

---
