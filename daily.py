# coding=utf-8
import csv 
import random
import time
from gtts import gTTS
import os
import gi

# GLOBAL VARS
CONJUGATIONS = 'conjugations.csv'

# https://github.com/TaylorSMarks/playsound/
def playsound(file_path):
    try:
        from urllib.request import pathname2url
    except ImportError:
        # python 2
        from urllib import pathname2url
    try:
        gi.require_version('Gst', '1.0')
        from gi.repository import Gst
        Gst.init(None)
        playbin = Gst.ElementFactory.make('playbin', 'playbin')
        playbin.props.uri = 'file://' + pathname2url(os.path.abspath(file_path))
        set_result = playbin.set_state(Gst.State.PLAYING)
        if set_result != Gst.StateChangeReturn.ASYNC:
            raise PlaysoundException(
                "playbin.set_state returned " + repr(set_result))
        bus = playbin.get_bus()
        bus.poll(Gst.MessageType.EOS, Gst.CLOCK_TIME_NONE)
    except Exception as e:
        print("gstreamer-exception:", e.__str__())
    finally:
        playbin.set_state(Gst.State.NULL)

# https://gtts.readthedocs.io/
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
                print("{} -> {}".format(row['fr'], row['en']))
                play(row["fr"])
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("")
        pass

# __main__()
load_conj(CONJUGATIONS)

