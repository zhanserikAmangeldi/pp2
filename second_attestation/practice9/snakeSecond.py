import pygame, random, datetime

pygame.init()

# Чтобы сделать возможность начала игры заново я сделал из игру функцию,
# которую игрок вызывает, если после смерти он решить сыграть заново
def game():
    # Здесь я добавил константные занчения, как размер экрана,
    # цвет и разметка для header-а(поле где показывается набранные очки игрока и уровень)
    class Apple():
        global screen
        def __init__(self):
            self.weight = random.randint(1, 5)
            self.pos = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            self.spawn = True
        def updates(self):
            self.pos = (random.randint(1, screen.get_width() / 10 - 1) * 10, random.randint(10, screen.get_height() / 10 - 1) * 10)
            self.weight = random.randint(1, 5)
            self.lifetime = 10
    screen = pygame.display.set_mode((400, 500))
    SNAKE_COLOR = 'black'
    BG_COLOR = (183, 212, 168)
    APPLE_COLOR = 'black'
    HEADER_LINE_START = (0, 100)
    HEADER_LINE_END = (400, 100)

    a1 = Apple()

    clock = pygame.time.Clock()
    running = True
    score = 0
    speed = 1
    LIST_OF_LEVEL = ['easy', 'normal', 'hard', 'very hard', 'impossible', 'impossible x2', 'death']
    score_font = pygame.font.SysFont('lunchtime Doubly So', 32)

    # Здесь я прописал начальную позицию змей и добавил элемент который определять куда должен повернутся и движется змея
    change = 'left' # указывает куда должен повернутся
    direction = 'left' # показывает куда двигалась до этого змея и из-за change меняет направление
    # это сделанно чтобы змея не меняло свое направление на противоположное

    player_pos = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]] # вся змея

    # Cпециальный ивент для уменьшие время жизни яблока,
    # у меня в игре яблоко имеет "жизни" и этот ивент убирает одну единицу жизни
    # Чтобы яблоко исчезла
    minuslife = pygame.USEREVENT + 1
    pygame.time.set_timer(minuslife, 1000)

    while running:
        '''
        Игрок только меняет направление движения змей, а змея уже сама движется без остановки по направлению
        За счет такого способа, мы избегаем того что змея может направиться в противоположную сторону
        Из-за этого он просто бы бился бы об себя
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_KP_8:
                    change = 'up'
                if event.key == pygame.K_s or event.key == pygame.K_KP_2:
                    change = 'down'
                if event.key == pygame.K_a or event.key == pygame.K_KP_4:
                    change = 'left'
                if event.key == pygame.K_d or event.key == pygame.K_KP_6:
                    change = 'right'
            if event.type == minuslife:
                print(1)
                a1.lifetime -= 1
                if a1.lifetime == 0:
                    a1.updates()

        if direction != 'up' and change == 'down':
            direction = 'down'
        if direction != 'down' and change == 'up':
            direction = 'up'
        if direction != 'left' and change == 'right':
            direction = 'right'
        if direction != 'right' and change == 'left':
            direction = 'left'

        if direction == 'up':
            player_pos[1] -= 10
        if direction == 'down':
            player_pos[1] += 10
        if direction == 'left':
            player_pos[0] -= 10
        if direction == 'right':
            player_pos[0] += 10

        # Логика по которой яблоко респавниться после поедания
        while a1.spawn:
            a1.updates()
            if a1.pos not in snake:
                a1.spawn = False

        # Змея растёт постоянно, но только когда она съедает яблоко, она сохраняет свой размер
        # Съедания значить то что координаты головы змей и яблока совпали
        snake.insert(0, list(player_pos))

        if player_pos[0] == a1.pos[0] and player_pos[1] == a1.pos[1]:
            score += a1.weight
            a1.spawn = True
            speed = score // 4 + 1
        else:
            snake.pop()

        screen.fill(BG_COLOR)




        pygame.draw.line(screen, 'black', HEADER_LINE_START, HEADER_LINE_END, 1)

        # Условия при которых игрок проигрывает. Прерывается сама игра, и сразу же начинается следующий цикл
        if ((player_pos[0] < -5 or player_pos[0] > screen.get_width() - 5) or (
                player_pos[1] < 100 or player_pos[1] > screen.get_height() - 5)):
            break
        if player_pos in snake[1:]:
            break

        # Отрисовка элементов игры(змея, яблоко, показатели, четра для отделения игрового поля и показателей)
        for pos in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(a1.pos[0], a1.pos[1], 10, 10))
        screen.blit(score_font.render(f'Score: {score}', True, 'black'), (20, 38))
        if speed <= 7:
            screen.blit(score_font.render(f'Speed: {LIST_OF_LEVEL[speed - 1]}', True, 'black'), (20, 58))
        else:
            screen.blit(score_font.render(f'Speed: death', True, 'black'), (20, 58))
        pygame.display.update()

        clock.tick(5 + speed*2) # Изменение скорости змей

    # Цикл для меню выбора после проигрыша игрока
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game()
                if event.key == pygame.K_q:
                    running = False
        screen.fill(BG_COLOR)

        screen.blit(score_font.render('Press R for restart or Q for quit', True, 'black'), (35, 200))
        pygame.display.update()


game()

pygame.quit()
