import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=4 and hour<12:
        speak("morning o g")

    elif hour>=12 and hour<18:
        speak("afternoon innit?")
    else:
        speak("evening o g")

    speak(" alright, im god and im designed to destruct, gimme commands and see the destruction i cause HAHAHAHHAHAHA")
def takecommand():
    #takes mic input dimwit
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tryna Listen")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Tryna Interpret")
        query = r.recognize_google(audio, language='en-in')
        print("you typed", query)

    except Exception as e:
        #print(e)

        print("come again..")
        return "None"
    return query

if __name__ == "__main__":
    wishme()
    while True:

        query = takecommand().lower()
        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("by wikipedia")
            print(results)
            speak(results)
        elif 'instagram' in query:
            webbrowser.open("instagram.com")

        elif 'vs code' in query :
            cPath = r"C:\Users\Dell\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(cPath)
        elif 'attack' in query:
            cpath = r"C:\Users\Dell\Desktop\god\slowloris.py"
            os.startfile(cpath)
