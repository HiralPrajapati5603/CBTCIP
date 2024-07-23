import sounddevice as sd
import wavio

# Define the parameters for the recording
fs = 44100  # Sample rate
seconds = 5  # Duration of recording in seconds

print("Recording...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
print("Recording finished")

# Save the recording as a WAV
wavio.write("output.wav", myrecording, fs, sampwidth=2)
print("Saved as output.wav")