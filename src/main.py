import speech_recognition as sr
import time
import requests
import json
import sys
def main():
    mic = sr.Microphone(device_index=1)

    r = sr.Recognizer()
    r.pause_threshold=5

    with open("device_info.json", 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

        print(data)

        while True:
            with mic as source:
                
                try:
                    r.adjust_for_ambient_noise(source, duration=1)
                    
                    print("Listening...")
                    audio = r.listen(source, phrase_time_limit=10)
                    start_recognition = time.time()
                    # text = r.recognize_whisper(audio, model="tiny.en") 
                    text = str(r.recognize_google(audio)).lower()
                    end_recognition = time.time()

                    # if hotword in text, send request to api
                    if "jarvis" in text:
                        command = text.replace("jarvis", "")

                        headers = {
                            "Authorization": data["device_id"]
                        }

                        payload = json.dumps({
                            "input": command
                        })

                        response = requests.post("https://jarvos.io/api/assistant", headers=headers, data=payload)

                        print(f"the command: {command}")
                        print(f"returned: {response.json()}")


                        print(f"It took {end_recognition - start_recognition} seconds")
                except sr.UnknownValueError:
                    print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    main()
