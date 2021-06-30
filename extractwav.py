# A simple code to extract messages hidded using hidewav.py

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

def clear():
    os.system('clear')

def help():
  print("\033[92mExtract Your Secret Message from Audio Wave File.\033[0m")
  print ('''usage: extractwav.py [-h] [-f AUDIOFILE]
optional arguments:
  -h, --help    show this help message and exit
  -f AUDIOFILE  Select Audio File''')