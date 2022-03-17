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
                Speak().speakout("Unable to recognize voice")
                return "could not recognize voice"
            else:
                return text





