from gtts import gTTS
import os

text_from_file = open('text.txt')
text = text_from_file.read()

language = 'en' #english
obj = gTTS(text = text, lang = language, slow = False)
obj.save('speech.mp3')

#open automatically
os.system('speech.mp3')