class ExtractCommand:
    def __init__(self,cmd):
        self.cmd = cmd
    
    def Extract(self):
        if "close" in self.cmd or "quit" in self.cmd or "exit" in self.cmd or "turn of" in self.cmd or "shut down" in self.cmd:
            return "exit"
        elif "tell me a joke" in self.cmd or "say something funny" in self.cmd or "joke" in self.cmd or "funny" in self.cmd or "make me laugh" in self.cmd or "tell me something funny" in self.cmd:
            return "joke"
        elif "tell me about" in self.cmd or "search wikipedia about" in self.cmd:
            command = "wiki"
            if "tell me about" in self.cmd:
                parameters = self.cmd.split("tell me about")[1]
            elif "search wikipedia about" in self.cmd:
                parameters = self.cmd.split("search wikipedia about")[1]
            return [command,parameters]
        elif "start steam" in self.cmd:
            return "steam"
        elif "start uplay" in self.cmd:
            return "uplay"
        elif "start torrent" in self.cmd:
            return "torrent"
        elif "start excel" in self.cmd:
            return "excel"
        elif "start word" in self.cmd:
            return "word"
        elif "take note" in self.cmd:
            return "notes"
        else:
            return f"{self.cmd}"
