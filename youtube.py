from pytube import YouTube
from pydub import AudioSegment

# URL of the YouTube video
url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Download the YouTube video
video = YouTube(url)
video_stream = video.streams.get_audio_only()
video_stream.download()

# Convert the downloaded video to MP3
video_filename = video_stream.default_filename
audio_filename = video_filename.replace(".mp4", ".mp3")
audio = AudioSegment.from_file(video_filename, format="mp4")
audio.export(audio_filename, format="mp3")

