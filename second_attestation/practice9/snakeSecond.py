import pygame, random, datetime

pygame.init()
class Map:
    def __init__(self, ref, screen):
        self.screen = screen
        self.ref = ref
        self.size = 10
        self.coords = self.rect_coords()

    def rect_coords(self):
        with open(self.ref, 'r') as file:
            rects = []
            for row_index, row in enumerate(file):
                for col_index, col in enumerate(row):
                    if col == '#':
                        rects += [pygame.Rect(col_index * self.size, row_index * self.size + 100, 10, 10)]
            return rects
    def draw(self):
        try:
            for rect in self.coords:
                pygame.draw.rect(self.screen, 'black', rect, 4)
        except:
            pass
# Чтобы сделать возможность начала игры заново я сделал из игру функцию,
# которую игрок вызывает, если после смерти он решить сыграть заново
def game():
    # Здесь я добавил константные значения, как размер экрана,
    # цвет и разметка для header-а(поле где показывается набранные очки игрока и уровень)
    class Apple:
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
    level = 0
    a1 = Apple()

    clock = pygame.time.Clock()
    running = True
    score = 0
    score_font = pygame.font.SysFont('lunchtime Doubly So', 32)
    levels = [Map('level/level0.txt', screen),Map('level/level1.txt', screen),Map('level/level2.txt', screen),Map('level/level3.txt', screen),Map('level/level4.txt', screen)]

    # Здесь я прописал начальную позицию змей и добавил элемент который определять куда должен повернутся и движется змея
    change = 'left' # указывает куда должен повернутся
    direction = 'left' # показывает куда двигалась до этого змея и из-за change меняет направление
    # это сделанно чтобы змея не меняло свое направление на противоположное

    player_pos = [220, 200]
    snake = [[220, 200], [230, 200], [240, 200]] # вся змея

    # Cпециальный ивент для уменьшения время жизни яблока,
    # у меня в игре яблоко имеет "жизни" и этот ивент убирает одну единицу жизни
    # Чтобы яблоко исчезла
    minuslife = pygame.USEREVENT + 1
    pygame.time.set_timer(minuslife, 1000)


    level_change = False
    time_now = 0
    time_before = 0
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
            old_level = level
            level = score // 4
            if level > len(levels) - 1:
                level = len(levels) - 1
            if level > old_level:
                print(1)
                level_change = True
                time_before = pygame.time.get_ticks()
        else:
            snake.pop()
        if (a1.pos[0], a1.pos[1], 10, 10) in levels[level].coords:
            a1.spawn = True
        time_now = pygame.time.get_ticks()
        screen.fill(BG_COLOR)




        pygame.draw.line(screen, 'black', HEADER_LINE_START, HEADER_LINE_END, 1)

        # Условия при которых игрок проигрывает. Прерывается сама игра, и сразу же начинается следующий цикл
        if ((player_pos[0] < -5 or player_pos[0] > screen.get_width() - 5) or (
                player_pos[1] < 100 or player_pos[1] > screen.get_height() - 5)):
            break
        if level_change:
            if time_now - time_before > 2000:
                level_change = False
                if (player_pos[0], player_pos[1], 10, 10) in levels[level].coords:
                    break
        else:
            if (player_pos[0], player_pos[1], 10, 10) in levels[level].coords:
                break
        if a1.pos in levels[level].coords:
            a1.updates()
        if player_pos in snake[1:]:
            break

        # Отрисовка элементов игры(змея, яблоко, показатели, четра для отделения игрового поля и показателей)
        for pos in snake:
            pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(pos[0], pos[1], 10, 10))
        pygame.draw.rect(screen, APPLE_COLOR, pygame.Rect(a1.pos[0], a1.pos[1], 10, 10))
        screen.blit(score_font.render(f'Score: {score}', True, 'black'), (20, 38))
        levels[level].draw()
        pygame.display.update()

        clock.tick(15) # Изменение скорости змей

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