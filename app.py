import streamlit as st
from transcript import get_transcript
from article_generator import generate_article
from pdf_generator import create_pdf
import os

def clean_filename(title):
    return "".join(c for c in title if c.isalnum() or c in " _-").strip()

if "generated" not in st.session_state:
    st.session_state.generated = False

st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #f5faff);
}
.main {
    background-color: #ffffffcc;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}
h1 {
    color: #0d47a1;
    text-align: center;
}
h3 {
    color: #1565c0;
}
.stTextInput input {
    border-radius: 10px;
    border: 1px solid #90caf9;
    padding: 10px;
}
.stSelectbox div {
    border-radius: 10px !important;
}
.stButton button {
    background: linear-gradient(90deg, #42a5f5, #1e88e5);
    color: white;
    border-radius: 10px;
    padding: 10px 20px;
    font-weight: bold;
    border: none;
}
.stButton button:hover {
    background: linear-gradient(90deg, #1e88e5, #1565c0);
}
.stDownloadButton button {
    background-color: #0d47a1;
    color: white;
    border-radius: 10px;
}
.stExpander {
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="YouTube → Article & PDF", layout="centered")

st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap" rel="stylesheet">
<h1 style="
    font-family: 'Playfair Display', serif;
    text-align: center;
    font-size: 48px;
    color: #0d47a1;
    letter-spacing: 1px;
">
🎬 Video Insight Article Generator
</h1>""", unsafe_allow_html=True)

st.markdown(
    "<p style='text-align:center; color:#555;'> ✨ Convert YouTube videos into professional articles & PDFs</p>",
    unsafe_allow_html=True
)

url = st.text_input("🔗 Enter YouTube URL")

if st.button("🚀 Generate Article & PDF"):

    if not url:
        st.warning("Please enter a YouTube URL")

    else:
        with st.spinner("Processing..."):

            transcript, title, error = get_transcript(url)

            if error:
                st.error(error)

            else:
                # ✅ STORE IN SESSION (ADDED)
                st.session_state.generated = True
                st.session_state.transcript = transcript
                st.session_state.title = title
                st.session_state.article = generate_article(transcript)


if st.session_state.generated:

    transcript = st.session_state.transcript
    title = st.session_state.title
    article = st.session_state.article

    st.success("✅ Transcript extracted")

    st.subheader(f"🎬 {title}")

    with st.expander("📄 View Transcript"):
        st.write(transcript)

    st.success("✅ Article generated!")

    safe_title = clean_filename(title)

    article_pdf = create_pdf(article)
    transcript_pdf = create_pdf(transcript)

    st.markdown("### 📥 Download Files")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "📄 Article PDF",
            article_pdf,
            file_name=f"{safe_title}_article.pdf",
            mime="application/pdf"
        )

    with col2:
        st.download_button(
            "📜 Transcript PDF",
            transcript_pdf,
            file_name=f"{safe_title}_transcript.pdf",
            mime="application/pdf"
        )

    st.subheader("📄 Generated Article")
    st.text_area("", article, height=400)

    st.markdown("---")
    if st.button("🔄 Clear & Start New"):
        st.session_state.clear()
        st.rerun()