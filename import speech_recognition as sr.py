import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Capture audio from the microphone
with sr.Microphone() as source:
    print("Say something:")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio = recognizer.listen(source, timeout=5)  # Listen for up to 5 seconds of audio input

# Use Google Web Speech API to recognize the audio
try:
    recognized_text = recognizer.recognize_google(audio)
    print("You said: " + recognized_text)
except sr.UnknownValueError:
    print("Google Web Speech API could not understand the audio")
except sr.RequestError as e:
    print("Could not request results from Google Web Speech API; {0}".format(e))
