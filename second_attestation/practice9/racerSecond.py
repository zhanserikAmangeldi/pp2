import pygame
import random
import time

pygame.init()

BACKGROUND = pygame.image.load('image/AnimatedStreet.png')
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 600))
speed = 5
score = 0
coins = 0

'''
Все классы являются спрайтами, это позволяет без сложных манипуляций
делать действия при столкновениях прямоугольников объектов за счет функции spritecollide/spritecollideany
Но здесь, я использую еще один аттрибут, чтобы проверить столкновение объектов, это pygame.spirt.collide_mask
В отличи от обычного, он работает более точно, потому что он сохраняет только непрозрачные пиксели объекта, а не всё

У каждого класса есть функция move, которая отвечает за движение объекта 
и поведений при столкновений с другими объектами
'''
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('image/Player.png')
        self.rect = self.img.get_rect(width=37)
        self.rect.center = (160,520)
        self.mask = pygame.mask.from_surface(self.img)
    def move(self):
        pressed_key = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_key[pygame.K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < screen.get_width():
            if pressed_key[pygame.K_RIGHT]:
                self.rect.move_ip(5,0)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('image/Enemy.png')
        self.rect = self.img.get_rect(width=42)
        self.rect.center = (random.randint(40, 360), 0)
        self.mask = pygame.mask.from_surface(self.img)
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if(self.rect.top > 600):
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.img = pygame.image.load('image/coin.png')
        self.rect = self.img.get_rect()
        self.rect.center = (random.randint(40, 360), random.randint(-100, 0))
        self.weight = random.randint(1,4)
        self.mask = pygame.mask.from_surface(self.img)
        self.coins_on_speed = 0

    def move(self):
        global coins, speed
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, 360), 0)
        elif pygame.sprite.spritecollide(self, player , False, pygame.sprite.collide_mask):
            self.coins_on_speed += 1
            if self.coins_on_speed >= 5:
                speed += 0.5
                self.coins_on_speed = 0
            coins += self.weight
            self.rect.top = 0
            self.rect.center = (random.randint(40,360), 0)
        elif pygame.sprite.spritecollideany(self, enemies, pygame.sprite.collide_mask):
            self.rect.center = (random.randint(40,360), 0)

        self.rect.move_ip(0, speed)


# создание и добавление объектов
p1 = Player()
e1 = Enemy()

player = pygame.sprite.Group()
player.add(p1)
coins_group = pygame.sprite.Group()
all_group = pygame.sprite.Group()
enemies = pygame.sprite.Group()
all_group.add(p1)
enemies.add(e1)
all_group.add(e1)
all_group.add(p1)

for i in range(5):
    c1 = Coin()
    coins_group.add(c1)
    all_group.add(c1)

running = True

# Это специальный ивент, который отвечает за ускорение игры по истечению 1 секунды(1000 миллисекунд)
inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)

# Шрифты
font = pygame.font.SysFont('Verdana', 40)
font_score = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game Over', True, 'black')


while running:
    for event in pygame.event.get():
        if event.type == inc_speed:
            speed += 0.5
        if event.type == pygame.QUIT:
            running = False
    # Вывод элементов на экран
    screen.blit(BACKGROUND, (0,0))
    score_view = font_score.render(f'{score}', True, 'black')
    coins_view = font_score.render(f'{coins}', True, 'black')
    screen.blit(score_view, (10,10))
    screen.blit(coins_view, (360,0))

    # Условие при котором игра знакончиться
    if pygame.sprite.spritecollide(p1, enemies, False, pygame.sprite.collide_mask):
        pygame.mixer.Sound('image/crash.wav').play()
        time.sleep(1)

        screen.fill('red')
        screen.blit(game_over, (75, 250))

        pygame.display.update()
        # Убирает все объекты
        for unite in all_group:
            unite.kill()
        time.sleep(2)
        running = False

    # Вывод на экран всех объектов
    for unite in all_group:
        unite.move()
        screen.blit(unite.img, unite.rect)

    pygame.display.update()
    clock.tick(60)

pygame.quit()