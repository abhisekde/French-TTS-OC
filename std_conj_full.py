#!/usr/bin/env python
# coding=utf-8

from gtts import gTTS, gTTSError
from playsound import playsound
import time
from os import path
from conj import en_fr
import sys
import random 

# French conjugation in present tense indicative mode
# Author: mr.abhisek.de@gmail.com
# Uses Google Text-to-Speech (gTTS) 

def get_audio(fr_text, mp3_name):
    audio_file  = "./conjugation/{}.mp3".format(mp3_name)
    tts = gTTS(text=fr_text, lang="fr")
    tts.save(audio_file)
    return audio_file

def play(mp3_name):
    audio_file = "./conjugation/{}.mp3".format(mp3_name)
    if not path.exists(audio_file):
        get_audio(mp3_name.decode("utf-8"), mp3_name)
    playsound(audio_file)

# __main__ 
conj_list = en_fr
total_nr = len(conj_list)
count_nr = 0
exit_code = 0
while total_nr > count_nr:
    count_nr = count_nr +1
    last_i = len(conj_list) -1
    i = random.randint(0, last_i) 
    try:
        item = conj_list[i]
        fr_text = item["fr"]
        en_text = item["en"]
        print("{} -> {}".format(fr_text, en_text))
        play(fr_text)
        time.sleep(1)
        conj_list.remove(item)

    except KeyboardInterrupt:
        print("")
        exit_code = 0
        break
    except gTTSError:
        exit_code = 1
        print("Can't connect to Google TTS, moving on...")
    except IndexError:
        exit_code = -1
        break # No option, break loop
    except ValueError:
        exit_code = -1
        break # No option, break loop
    except KeyError:
        exit_code = -1
        break # No option, break loop
    except Exception:
        exit_code = 1
        print("Unexpected error, moving on...")
# end of while loop
exit(exit_code)
