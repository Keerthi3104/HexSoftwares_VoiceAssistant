import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pywhatkit

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good Morning")
    elif hour < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am your assistant. How can I help you?")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
    except:
        print("Say again...")
        return "none"
    return command.lower()

def run_assistant():
    wish()
    while True:
        command = take_command()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak("The time is " + time)

        elif "open google" in command:
            webbrowser.open("https://www.google.com")

        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")

        elif "play" in command:
            song = command.replace("play", "")
            speak("Playing " + song)
            pywhatkit.playonyt(song)

        elif "who is" in command:
            person = command.replace("who is", "")
            info = wikipedia.summary(person, 2)
            speak(info)

        elif "search" in command:
            query = command.replace("search", "")
            pywhatkit.search(query)

        elif "stop" in command or "exit" in command:
            speak("Goodbye")
            break

run_assistant()