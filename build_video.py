from moviepy.editor import *
import os
import random

# Folders
ASSETS_FOLDER = "assets"
AUDIO_FILE = "audio/voice.mp3"
OUTPUT_FILE = "video/output.mp4"

os.makedirs("video", exist_ok=True)

# Load audio
audio = AudioFileClip(AUDIO_FILE)

# Get video clips
clips = []
for file in os.listdir(ASSETS_FOLDER):
    if file.endswith((".mp4", ".mov")):
        clips.append(VideoFileClip(os.path.join(ASSETS_FOLDER, file)))

if not clips:
    raise Exception("No video clips found in assets folder!")

# Randomize for natural feel
random.shuffle(clips)

# Trim clips to match audio duration
final_clips = []
duration_left = audio.duration

for clip in clips:
    if duration_left <= 0:
        break

    clip = clip.resize(height=720)  # YouTube HD quality
    clip = clip.set_fps(30)

    if clip.duration > duration_left:
        clip = clip.subclip(0, duration_left)

    final_clips.append(clip)
    duration_left -= clip.duration

# Combine
final_video = concatenate_videoclips(final_clips, method="compose")
final_video = final_video.set_audio(audio)

# Export (higher quality settings)
final_video.write_videofile(
    OUTPUT_FILE,
    fps=30,
    codec="libx264",
    audio_codec="aac",
    bitrate="5000k",
    threads=4
)

print("DONE: High-quality video created!")
