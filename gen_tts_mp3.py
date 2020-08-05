# coding=utf-8
from playsound import playsound
from gtts import gTTS
from sys import argv 
if len(argv) != 3:
    print("Usage: {} 'phrase française' /path/mp3/folder".format(argv[0]))
    exit(1)
text_fr = argv[1] 
out_dir = argv[2]
tts = gTTS(text = text_fr.decode('utf-8'), lang = "fr")
tts.save("{}/{}.mp3".format(out_dir, text_fr))
playsound("{}/{}.mp3".format(out_dir, text_fr))

