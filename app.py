import streamlit as st
from transcript import get_transcript
from article_generator import generate_article
from pdf_generator import create_pdf
import os

st.markdown("""
<style>

/* Background */
.stApp {
    background: linear-gradient(135deg, #e3f2fd, #f5faff);
}

/* Main container (card effect) */
.main {
    background-color: #ffffffcc;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
}

/* Title */
h1 {
    color: #0d47a1;
    text-align: center;
}

/* Subheader */
h3 {
    color: #1565c0;
}

/* Input box */
.stTextInput input {
    border-radius: 10px;
    border: 1px solid #90caf9;
    padding: 10px;
}

/* Selectbox */
.stSelectbox div {
    border-radius: 10px !important;
}

/* Button */
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

/* Download button */
.stDownloadButton button {
    background-color: #0d47a1;
    color: white;
    border-radius: 10px;
}

/* Expander */
.stExpander {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.set_page_config(page_title="YouTube → Article & PDF", layout="centered")

st.markdown("<h1>🎬 AI Video Insight Generator</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; color:#555;'>Convert YouTube videos into professional articles & PDFs</p>",
    unsafe_allow_html=True)
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
                st.download_button(
                     "📥 Download PDF",
                      pdf_bytes,
                      file_name="output.pdf",
                      mime="application/pdf")