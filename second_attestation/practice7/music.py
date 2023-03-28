import pygame
import os
import random

def play_a_different_song():
    global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

def play_next_song():
    global _songs
    _songs = _songs[1:] + [_songs[0]] # move current song to the back of the list
    pygame.mixer.music.load(_songs[0])
    pygame.mixer.music.play()

_sound_library = {}
def play_sound(path):
    global _sound_library
    sound = _sound_library.get(path)
    if sound == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        sound = pygame.mixer.Sound(canonicalized_path)
        _sound_library[path] = sound
    sound.play()


pygame.init()

play_music= True

_songs = ['music/sound1.mp3', 'music/sound2.mp3', 'music/sound3.mp3', 'music/sound4.mp3', 'music/sound5.mp3']
_currently_playing_song = None



# effect = pygame.mixer.Sound('beep.wav')
# effect.play()


SONG_END = pygame.USEREVENT + 1

screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True

clock = pygame.time.Clock()


pygame.mixer.music.set_endevent(SONG_END)
play_next_song()

x = 30
y = 30


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            done = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue
        if event.type == pygame.KEYDOWN and event.key == pygame.K_n:
            play_next_song()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            pygame.mixer.music.stop()        
            play_music = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:   
            play_music = True
            play_next_song()
        if event.type == SONG_END:
            print("music end")
            if play_music:
                play_next_song()
    pressed = pygame.key.get_pressed()


    if pressed[pygame.K_UP]: y -= 3
    if pressed[pygame.K_DOWN]: y += 3 
    if pressed[pygame.K_LEFT]: x -= 3
    if pressed[pygame.K_RIGHT]: x += 3
    
    screen.fill((0,0,0))
    if is_blue: color = (0, 123, 255)
    else: color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x,y,60,60))

    pygame.display.flip()
    clock.tick(60)