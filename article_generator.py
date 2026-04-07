from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_article(transcript, length="medium"):
    length = length.lower()
    length_map = {
        "short": "Around 300 words",
        "medium": "Around 600 words",
        "long": "Around 1000 words"
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
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return response.choices[0].message.content