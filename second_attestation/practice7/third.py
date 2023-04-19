import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400, 400))

x = 20
y = 20


clock = pygame.time.Clock()
color = (0, 0, 255)
colors = [(255,0,0), (0, 255, 0), (0,0,0)]
i = 0
while True:
    for element in pygame.event.get():
        if element.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN] and y + 35 <= screen.get_height():
        y += 20
    if pressed[pygame.K_UP] and y - 35 >= 0:
        y -= 20
    if pressed[pygame.K_LEFT] and x - 35 >= 0:
        x -= 20
    if pressed[pygame.K_RIGHT] and x + 35 <= screen.get_width():
        x += 20
    if ( not x + 25 < screen.get_width() or not x + 35 >= screen.get_width() or not x - 35 <= 0 or  y - 35 <= 0 or  not y + 35 >= screen.get_height()):
        color = colors[i]
        i += 1
        if i == 3:
            i = 0
    screen.fill((0,0,0))
    pygame.draw.circle(screen, color, (x, y), 25 )

    pygame.display.flip()
    clock.tick(60)