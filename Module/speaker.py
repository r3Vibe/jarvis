import pyttsx3

class Speak:
    engine = pyttsx3.init()
    engine.setProperty('rate',145)

    def speakout(self,voice):
        self.engine.say(voice)
        self.engine.runAndWait()



