#!/usr/bin/env python3

# imports
import os
import wave
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-f', help='audiofile', dest='audiofile')
args = parser.parse_args()
af = args.audiofile
arged = False
if af:
    arged = True
def cls():
  os.system("clear")
def help():
  print("\033[92mExtract Your Secret Message from Audio Wave File.\033[0m")
  print ('''usage: ExWave.py [-h] [-f AUDIOFILE]

optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File''')
  
def ex_msg(af):
    if not arged:
      help()
    else:
        print ("Please wait...")
        waveaudio = wave.open(af, mode='rb')
        frame_bytes = bytearray(list(waveaudio.readframes(waveaudio.getnframes())))
        extracted = [frame_bytes[i] & 1 for i in range(len(frame_bytes))]
        string = "".join(chr(int("".join(map(str,extracted[i:i+8])),2)) for i in range(0,len(extracted),8))
        msg = string.split("###")[0]
        print("Your Secret Message is: \033[1;91m"+msg+"\033[0m")
        waveaudio.close()
cls()

try:
  ex_msg(af)
except:
  print ("Something went wrong!! try again")
  quit('')