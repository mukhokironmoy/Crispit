from youtube_transcript_api import YouTubeTranscriptApi as scriptapi
from youtube_transcript_api.formatters import TextFormatter as format
import summarise

def get_video_id(url):
    import re
####
    # Handle standard watch?v= links
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    
    # Handle youtu.be short links
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    
    # Handle /live/ links
    elif "youtube.com/live/" in url:
        return url.split("youtube.com/live/")[-1].split("?")[0]
    
    # Optional: use regex fallback
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11})", url)
    if match:
        return match.group(1)
    
    raise ValueError("Invalid YouTube URL format")

    
def transcript(url):
    try:
        video_id = get_video_id(url)
        transcript_data = scriptapi.get_transcript(video_id)
        lines = [entry['text'] for entry in transcript_data]
        formatted_transcript = "\n".join(lines)
        
        open("data/transcript.txt", "w").close()        
        
        with open("data/transcript.txt", 'w', encoding='utf-8') as f:
                f.write(formatted_transcript)

        print(f"Transcript saved.")
    
    except Exception as e:
        print(f"Error: {e}")
        
video_url = input("Paste the YouTube video URL: ")
transcript(video_url)

summarise.news()