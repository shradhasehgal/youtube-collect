import os
import speech_recognition as sr

command2mp3 = "ffmpeg -i video3.mp4 video3.mp3"
command2wav = "ffmpeg -i video3.mp3 video3.wav"
os.system(command2mp3)
os.system(command2wav)

r = sr.Recognizer()
audio = sr.AudioFile('video3.wav')

with audio as source:
    audio = r.record(source, duration=400)
    print(r.recognize_google(audio))