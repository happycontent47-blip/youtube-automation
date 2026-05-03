import os
from moviepy.editor import *

# Load audio
audio = AudioFileClip("audio/voice.mp3")

# Load clips from assets folder
clips = []
for file in os.listdir("assets"):
    if file.endswith(".mp4"):
        clip = VideoFileClip(f"assets/{file}").without_audio()
        clips.append(clip)

# Loop clips to match audio length
final_clips = []
total_duration = 0

while total_duration < audio.duration:
    for clip in clips:
        final_clips.append(clip)
        total_duration += clip.duration
        if total_duration >= audio.duration:
            break

video = concatenate_videoclips(final_clips)

# Trim to audio length
video = video.subclip(0, audio.duration)

# Add audio
video = video.set_audio(audio)

# Export
video.write_videofile("video/output.mp4", fps=24)
