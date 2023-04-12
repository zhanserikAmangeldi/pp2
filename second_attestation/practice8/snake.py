import pygame, random, sys

pygame.init()
# Чтобы сделать возможность начала игры заново я сделал из игру функцию,
# которую игрок вызывает, если после смерти он решить сыграть заново
def play():
    # Здесь я добавил константные занчения, как размер экрана,
    # цвет и разметка для header-а(поле где показывается набранные очки игрока и уровень)
    screen = pygame.display.set_mode((400, 500))
    SNAKE_COLOR = 'black'
    BG_COLOR = (183, 212, 168)
    APPLE_COLOR = 'black'
    HEADER_LINE_START = (0, 100)
    HEADER_LINE_END = (400, 100)

    clock = pygame.time.Clock()
    running = True


    apple = (random.randint(1, screen.get_width() / 10 - 1) * 10,
             random.randint(10, screen.get_height() / 10 - 1) * 10) # random spawn of apple
    apple_spawn = True  # чтобы было только одно яблоко
    score = 0
    speed = 1
    LIST_OF_LEVEL = ['easy','normal','hard','very hard', 'impossible', 'impossible x2', 'death'] # уровни сложности
    score_font = pygame.font.SysFont('lunchtime Doubly So', 32) # шрифт для показ очков и уровня сложности

    # Здесь я прописал начальную позицию змей и добавил элемент который определять куда должен повернутся и движется змея
    change = 'left' # указывает куда должен повернутся
    direction = 'left' # показывает куда двигалась до этого змея и из-за change меняет направление
    # это сделанно чтобы змея не меняло свое направление на противоположное

    player_pos = [220, 200] # голова
    snake = [[220, 200], [230, 200], [240, 200]] # вся змея

    while running:
        '''
        Игрок только меняет направление движения змей, а змея уже сама движется без остановки по направлению
        За счет такого способа, мы избегаем того что змея может направиться в противоположную сторону
        Из-за этого он просто бы бился бы об себя
        '''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change = 'up'
                if event.key == pygame.K_s:
                    change = 'down'
                if event.key == pygame.K_a:
                    change = 'left'
                if event.key == pygame.K_d:
                    change = 'right'

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
        while apple_spawn:
            apple = (
                random.randint(1, screen.get_width() / 10 - 1) * 10,
                random.randint(10, screen.get_height() / 10 - 1) * 10)
            if apple not in snake:
                apple_spawn = False


        # Змея растёт постоянно, но только когда она съедает яблоко, она сохраняет свой размер
        # Съедания значить то что координаты головы змей и яблока совпали
        snake.insert(0, list(player_pos))

        if player_pos[0] == apple[0] and player_pos[1] == apple[1]:
            score += 1
            apple_spawn = True
            speed = score // 4 + 1
        else:
            snake.pop()

        screen.fill(BG_COLOR)




        # Условия при которых игрок проигрывает. Прерывается сама игра, и сразу же начинается следующий цикл
        if ((player_pos[0] < -5 or player_pos[0] > screen.get_width() - 5) or (
                player_pos[1] < 100 or player_pos[1] > screen.get_height() - 5)):
            break
        if player_pos in snake[1:]:
            break


        # Отрисовка элементов игры(змея, яблоко, показатели, четра для отделения игрового поля и показателей)
        for pos in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(apple[0], apple[1], 10, 10))
        pygame.draw.line(screen, 'black', HEADER_LINE_START, HEADER_LINE_END, 1)
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
                    play()
                if event.key == pygame.K_q:
                    running = False
        screen.fill(BG_COLOR)

        screen.blit(score_font.render('Press R for restart or Q for quit', True, 'black'), (35, 200))


        pygame.display.update()

play()

pygame.quit()



