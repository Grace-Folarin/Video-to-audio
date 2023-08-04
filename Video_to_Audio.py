#!/usr/bin/python3

import os
import subprocess
import moviepy.editor as mp

from moviepy.editor import VideoFileClip

def extract_audio(video_path, output_audio_path):
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_audio_path)
    audio_clip.close()
    video_clip.close()

video_path = "input_video.mp4"
output_audio_path = "output_audio.wav"

extract_audio(video_path, output_audio_path)
