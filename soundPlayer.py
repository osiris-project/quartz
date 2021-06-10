from loopSound import LoopSound
from glob import glob
import simpleaudio as sa

class SoundPlayer:
    """
    A class to handle playing sound effects given their names
    Also handles stopping playing sounds with functionality to handle looping audio.
    """
    def __init__(self):
        self.loopingSounds = []


    def playSound(self, soundName, looping=False):
        """
        Given a sound effect name, and bool for whether or not the sound should be looping, 
        searches for the sound under the 'sound' directory, and plays it accordingly.
        """
        baseDirectory = "./sounds/"
        audioFiles = glob(baseDirectory + "**/*" + soundName + "*", recursive=True)
        #TODO: Check for correct file type
        #TODO: Figure out the "Weird sample rates are not supported."
        """
        The following sample rates are allowed (though not necessarily guaranteed to be supported on your platform/hardware): 
        8, 11.025, 16, 22.05, 32, 44.1, 48, 88.2, 96, and 192 kHz.
        """
        if len(audioFiles) > 0:
            if looping:
                self.loopingSounds.append(LoopSound(audioFiles[0], soundName))
            else:
                waveObj = sa.WaveObject.from_wave_file(audioFiles[0])
                waveObj.play()
        else:
            print("No sound file found")

    def stopRepeating(self, soundName):
        """Stops given currently repeating sound after it has finished playing its current loop"""
        for sound in self.loopingSounds:
            if soundName == sound.getSoundName():
                sound.stop()

    def stopAll(self):
        """Immediately stops all playing sounds, including looping."""
        sa.stop_all()
        for sound in self.loopingSounds:
            sound.stopImmediately()
    

    def stopAllRepeating(self):
        """Stops all currently repeating sounds after they have finished playing their current loop"""
        for sound in self.loopingSounds:
            sound.stop()
