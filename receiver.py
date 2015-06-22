"""PyAudio Example: Play a wave file."""

import pyaudio
import wave
import sys
import socket
from struct import *


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
if sys.platform == 'darwin':
    CHANNELS = 1

# instantiate PyAudio (1)
p = pyaudio.PyAudio()

# open stream (2)
stream = p.open(format=FORMAT,channels=CHANNELS,
rate=RATE,output=True)



s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 9999))

wf = wave.open("output.wav", 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)



# read data
#data = wf.readframes(CHUNK)

data = s.recv(5000)[12:]
# play stream (3)
while data != '':
    stream.write(data)
    #data = wf.readframes(CHUNK)
    wf.writeframes(b''.join(data))
    data = s.recv(5000)[12:]
    
# stop stream (4)
stream.stop_stream()
stream.close()

# close PyAudio (5)
p.terminate()
wf.close()
