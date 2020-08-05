#!/usr/bin/env python

import sys, os, time, thread
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib, GObject
from conj import en_fr
from gtts import gTTS, gTTSError
import playsound

class CLI_Main(object):

    def __init__(self):
        self.player = Gst.ElementFactory.make("playbin", "player")
        fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
        self.player.set_property("video-sink", fakesink)
        bus = self.player.get_bus()
        bus.add_signal_watch()
        bus.connect("message", self.on_message)

    def on_message(self, bus, message):
        t = message.type
        if t == Gst.MessageType.EOS:
            self.player.set_state(Gst.State.NULL)
            self.playmode = False
        elif t == Gst.MessageType.ERROR:
            self.player.set_state(Gst.State.NULL)
            err, debug = message.parse_error()
            raise Exception(debug)
            self.playmode = False

    def get_audio(self, text, file_name):
        audio_file  = "./conjugation/{}".format(file_name)
        tts = gTTS(text=text, lang="fr")
        tts.save(audio_file)
        return audio_file

    def conjugations(self):
        for item in en_fr:
            fr_text = item["fr"]
            en_text = item["en"]
            print("{} -> {}".format(fr_text, en_text))
            if en_text.startswith("They"):
                print("") 
            yield "./conjugation/{}.mp3".format(fr_text)
                
    def start(self):
        for filepath in self.conjugations():
            if not os.path.exists(filepath):
                text = os.path.basename(filepath).replace(".mp3", "")
                file_name = os.path.basename(filepath)
                self.get_audio(text, file_name)

            filepath = os.path.realpath(filepath)
            self.playmode = True
            self.player.set_property("uri", "file://" + filepath)
            self.player.set_state(Gst.State.PLAYING)
            while self.playmode:
                time.sleep(1)
            time.sleep(1)
        loop.quit()

# __main__
GObject.threads_init()
Gst.init(None)        
mainclass = CLI_Main()
thread.start_new_thread(mainclass.start, ())
loop = GLib.MainLoop()
try:
    loop.run()
except KeyboardInterrupt:
    print("")
except gTTSError:
    print("Can't connect to Google TTS, moving on...")
except Exception:
    print("Unexpected error, moving on...")