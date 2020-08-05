#!/usr/bin/env python
# coding=utf-8

from gtts import gTTS, gTTSError
from playsound import playsound
import time
from os import path
from conj import en_fr
import sys
# French conjugation in present tense indicative mode
# Author: mr.abhisek.de@gmail.com
# Uses Google Text-to-Speech (gTTS) 

def get_audio(text, file_name):
    audio_file  = "./conjugation/{}.mp3".format(file_name)
    tts = gTTS(text=text, lang="fr")
    tts.save(audio_file)
    return audio_file

def play(file_name):
    full_path = "./conjugation/{}.mp3".format(file_name)
    if not path.exists(full_path):
        get_audio(file_name.decode("utf-8"), file_name)
    playsound(full_path)

# __main__ 
for item in en_fr:
    fr_text = item["fr"]
    en_text = item["en"]
    try:
        print("{} -> {}".format(fr_text, en_text))
        play(fr_text)
        time.sleep(1)
        if en_text.startswith("They"):
            print("") 
    except KeyboardInterrupt:
        print("")
        break
    except gTTSError:
        print("Can't connect to Google TTS, moving on...")
    except Exception:
        print("Unexpected error, moving on...")
