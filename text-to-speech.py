from gtts import gTTS
import os

text_typed = input('Enter Text Here: ')

language = "en"

speech = gTTS(text=text_typed, lang=language, slow=False)

speech.save("speech.mp3")

os.system("start speech.mp3")
