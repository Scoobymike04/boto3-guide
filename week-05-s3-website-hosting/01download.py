import sys
from yt_dlp import YoutubeDL # type: ignore

# Check if the URL was provided as an argument
if len(sys.argv) != 2:
    print("Usage: python 01download.py <URL>")
    sys.exit(1)

# URL of the YouTube video
video_url = sys.argv[1]

# Path to save the video
save_path = 'video.mp4'

try:
    # Download the video
    ydl_opts = {'outtmpl': save_path}
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f'Video downloaded successfully and saved as {save_path}')
except Exception as e:
    print(f"Error downloading video: {e}")