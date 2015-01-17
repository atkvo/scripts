#!/usr/bin/env python3

import argparse
import time

parser = argparse.ArgumentParser(description='Timer in minutes.')
parser.add_argument("mins", help="time to countdown from", type=float)
args = parser.parse_args()

print("Time left: ", args.mins)
i = 60 * args.mins


while i >= 0:
    minutes = int(i/60)
    seconds = int(((i/60) - minutes)*60)
    print("{0:0=2d}".format(minutes), ":", "{0:0=2d}".format(seconds))
    i = i - 1 
    time.sleep(1)
print("TIMEUP")
    
