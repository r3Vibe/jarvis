import speech_recognition as sr

class Recognizer:
    r = sr.Recognizer()

    def listen(self):
        self.r.pause_threshold = 1
        with sr.Microphone() as Source:
            audio = self.r.listen(Source,phrase_time_limit=4)
            try:
                text = self.r.recognize_google(audio).lower()
            except Exception as e:
                return "could not recognize voice"
            else:
                return text


import pyttsx3

class Speak:
    engine = pyttsx3.init()
    engine.setProperty('rate',145)

    def speakout(self,voice):
        self.engine.say(voice)
        self.engine.runAndWait()



class ExecuteCommand:
    def __init__(self,cmd):
        self.cmd = cmd

    def Execute(self):
        if "exit" == self.cmd:
            exit()
        else:
            Speak().speakout(self.cmd)
            print(self.cmd)




class ExtractCommand:
    def __init__(self,cmd):
        self.cmd = cmd
    
    def Extract(self):
        if "close" in self.cmd:
            return "exit"
        else:
            return f"{self.cmd}"



