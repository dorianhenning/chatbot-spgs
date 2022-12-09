import os
import numpy as np
import speech_recognition as sr
from gtts import gTTS


class ChatBot():
    def __init__(self, name: str):
        self.name = name
        print(f"Starting up: {name}")
        self.up = False

    def speech_to_text(self):
        recognizer = sr.Recognizer()
        with sr.Microphone() as mic:
             print("listening...")
             audio = recognizer.listen(mic)
        try:
             self.text = recognizer.recognize_google(audio)
             print("me --> ", self.text)
        except:
             print("me -->  ERROR")

    def wake_up(self, text):
        correct_name = self.name.lower() in text.lower()
        if not self.up:
            self.up = correct_name
            return correct_name
        else:
            return False

    @staticmethod
    def text_to_speech(text):
        print("AI --> ", text)
        speaker = gTTS(text=text, lang="en", slow=False)
        speaker.save("res.mp3")
        os.system("mpg123 res.mp3")  #if you have a macbook->afplay or for windows use->start
        os.remove("res.mp3")

# Execute when script is called
if __name__ == "__main__":
    ai = ChatBot("Tom")

    while True:
        ai.speech_to_text()
        ## wake up
        if ai.wake_up(ai.text):
            res = "Hello I am Tom the AI, what can I do for you?"
            ai.text_to_speech(res)
