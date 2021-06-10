from loopSound import LoopSound
from playsound import playsound
from glob import glob
import simpleaudio as sa

class SoundPlayer:
    def __init__(self):
        self.loopingSounds = []

    def playSound(self, fileName, looping=False):
        baseDirectory = "./sounds/"
        audioFiles = glob(baseDirectory + "**/*" + fileName + "*", recursive=True)
        if len(audioFiles) > 0:
            if looping:
                self.loopingSounds.append(LoopSound(audioFiles[0]))
            else:
                waveObj = sa.WaveObject.from_wave_file(audioFiles[0])
                waveObj.play()
        else:
            print("No sound file found")


    def testingDriver(self):
        lineIn = input("Input file name: ")
        while lineIn != 'q':
            inputs = lineIn.split(" ")
            #TODO Validate inputs
            if lineIn == 'stop all repeating' :
                for sound in self.loopingSounds:
                    sound.stop()
            elif lineIn == 'stop all':
                sa.stop_all()
                for sound in self.loopingSounds:
                    sound.stopImmediately()
            elif len(inputs) > 1:
                if str.lower(inputs[1]) == 'looping' or str.lower(inputs[1]) == 'loop':
                    self.playSound(inputs[0], True)
                elif str.lower(inputs[1]) == 'stop':
                    for sound in self.loopingSounds:
                        if inputs[0] in sound.soundFile:
                            sound.stop()
            else:
                self.playSound(inputs[0])
            lineIn = input()

        #Exiting
        sa.stop_all()
        for sound in self.loopingSounds:
            sound.stopImmediately()

if __name__ == "__main__":
    soundPlayer = SoundPlayer()
    soundPlayer.testingDriver()
