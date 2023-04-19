import pygame
import os, sys
_songs = []
for root, dirs, files in os.walk('music/'):
    for filename in files:
        direct = f'{root}/{filename}'
        print(direct)
        _songs += [direct]

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

play_music = False


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_g and not play_music:
                pygame.mixer_music.load(_songs[0])
                pygame.mixer.music.play()
                play_music = True
            if event.key == pygame.K_s:
                pygame.mixer.music.pause()
                play_music = False
            if event.key == pygame.K_c:
                play_music = True
                pygame.mixer.music.unpause()
            if event.key == pygame.K_n and play_music:
                next_song()
            if event.key == pygame.K_p and play_music:
                previous_song()

    pygame.display.flip()