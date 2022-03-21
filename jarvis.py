# from Module import recognizer,execute,extractor,speaker
from glob import glob
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
            listen_for_command()
        else:
            print(keyw)
            continue


global listen_iter
listen_iter = 0

def listen_for_command():
    global listen_iter
    print("Listening....")
    Speak().speakout("Yes?")
    command = Recognizer().listen()
    listen_iter += 1
    if command == "false" and listen_iter < 5:
        Speak().speakout("Cannot Understand. Please Repeat after 2 seconds.")
        sleep(2)
        listen_for_command()
    elif command == "false" and listen_iter > 5:
        Speak().speakout("Script Restart.")
        sleep(2)
        listen_for_keyword()
    else:
        Speak().speakout("Ok")
        get_cmd = ExtractCommand(command).Extract()
        if type(get_cmd) == list:
            if get_cmd[0] == "wiki":
                ExecuteCommand(get_cmd[0]).SearchWiki(get_cmd[1])
                sleep(2)
                listen_for_keyword()
            if get_cmd[0] == "app":
                ExecuteCommand(get_cmd[0]).StartApp(get_cmd[1])
                sleep(2)
                listen_for_keyword()
        else:
            ExecuteCommand(get_cmd).Execute()
            sleep(2)
            listen_for_keyword()


if __name__ == "__main__":
    listen_for_keyword()