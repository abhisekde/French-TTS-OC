#!/usr/bin/env python
import sys
from gtts import gTTS, gTTSError
import random
from playsound import playsound, PlaysoundException # requires GStreamer
import time
# French numbers oral comprehension
# Author: mr.abhisek.de@gmail.com
# Uses Google Text-to-Speech (gTTS) API

def audio(text):
    audio_file  = "./audio/{}.mp3".format(text)
    tts = gTTS(text=text, lang='fr')
    tts.save(audio_file)
    return audio_file

# __main__():
if len(sys.argv) != 3:
    print("Usage: {} <start> <end>".format(sys.argv[0]))
    sys.exit(1)
try:
    range_start = int(sys.argv[1])
    range_end   = int(sys.argv[2])
    
    if range_start >= range_end:
        raise ValueError()
    print("Press Ctrl+C to stop")
    #while True:
    for i in range(range_start, range_end+1):
        #randn = random.randint(range_start, range_end).__str__()
        randn = i.__str__()
        sound = audio(randn)
        print(randn)
        playsound(sound)
        # time.sleep(1)
except KeyboardInterrupt:
    # Assumtion: Last number has already been fetch by the time we break the loop, so we ignore the unattempted last number 
    pass
except ValueError:
    print("Please pass integer <start> and <end> values, with start < end")
except gTTSError:
    print("Can't connect to Google TTS service.")
except PlaysoundException:
    pass
except Exception as e:
    print("Unexpected error: " + e.__str__())
