from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled, NoTranscriptFound
from youtube_transcript_api._errors import RequestBlocked

def get_video_id(url):
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]

    elif "youtube.com/watch" in url:
        return url.split("v=")[1].split("&")[0]

    elif "youtube.com/shorts/" in url:
        return url.split("shorts/")[1].split("?")[0]

    else:
        raise ValueError("Invalid YouTube URL")


def get_transcript(url):
    video_id = get_video_id(url)

    try:
        # ✅ USE THIS (more reliable)
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])

        text = " ".join([i['text'] for i in transcript])
        return text

    except RequestBlocked:
        return "⚠️ YouTube blocked transcript access. Try another video."

    except TranscriptsDisabled:
        return "⚠️ Transcripts are disabled for this video."

    except NoTranscriptFound:
        return "⚠️ No transcript available."

    except Exception as e:
        return "⚠️ Unable to fetch transcript. Try another video."