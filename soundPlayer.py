from loopSound import LoopSound
from playsound import playsound
from glob import glob

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
                playsound(audioFiles[0])
        else:
            print("No sound file found")


    def testingDriver(self):
        lineIn = input("Input file name: ")
        while lineIn != "q":
            inputs = lineIn.split(" ")
            #TODO Validate inputs
            if inputs[0] == "/" : 
                for sound in self.loopingSounds:
                    sound.stop()
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
        for sound in self.loopingSounds:
            sound.stop()

if __name__ == "__main__":
    soundPlayer = SoundPlayer()
    soundPlayer.testingDriver()
