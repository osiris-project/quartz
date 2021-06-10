from threading import Thread
import simpleaudio as sa

class LoopSound:
    """
    A class to keep track of a looping sound. 
    Automatically creates a new thread when starting the loop to keep it playing 
    without interrupting any other functionality.
    """
    def __init__(self, soundFile, soundName):
        self.soundFile = soundFile
        self.soundName = soundName
        self.looping = True
        self.loopThread = None
        self.playObj = None
        self.startLoop()

    def soundLoop(self):
        """Main loop for a looping sound."""
        while self.looping:
            waveObj = sa.WaveObject.from_wave_file(self.soundFile)
            self.playObj = waveObj.play()
            self.playObj.wait_done()

    def startLoop(self):
        """Starts the sound playing on loop."""
        self.looping = True
        self.loopThread = Thread(target=self.soundLoop)
        self.loopThread.start()

    def stop(self):
        """Stops the sound after it completes its current loop."""
        self.looping = False

    def stopImmediately(self):
        """Stops sound immediately"""
        self.playObj.stop()
        self.looping = False

    def getSoundName(self):
        return self.soundName