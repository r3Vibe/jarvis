from time import sleep
from .speaker import Speak
from .recognizer import Recognizer
import pyjokes,wikipedia,os,pyautogui

class ExecuteCommand:
    def __init__(self,cmd):
        self.cmd = cmd

    def Execute(self):
        if "exit" == self.cmd:
            exit()
        elif "joke" == self.cmd:
            myjoke = pyjokes.get_joke(language="en",category='all')
            Speak().speakout(myjoke)
        elif "steam" == self.cmd:
            Speak().speakout("starting steam")
            os.startfile(r"C:\\Program Files (x86)\Steam\steam.exe")
        elif "uplay" == self.cmd:
            Speak().speakout("starting uplay")
            os.startfile(r"C:\\Program Files (x86)\\Ubisoft\\Ubisoft Game Launcher\\UbisoftGameLauncher64.exe")
        elif "torrent" == self.cmd:
            Speak().speakout("starting torrent")
            os.startfile(r"C:\\Users\\arnab\AppData\\Roaming\\BitTorrent\\BitTorrent.exe")
        elif "excel" == self.cmd:
            Speak().speakout("starting excel")
            os.startfile(r"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
        elif "word" == self.cmd:
            Speak().speakout("starting word")
            os.startfile(r"C:\\Program Files\\Microsoft Office\\root\\Office16\WINWORD.EXE")
        elif "notes" == self.cmd:
            os.popen("notepad")
            sleep(2)
            Speak().speakout("Start telling your note now")
            text = Recognizer().listen()
            pyautogui.typewrite(text)
        else:
            Speak().speakout(self.cmd)

    def SearchWiki(self,param):
        wikin = wikipedia.summary(param,sentences=3)
        Speak().speakout(wikin)


