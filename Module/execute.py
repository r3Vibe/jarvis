class ExecuteCommand:
    def __init__(self,cmd):
        self.cmd = cmd

    def Execute(self):
        if "exit" == self.cmd:
            exit()
        else:
            Speak().speakout(self.cmd)
            print(self.cmd)



