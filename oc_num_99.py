#!/usr/bin/env python
import sys
import random
from playsound import playsound, PlaysoundException # requires GStreamer
import time

# __main__():
if len(sys.argv) != 3:
    print("Usage: {} <start> <end>".format(sys.argv[0]))
    sys.exit(1)
try:
    range_start = int(sys.argv[1])
    range_end   = int(sys.argv[2])
    
    if range_start >= range_end or range_start < 10 or range_end > 99:
        raise ValueError()
    ans = []
    print("Press Ctrl+C to stop")
    last = '-1'
    while True:
        randn = random.randint(range_start, range_end).__str__()
        if last == randn:
            continue
        else:
            last = randn
        ans.append(randn)
        playsound("./audio/{}.mp3".format(randn))
        time.sleep(0.5)
except KeyboardInterrupt:
    # Assumtion: Last number has already been fetch by the time we break the loop, so we ignore the unattempted last number 
    size  = len(ans)
    print(" Answers:")
    print(ans[:size-1]) 
    sys.exit(0)
except ValueError:
    print("Please pass integer <start> and <end> values, in range [10, 99]")
    sys.exit(1)
except PlaysoundException:
    sys.exit(0)
except Exception as e:
    print("Unexpected error: " + e.__str__())
    sys.exit(1)

