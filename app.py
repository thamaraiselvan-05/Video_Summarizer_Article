import streamlit as st
from transcript import get_transcript
from summarizer import summarize_text
from article_generator import generate_article
from pdf_generator import create_pdf

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Video Summarizer", layout="centered")

st.markdown("""
<style>
/* Background */
body {
    background: linear-gradient(135deg, #e3f2fd, #f5faff);
}

/* Main container */
.main {
    background-color: #ffffffcc;
    padding: 30px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}

/* Title */
.title {
    font-size: 34px;
    font-weight: 700;
    color: #0d47a1;
    text-align: center;
}

/* Subtitle */
.subtitle {
    text-align: center;
    color: #555;
    margin-bottom: 25px;
}

/* Input box */
.stTextInput>div>div>input {
    border-radius: 10px;
    border: 1px solid #90caf9;
    padding: 10px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #42a5f5, #1e88e5);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(90deg, #1e88e5, #1565c0);
}

/* Card */
.card {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 3px 15px rgba(0,0,0,0.08);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- TITLE ----------
st.markdown('<div class="title">📊 Video Insight Generator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Transform YouTube Videos into Professional Articles & Reports</div>', unsafe_allow_html=True)

url = st.text_input("🔗 Paste your YouTube video link here")

if st.button(" Generate Smart Article"):
    if url:
        with st.spinner("Analyzing video and generating insights..."):
            text = get_transcript(url)
            summary = summarize_text(text)
            article = generate_article(summary)
            create_pdf(article)

        st.success("✅ Article Generated Successfully!")

       
        st.markdown('<div class="card">', unsafe_allow_html=True)

        st.subheader("📄 Generated Article")
        st.text_area("", article, height=400)

        with open("output.pdf", "rb") as f:
            st.download_button("📥 Download PDF", f, file_name="AI_Article.pdf")

        st.markdown('</div>', unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter a valid YouTube URL")