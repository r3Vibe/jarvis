import speech_recognition as sr
from .speaker import Speak

class Recognizer:
    r = sr.Recognizer()

    def listen(self):
        self.r.pause_threshold = 0.5
        with sr.Microphone() as Source:
            audio = self.r.listen(Source,phrase_time_limit=4,timeout=None)
            try:
                text = self.r.recognize_google(audio).lower()
            except Exception as e:
                return "false"
            else:
                return text





