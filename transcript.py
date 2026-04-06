from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api._errors import RequestBlocked

def get_video_id(url):
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "v=" in url:
        return url.split("v=")[1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")

def get_transcript(url):
    video_id = get_video_id(url)

    try:
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        text = " ".join([i.text for i in transcript])
        return text

    except RequestBlocked:
        return "⚠️ YouTube blocked transcript access. Please try another video."

    except TranscriptsDisabled:
        return "⚠️ Transcripts are disabled for this video."

    except NoTranscriptFound:
        return "⚠️ No transcript available for this video."

    except Exception as e:
        return f"⚠️ Error: {str(e)}"