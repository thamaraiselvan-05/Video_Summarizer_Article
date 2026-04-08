import streamlit as st
from groq import Groq
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY") 

client = Groq(api_key=api_key)

def generate_article(transcript):
    
    prompt = f"""
Convert the following YouTube transcript into a professional article.

Requirements:
Use plain text (no ** symbols)

- Title
- Introduction
- Key Insights (bullet points)
- Detailed Explanation
- Conclusion

Length: Around 1000 words

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content