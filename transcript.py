import re
import yt_dlp

def extract_video_id(url: str):
    patterns = [
        r"(?:v=|\/)([0-9A-Za-z_-]{11})",
        r"youtu\.be\/([0-9A-Za-z_-]{11})",
        r"embed\/([0-9A-Za-z_-]{11})",
        r"shorts\/([0-9A-Za-z_-]{11})",
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


# ---------- GET TRANSCRIPT + TITLE ----------
def get_transcript(url: str):
    video_id = extract_video_id(url)

    if not video_id:
        return "", "", "❌ Invalid YouTube URL"

    full_url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        "quiet": True,
        "skip_download": True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(full_url, download=False)

        # 🎯 Get title
        video_title = info.get("title", "YouTube Video")

        subtitles = info.get("subtitles", {})
        auto_captions = info.get("automatic_captions", {})

        # 🎯 Prefer English subtitles
        chosen = subtitles.get("en") or auto_captions.get("en")

        # fallback to any language
        if not chosen:
            chosen = next(iter(subtitles.values()), None) or \
                     next(iter(auto_captions.values()), None)

        if not chosen:
            return "", video_title, "⚠️ No captions available for this video."

        # 🎯 Get subtitle URL
        subtitle_url = next(
            (f["url"] for f in chosen if f.get("ext") == "json3"),
            chosen[0]["url"]
        )

        # 🎯 Download subtitles
        import urllib.request, json

        with urllib.request.urlopen(subtitle_url) as response:
            content = response.read().decode("utf-8")

        # 🎯 Parse JSON subtitles
        try:
            data = json.loads(content)
            events = data.get("events", [])

            texts = []
            for event in events:
                for seg in event.get("segs", []):
                    t = seg.get("utf8", "").strip()
                    if t and t != "\n":
                        texts.append(t)

            transcript_text = " ".join(texts)

        except:
            # fallback if not JSON
            transcript_text = re.sub(r"<[^>]+>", "", content)

        transcript_text = re.sub(r"\s+", " ", transcript_text).strip()

        if not transcript_text:
            return "", video_title, "⚠️ Transcript empty."

        return transcript_text, video_title, None

    except Exception as e:
        return "", "YouTube Video", f"⚠️ Error: {str(e)}"