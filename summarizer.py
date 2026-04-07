from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_article_with_groq(transcript, length="medium"):
    
    length_map = {
        "short": "around 300 words",
        "medium": "around 600 words",
        "long": "around 1000 words"
    }

    prompt = f"""
Convert the following YouTube transcript into a professional article.

Requirements:
- Title
- Introduction
- Key Insights (bullet points)
- Detailed Explanation
- Conclusion

Length: {length_map[length]}

Transcript:
{transcript}
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",  # fast + powerful
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content