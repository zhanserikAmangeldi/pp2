import pygame, sys, datetime

def rotate(surface, angle):
    rotated_surface = pygame.transform.rotozoom(surface,-angle,1)
    rotated_rect = rotated_surface.get_rect(center=(320,240))
    return rotated_surface, rotated_rect


pygame.init()

clock = pygame.time.Clock()
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))

mickey = pygame.image.load('mickey.jpg')
hand_minute = pygame.image.load('hand_minute.png')
hand_second = pygame.image.load('hand_second.png')


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')

    angle_min = datetime.datetime.now().minute

    angle_hour = datetime.datetime.now().second

    rotated_surface_minute, rotated_rect_minute = rotate(hand_minute, angle_min * 6)

    rotated_surface_second, rotated_rect_second = rotate(hand_second, angle_hour * 6)

    screen.blit(mickey,(0,0))
    screen.blit(rotated_surface_minute, rotated_rect_minute)
    screen.blit(rotated_surface_second, rotated_rect_second)
    print(rotated_rect_second.topleft)
    pygame.display.update()
    clock.tick(60)