from soundPlayer import SoundPlayer

def terminalDriver():
    """
    A driver for the audioPlayer through a terminal interface. 
    """
    soundPlayer = SoundPlayer()
    lineIn = input("Input file name: ")
    while lineIn != 'q':
        inputs = lineIn.rsplit(" ", 1)
        #TODO Validate inputs
        if lineIn == 'stop all repeating' :
            soundPlayer.stopAllRepeating()
        elif lineIn == 'stop all':
            soundPlayer.stopAll()
        elif len(inputs) > 1:
            if str.lower(inputs[1]) == 'looping' or str.lower(inputs[1]) == 'loop':
                soundPlayer.playSound(inputs[0], True)
            elif str.lower(inputs[1]) == 'stop':
                soundPlayer.stopRepeating(inputs[0])
            else:
                soundPlayer.playSound(lineIn)
        else:
            soundPlayer.playSound(lineIn)
        lineIn = input()

    #Exiting
    soundPlayer.stopAll()

if __name__ == "__main__":
    terminalDriver()
