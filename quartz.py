from soundPlayer import SoundPlayer
from glob import glob

BASE_DIRECTORY = "./sounds/"

def getFile(soundName):
    """Returns the first matching file from the given name in the 'sounds' directory"""
    audioFiles = glob(BASE_DIRECTORY + "**/*" + soundName + ".wav", recursive=True)
    if (len(audioFiles) < 1):
        raise FileNotFoundError
    return audioFiles[0]

def terminalDriver():
    """A driver for the audioPlayer through a terminal interface."""
    soundPlayer = SoundPlayer()
    lineIn = input("Input file name: ")
    while lineIn != 'q':
        inputs = lineIn.rsplit(" ", 1)
        #TODO Validate inputs
        try:
            if lineIn == 'stop all repeating' :
                soundPlayer.stopAllRepeating()
            elif lineIn == 'stop all':
                soundPlayer.stopAll()
            elif len(inputs) > 1:
                if str.lower(inputs[1]) == 'looping' or str.lower(inputs[1]) == 'loop':
                    soundPlayer.playSound(getFile(inputs[0]), True)
                elif str.lower(inputs[1]) == 'stop':
                    soundPlayer.stopRepeating(getFile(inputs[0]))
                else:
                    soundPlayer.playSound(getFile(lineIn))
            else:
                soundPlayer.playSound(getFile(lineIn))
        except FileNotFoundError:
            print("File not found")
        except ValueError:
            print("File has unsuported sample rate")
        lineIn = input()

    #Exiting
    soundPlayer.stopAll()

if __name__ == "__main__":
    terminalDriver()
