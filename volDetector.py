
import sounddevice as sd
import numpy as np

duration = 3
threshold = 2

def callback(indata, outdata, frames, time, status):
        vol = np.linalg.norm(indata) * 10
        if (vol > threshold):
                print("Audio Detected")
        else:
                print("Waitin")

with sd.Stream(callback = callback):
        sd.sleep(duration * 1000)
