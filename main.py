from gtts import gTTS
from playsound import playsound
import time
import pyttsx3
import os
import openai
import pyaudio
import openai
import speech_recognition as sr


openai.organization = "org-rsLil8CYVScO9y4IxDiFJpQW"
openai.api_key = "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"

prom="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today? "

def doprompt(text,prompt):
    prompt = prompt + "\nHuman: " + text + "\nAI"
    return prompt

def wattson(text):
  start_sequence = "\nAI:"
  restart_sequence = "\nHuman: "


  response = openai.Completion.create(
  engine="text-davinci-002",
  temperature=0.9,
  max_tokens=150,
  prompt=prom,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.6,
  stop=[" Human:", " AI:"]
)


  content = response.choices[0].text
  return content

lang= 'fr'
test=pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)




def alternative():
    while True:
        text=input('Type some Text :  ')
        tts=gTTS(text=text,lang=lang,slow=False)
        tts.save('test.mp3')

        time.sleep(0.6)
        playsound('test.mp3',True)

voices = engine.getProperty('voices')

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said : {}".format(text))
        return text
    except:
        print("Sorry could not recognize your voice")



while True:

    text = listen()
    prom=doprompt(text,prom)
    if text=="exit":
        output = wattson(text)[2:]
        prom = prom + output
        print(output)
        engine.say(output)
        engine.stop()
        break

    output = wattson(text)[2:]
    prom=prom+output
    print(output)
    engine.say(output)
    engine.runAndWait()



