"""
PyAudio example: Record a few seconds of audio and save to a WAVE
file.
"""

import pyaudio
import wave
import sys
import socket
from struct import *
import time

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_INT = 5


if sys.platform == 'darwin':
    CHANNELS = 1

p = pyaudio.PyAudio()

if len(sys.argv) < 2:
    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)
HOST = sys.argv[1]

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)


PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sequence = 0

print("* recording")
for j in range(5000):
	frames = []
	#for i in range(0, int(RATE / CHUNK * RECORD_INT)):
	for i in range(1):
	    data = stream.read(CHUNK)
	    frames.append(data)
	data = pack('iii',sequence,time.time(),1)+b''.join(frames)

	s.sendto(data, (HOST, PORT))

s.sendto("", (HOST, PORT))

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()
'''
wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()
'''


