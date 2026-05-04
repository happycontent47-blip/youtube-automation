import os

print("STEP 1: Generating voice...")
os.system("python generate_voice.py")

print("STEP 2: Building video...")
os.system("python build_video.py")

print("DONE: Full video generated in /video")
