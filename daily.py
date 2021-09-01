# coding=utf-8
# @abhisek.de 

import csv 
import time
from gtts import gTTS
import os
from playsound import playsound

# GLOBAL VARS 
# FR most used verb's conjugation database
# https://github.com/abhisekde/French-TTS-OC/blob/master/conjugations.csv
CONJUGATIONS = 'conjugations.csv'

# https://gtts.readthedocs.io
def save_tts(fr_text, audio_file):
    tts = gTTS(text=fr_text, lang='fr')
    tts.save(audio_file.strip())

def play(conj):
    file_name = conj.replace("'", "-").replace(" ", "-")
    full_path = "conj20/{}.mp3".format(file_name)
    if not os.path.isfile(full_path):
        save_tts(conj, full_path)
    playsound(full_path)

def load_conj(file_path):
    try:
        with open(file_path) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['fr'] == '':
                    continue
                print("{} -> {}".format(row['fr'], row['en']))
                play(row["fr"])
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("")
        pass

# __main__()
load_conj(CONJUGATIONS)
