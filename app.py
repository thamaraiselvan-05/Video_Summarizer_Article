import streamlit as st
from transcript import get_transcript
from article_generator import generate_article
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

            transcript, title, error = get_transcript(url)

            if error:
                st.error(error)

            else:
                st.success("✅ Transcript extracted")

                # Show video title
                st.subheader(f"🎬 {title}")

                #  Optional transcript preview
                with st.expander("📄 View Transcript"):
                    st.write(transcript[:2000])

                #  Generate article
                article = generate_article(transcript, length)

                # Create PDF
                pdf_bytes = create_pdf(article)

                st.download_button(
                     "📥 Download PDF",
                      pdf_bytes,
                      file_name="article.pdf",
                      mime="application/pdf")

                st.success("✅ Article generated!")

                # Show article
                st.subheader("📄 Generated Article")
                st.text_area("", article, height=400)

                #  Download button
                with open("output.pdf", "rb") as f:
                    st.download_button("📥 Download PDF", f)