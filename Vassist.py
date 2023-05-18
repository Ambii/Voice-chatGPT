import speech_recognition as sr
import pyttsx3
import time
import os
import openai

# Set up OpenAI ChatGPT
openai.api_key = "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"
engine = pyttsx3.init()
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[0].id)
engine.setProperty('voice', voices[1].id)

# Function to convert speech to text
def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Sorry, I could not understand.")
        return ""
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return ""

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# ChatGPT interaction function
def chat(text):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=text,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
    )
    reply = response.choices[0].text.strip()
    print("ChatGPT:", reply)
    speak(reply)

# Main program loop
if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            chat(user_input)
        time.sleep(1)
