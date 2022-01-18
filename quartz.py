from soundPlayer import SoundPlayer
from wave import Error as Wave_Error
import os

BASE_DIRECTORY = "./sounds/"

def getFile(soundName):
    """Given the name of the sound file, returns the full file from the 'sounds' directory"""
    path = os.path.join(os.path.curdir, 'sounds', soundName + '.wav')
    if os.path.exists(path):
        return path
    else:
        raise FileNotFoundError

def terminalDriver():
    """A driver for the audioPlayer through a terminal interface."""
    soundPlayer = SoundPlayer()
    lineIn = input("Input file name: ")
    while lineIn != 'q':
        inputs = lineIn.rsplit(" ", 1)
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
        except Wave_Error as wave_error:
            print(wave_error)
        except ValueError as e:
            print(e.args[0])
        lineIn = input()

    #Exiting
    soundPlayer.stopAll()

if __name__ == "__main__":
    terminalDriver()
