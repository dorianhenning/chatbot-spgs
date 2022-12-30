import os
import numpy as np
import speech_recognition as sr
from gtts import gTTS
import transformers


class ChatBot:
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
        os.system(
            "mpg123 res.mp3"
        )  # if you have a macbook->afplay or for windows use->start
        os.remove("res.mp3")


class AiChatBot:
    def __init__(self):
        self.model = transformers.AutoModelForCausalLM.from_pretrained(
            "microsoft/DialoGPT-medium"
        )
        self.tokenizer = transformers.AutoTokenizer.from_pretrained(
            "microsoft/DialoGPT-medium"
        )

        self.eos_token = self.tokenizer.eos_token
        self.eos_token_id = self.tokenizer.eos_token_id
        self.max_length = 1000

    def response(self, query: str):
        query_tokens = self.tokenizer.encode(
            query + self.eos_token, return_tensors="pt"
        )
        response_tokens = self.model.generate(
            query_tokens, max_length=self.max_length, pad_token_id=self.eos_token_id
        )

        response_string = self.tokenizer.decode(
            response_tokens[:, query_tokens.shape[-1] :][0], skip_special_tokens=True
        )
        print(f"DialoGPT: {response_string}")


# Execute when script is called
if __name__ == "__main__":
    ai = AiChatBot()

    input_string = "Hello, what is your name?"

    ai.response(input_string)

    chatbot = ChatBot("Tom")

    while True:
        chatbot.speech_to_text()
        ## wake up
        if chatbot.wake_up(chatbot.text):
            res = "Hello I am Tom the AI, what can I do for you?"
            chatbot.text_to_speech(res)
