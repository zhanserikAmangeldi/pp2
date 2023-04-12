import pygame
import os, sys

_sound_library = {}

# def play_sound(path):
#     global _sound_library
#     sound = _sound_library.get(path)
#     if sound == None:
#         pygame.mixer.music.load(path)
#         _sound_library[path] = sound
#     pygame.mixer.music.play()

def next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]]
    pygame.mixer.music.stop()
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()
def previous_song():
    global _songs
    _songs = _songs[-1:] + _songs[:-1]
    pygame.mixer.music.stop()
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()


pygame.init()

screen = pygame.display.set_mode((400, 300))

s = 0


_songs = ['music/sound1.mp3', 'music/sound2.mp3', 'music/sound3.mp3', 'music/sound4.mp3', 'music/sound5.mp3']

play_music = True


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.mixer.music.pause()
            play_music = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            play_music = True
            pygame.mixer.music.unpause()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n and play_music:
            next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p and play_music:
            previous_song()

    pygame.display.flip()