import pygame
import time
import numpy as np

#Initialize pygame mixer
pygame.mixer.init()


# here we define notes from the "jingle bells "

notes= [
 (659, 0.4), (659, 0.4), (659, 0.4),
 (659, 0.4), (659, 0.4), (659, 0.4),
 (659, 0.4), (784, 0.4), (523, 0.4), (587, 0.4), (659, 0.4),
 (698, 0.4), (698, 0.4), (698, 0.4),(698, 0.4),
 (659, 0.4), (659, 0.4), (659, 0.4),(659, 0.4),
 (587, 0.4), (587, 0.4), (659, 0.4),(587, 0.4), (784, 0.4),
]


def generate_sound_array(frequency, duration, sample_rate=44100):
 t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
 wave = 0.5 * np.sin(2 * np.pi * frequency * t)
 sound_array = np.int16(wave * 32767)
 stereo_sound_array = np.column_stack((sound_array, sound_array))
 return stereo_sound_array


def play_note(frequency, duration):
 sound_array = generate_sound_array(frequency, duration)
 sound = pygame.sndarray.make_sound(sound_array)
 sound.play()
 time.sleep(duration)
 pygame.mixer.stop()


# Main loop to play the tune
print("Playing Jingle Bells...")
for note in notes:
    frequency, duration = note
    play_note(frequency, duration)

print("Tune finished!")
