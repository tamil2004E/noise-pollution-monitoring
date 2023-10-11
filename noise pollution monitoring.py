import sounddevice as sd
import numpy as np

# Define parameters
duration = 10  # Duration of the monitoring in seconds
sample_rate = 44100  # Sampling rate (Hz)
threshold_db = 60  # Threshold in decibels for noise pollution

def audio_callback(indata, frames, time, status):
    if status:
        print(f"Error in audio input: {status}")
    if np.max(indata) > threshold_db:
        print(f"Noise pollution detected! Max dB: {np.max(indata)}")

# Start audio recording
with sd.InputStream(callback=audio_callback, channels=1, samplerate=sample_rate):
    print(f"Listening for noise pollution for {duration} seconds...")
    sd.sleep(int(duration * 1000))  # Sleep for the specified duration
