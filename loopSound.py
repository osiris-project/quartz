from playsound import playsound
from threading import Thread

class LoopSound:
    def __init__(self, soundFile):
        self.soundFile = soundFile
        self.looping = True
        self.loopThread = None
        self.startLoop()

    def soundLoop(self):
        while self.looping:
            playsound(self.soundFile)

    def startLoop(self):
        self.looping = True
        self.loopThread = Thread(target=self.soundLoop)
        self.loopThread.start()

    def stop(self):
        self.looping = False
        self.loopThread.join()