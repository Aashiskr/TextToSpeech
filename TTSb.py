import requests
from playsound import playsound
import os
from typing import Union

def generate_audio(message: str, voice: str = "Brian") -> Union[bytes, None]:
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
    }

    try:
        result = requests.get(url, headers=headers)
        result.raise_for_status()
        return result.content
    except Exception as e:
        print("Error generating audio:", e)
        return None

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = "mp3") -> Union[str, None]:
    try:
        result_content = generate_audio(message, voice)
        if not result_content:
            return None

        filename = f"{voice}.{extension}"
        file_path = os.path.join(folder, filename)

        with open(file_path, "wb") as file:
            file.write(result_content)

        playsound(file_path)
        os.remove(file_path)

        return None

    except Exception as e:
        print("Error in speak():", e)
        return None

# Test calls
speak("hello i am jarvis")
speak("hello sir how may i help you today")
