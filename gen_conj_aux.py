#!/usr/bin/env python
# coding=utf-8
import sys
from gtts import gTTS, gTTSError
import random
from playsound import playsound, PlaysoundException # requires GStreamer
import time
# French numbers oral comprehension
# Author: mr.abhisek.de@gmail.com
# Uses Google Text-to-Speech (gTTS) API

def audio(text, fname):
    audio_file  = "./conjugation/{}.mp3".format(fname)
    tts = gTTS(text=text, lang='fr')
    tts.save(audio_file)
    return audio_file

# __main__():
try:
    fr_vr = { "I have": "J'ai",  "One have": "On a",  "He have": "Il a",  "You have": "Vous avez",  "We have": "Nous avon",  "They have": "Ils ont",  "I am": "Je suis",  "You (tu) have": "Tu as",  "You are": "Vous êtes",  "She is": "Elle est",  "You (tu) are": "Tu es",  "We are": "Nous sommes",  "They are": "ils sont",  "I do": "Je fais",  "You (tu) do": "Tu fais",  "He does": "Il fait",  "She does": "Elle fait",  "One does": "On fait",  "We do": "Nous faisons",  "You do": "Vous faites",  "They do": "Ils font",  "I go": "Je vais",  "You (tu) go": "Tu vas",  "He goes": "Il va",  "She goes": "Elle va",  "One goes": "On va",  "We go": "Nous allons",  "You go": "Vous allez",  "They go": "Ils vont" }
    fr = fr_vr.values()
    #while True:
    for item in fr:
        sound = audio(item.decode('utf-8'), item)
        print(item)
        #playsound(sound)
except KeyboardInterrupt:
    # Assumtion: Last number has already been fetch by the time we break the loop, so we ignore the unattempted last number 
    pass
except gTTSError:
    print("Can't connect to Google TTS service.")
except PlaysoundException:
    pass
except Exception as e:
    print("Unexpected error: " + e.__str__())
