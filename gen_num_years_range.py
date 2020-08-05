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
    audio_file  = "./years/{}.mp3".format(text)
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
    ans = []
    print("Press Ctrl+C to stop")
    while True:
        randn = random.randint(range_start, range_end).__str__()
        ans.append(randn)
        # playsound(audio(randn))
        # time.sleep(1)
        audio(randn)
except KeyboardInterrupt:
    # Assumtion: Last number has already been fetch by the time we break the loop, so we ignore the unattempted last number 
    size  = len(ans)
    print(" Answers:")
    print(ans[:size-1]) 
except ValueError:
    print("Please pass integer <start> and <end> values, with start < end")
except gTTSError:
    print("Can't connect to Google TTS service.")
except PlaysoundException:
    pass
except Exception as e:
    print("Unexpected error: " + e.__str__())

