from playsound import playsound
from threading import Thread
import simpleaudio as sa

class LoopSound:
    def __init__(self, soundFile):
        self.soundFile = soundFile
        self.looping = True
        self.loopThread = None
        self.playObj = None
        self.startLoop()

    def soundLoop(self):
        while self.looping:
            waveObj = sa.WaveObject.from_wave_file(self.soundFile)
            self.playObj = waveObj.play()
            self.playObj.wait_done()

    def startLoop(self):
        self.looping = True
        self.loopThread = Thread(target=self.soundLoop)
        self.loopThread.start()

    def stop(self):
        self.looping = False

    def stopImmediately(self):
        self.playObj.stop()
        self.looping = False