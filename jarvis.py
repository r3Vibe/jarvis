# from Module import recognizer,execute,extractor,speaker
from Module.speaker import Speak
from Module.execute import ExecuteCommand
from Module.extractor import ExtractCommand
from Module.recognizer import Recognizer
import os
from time import sleep


def listen_for_keyword():
    os.system("cls")
    while True:
        keyw = Recognizer().listen()
        if "jarvis" in keyw:
            Speak().speakout("Yes?")
            listen_for_command()
        else:
            continue


def listen_for_command():
    print("Listening....")
    command = Recognizer().listen()
    Speak().speakout("Ok")
    get_cmd = ExtractCommand(command).Extract()
    ExecuteCommand(get_cmd).Execute()
    sleep(2)
    listen_for_keyword()


if __name__ == "__main__":
    listen_for_keyword()