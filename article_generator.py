from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_article(summary):
    prompt = f"""
    Convert the following summary into a professional article with:

    - Title
    - Introduction
    - Key Insights (bullet points)
    - Detailed Explanation
    - Conclusion

    Summary:
    {summary}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text