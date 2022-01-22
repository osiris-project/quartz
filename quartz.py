"""Holds all functions necessary to run soundplayer on terminal"""

import os
from wave import Error as Wave_Error
from soundPlayer import SoundPlayer

BASE_DIRECTORY = "./sounds/"

def get_file(sound_name):
    """Given the name of the sound file, returns the full file from the 'sounds' directory"""
    while len(sound_name) >= 3 and sound_name[:3] == '../':
        sound_name = sound_name[3:]
    if len(sound_name) > 0:
        if len(sound_name) > 3 and sound_name[-4:] != '.wav':
            sound_name += '.wav'
        path = os.path.join(BASE_DIRECTORY, sound_name)
        if os.path.exists(path) and os.path.isfile(path):
            return path
    raise FileNotFoundError

def terminal_driver():
    """A driver for the audioPlayer through a terminal interface."""
    sound_player = SoundPlayer()
    line_in = input("Input file name: ")
    while line_in != 'q':
        inputs = line_in.rsplit(" ", 1)
        try:
            if line_in == 'stop all repeating' :
                sound_player.stopAllRepeating()
            elif line_in == 'stop all':
                sound_player.stopAll()
            elif len(inputs) > 1:
                if str.lower(inputs[1]) == 'looping' or str.lower(inputs[1]) == 'loop':
                    sound_player.playSound(get_file(inputs[0]), True)
                elif str.lower(inputs[1]) == 'stop':
                    sound_player.stopRepeating(get_file(inputs[0]))
                else:
                    sound_player.playSound(get_file(line_in))
            else:
                sound_player.playSound(get_file(line_in))
        except FileNotFoundError:
            print("File not found")
        except Wave_Error as wave_error:
            print(wave_error)
        except ValueError as error:
            print(error.args[0])
        line_in = input()

    #Exiting
    sound_player.stopAll()

if __name__ == "__main__":
    terminal_driver()
