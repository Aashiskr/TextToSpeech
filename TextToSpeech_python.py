#pip install pyttsx3

import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    
    # Set voice
    voices = engine.getProperty('voices')
    if len(voices) > 4:
        engine.setProperty('voice', voices[2].id)
    else:
        engine.setProperty('voice', voices[0].id)  # fallback
    
    # Set slower speech rate
    engine.setProperty('rate', 125)  # Try values between 100-150 for slower speech
    
    engine.say(text)
    engine.runAndWait()

# Speak multiple times
speak("hello vivek janu baby kaisi mumbai haar gyina")

