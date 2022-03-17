class ExtractCommand:
    def __init__(self,cmd):
        self.cmd = cmd
    
    def Extract(self):
        if "close" in self.cmd:
            return "exit"
        else:
            return f"{self.cmd}"
