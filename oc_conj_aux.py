#!/usr/bin/env python
# coding=utf-8

import random
from playsound import playsound
import time

# __main__():
fr_vr = { "I have": "J'ai",  "One have": "On a",  "He have": "Il a",  "You have": "Vous avez",  "We have": "Nous avon",  "They have": "Ils ont",  "I am": "Je suis",  "You have": "Tu as",  "You are": "Vous êtes",  "She is": "Elle est",  "You are": "Tu es",  "We are": "Nous sommes",  "They are": "ils sont",  "I do": "Je fais",  "You do": "Tu fais",  "He does": "Il fait",  "She does": "Elle fait",  "One does": "On fait",  "We do": "Nous faisons",  "You do": "Vous faites",  "They do": "Ils font",  "I go": "Je vais",  "You go": "Tu vas",  "He goes": "Il va",  "She goes": "Elle va",  "One goes": "On va",  "We go": "Nous allons",  "You go": "Vous allez",  "They go": "Ils vont" }
fr = fr_vr.values()
en = fr_vr.keys()
ans = []
last = -1
try:
    while True:
        i = random.randint(0, len(fr) -1) # last index = size -1
        if i == last:
            continue
        else:
            last = i
            playsound("./conjugation/{}.mp3".format(fr[i]))
            ans.append(i)
            time.sleep(1)
except KeyboardInterrupt:
    # Assumtion: Last item has already been fetched by the time we break the loop, so we ignore the unattempted last item 
    print(" Answers:")
    for i in range(len(ans) -1): # range(a, b) => [a, b)
        print("{} -> {}".format(fr[ans[i]], en[ans[i]]))
except Exception as e:
    print("Unexpected error: " + e.__str__())
