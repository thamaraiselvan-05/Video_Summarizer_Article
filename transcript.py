from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    elif "v=" in url:
        return url.split("v=")[1].split("&")[0]
    else:
        raise ValueError("Invalid YouTube URL")

def get_transcript(url):
    video_id = get_video_id(url)

    api = YouTubeTranscriptApi()
    transcript = api.fetch(video_id)

    text = " ".join([i.text for i in transcript])
    
    return text