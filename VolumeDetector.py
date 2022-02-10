#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import sounddevice as sd


# In[2]:


threshold = 2
def callback(indata, outdata, frames, time, status):
    vol = np.linalg.norm(indata) * 10
    if (vol > threshold):
        print("Audio Detected")
    else:
        print("Waiting")

#with sd.Stream(callback = callback):
#    sd.sleep(3000)

    
fs=44100
duration = 3  # seconds

myrecording = sd.rec(duration * fs, samplerate=fs, channels=1,dtype='float64')
print ("Recording Audio")

with sd.Stream(callback = callback):
    sd.sleep(3000)
    
sd.wait()

print ("Audio recording complete , Play Audio")

sd.play(myrecording, fs)

sd.wait()

print ("Play Audio Complete")

