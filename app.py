import streamlit as st
from transcript import get_transcript
from article_generator import generate_article_with_groq
from pdf_generator import create_pdf
import os

st.set_page_config(page_title="YouTube → Article & PDF", layout="centered")

st.title("🎬 YouTube → Article & PDF Generator")

url = st.text_input("🔗 Enter YouTube URL")

length = st.selectbox(
    "Select Article Length",
    ["short", "medium", "long"])

if st.button("🚀 Generate Article & PDF"):
    
    if not url:
        st.warning("Please enter a YouTube URL")
    
    else:
        with st.spinner("Processing..."):
            transcript = get_transcript(url)

            if "⚠️" in transcript:
                st.error(transcript)
            else:
                article = generate_article_with_groq(transcript, length)
                create_pdf(article)

                st.success("✅ Article Generated!")

                st.subheader("📄 Article")
                st.text_area("", article, height=400)

                with open("output.pdf", "rb") as f:
                    st.download_button("📥 Download PDF", f)