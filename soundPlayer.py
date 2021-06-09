from loopSound import LoopSound
from playsound import playsound
from glob import glob

class SoundPlayer:
    def __init__(self):
        self.loopingSounds = []

    def playSound(self, fileName, looping=False):
        baseDirectory = "./sounds/"
        audioFiles = glob(baseDirectory + "**/*" + fileName, recursive=True)
        if len(audioFiles) > 0:
            if looping:
                self.loopingSounds.append(LoopSound(audioFiles[0]))
                print("create looping sound")
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
                print("Canceling sounds")
                for sound in self.loopingSounds:
                    sound.end()
            elif len(inputs) > 1:
                looping = False
                if str.lower(inputs[1]) == 'looping' or str.lower(inputs[1]) == 'loop': looping = True
                self.playSound(inputs[0], looping)
            else:
                self.playSound(inputs[0])
            lineIn = input()

if __name__ == "__main__":
    soundPlayer = SoundPlayer()
    soundPlayer.testingDriver()
