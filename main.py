import speech_recognition as sr
import pyttsx3,webbrowser,time,pyjokes,wikipedia
from datetime import datetime,date

engine = pyttsx3.init()
engine.setProperty('rate',145)
r = sr.Recognizer()


def listneForCommand():
    with sr.Microphone() as Source:
        print("Listening...")
        r.pause_threshold = 1
        while True:
            audio = r.listen(Source,phrase_time_limit=4)
            try:
                text = r.recognize_google(audio).lower()
                if "hi jarvis" == text:
                    speak("Hello I Am jarvis. How can i help you?")
                    time.sleep(3)
                    listneForCommand()
                elif "hi jarvis" in text:
                    command = text.split("hi jarvis")
                    getFullCommand(command)
                else:
                    getFullCommand(text)
            except Exception as e:
                print(e)


def getFullCommand(cmd):
    if "open" in cmd:
        link = cmd.split("open")[1].replace(" ","")
        try:
            webbrowser.open_new_tab(link)
        except Exception as e:
            print(e)
        finally:
            time.sleep(2)
            listneForCommand()
    elif "close" in cmd:
        exit()
    elif "joke" in cmd:
        jokes = pyjokes.get_joke()
        speak(jokes)
        time.sleep(2)
        listneForCommand()
    elif "search wikipedia" in cmd:
        query = cmd.split("search wikipedia")[1].replace(" ","")
        results = wikipedia.summary(query,sentences = 3)
        speak(results)
        time.sleep(2)
        listneForCommand()
    elif "time now" in cmd:
        now = datetime.now()
        times = now.strftime("%H:%M:%S")
        speak(f"time now is {times}")
        time.sleep(2)
        listneForCommand()
    elif "today's date" in cmd:
        today = date.today()
        d1 = today.strftime("%B %d, %Y")
        speak(f"today's date is {d1}")
        time.sleep(2)
        listneForCommand()
    elif "date and time" in cmd:
        now = datetime.now()
        times = now.strftime("%H:%M:%S")
        today = date.today()
        d1 = today.strftime("%B %d, %Y")
        speak(f"today is {d1} and Time now is {times}")
        time.sleep(2)
        listneForCommand()
    elif "what is your name" in cmd:
        speak("my name is jarvis")
        time.sleep(2)
        listneForCommand()
    elif "who made you" in cmd:
        speak("arnab gupta")
        time.sleep(2)
        listneForCommand()

def speak(aud):
    engine.say(aud)
    engine.runAndWait()


if __name__ == "__main__":
    listneForCommand()



# engine.say(text)
# engine.runAndWait()