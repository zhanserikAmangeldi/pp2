import pygame, sys, random, os
from pygame.locals import *


class Game:
    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT + 100))
        self.TITLESIZE = 10
        self.clock = pygame.time.Clock()
        self.game_start = False
        self.FONT = pygame.font.SysFont('Verdana', size=20)
        self.endgame_font = self.FONT.render('Press Q for quit or R for restart', True, 'black')
        self.endscene = False
        self.new_game()

    def new_game(self):
        if not self.game_start:
            self.wall = Wall(self)
            self.snake = Snake(self)
            self.food = Food(self)
            self.font = Font(self)
            self.game_start = True
        else:
            self.endscene = True
    def update(self):
        if not self.endscene:
            self.wall.update()
            self.snake.update()
            self.food.update()
            self.font.update()
        pygame.display.update()
        self.clock.tick(60)
    def draw(self):
        self.screen.fill((183, 212, 168))
        self.border()
        self.wall.draw()
        self.snake.draw()
        self.food.draw()
        self.font.draw()

    def check_event(self):
        if not self.endscene:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.snake.control(event)
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_q:
                        pygame.quit()
                        sys.exit()
                    if event.key == K_r:
                        self.endscene = False
                        self.game_start = False
                        self.new_game()
                        self.run()

    def border(self):
        pygame.draw.line(self.screen, 'black', (0, 500), (500, 500))

    def endgame(self):
        self.screen.fill('black')
        self.screen.fill((183, 212, 168))
        self.screen.blit(self.endgame_font, (self.WIDTH/2 - 165, self.HEIGHT/2))

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()
            if self.endscene:
                break
        while True:
            self.check_event()
            self.endgame()
            self.update()




class Wall:
    def __init__(self, game):
        self.game = game
        self.size = 10
        self.levels = self.level_downloader()
        self.level = 0
        self.levelischange = False
        self.score = 0
        self.safe_positions = []
        # print(self.rect_walls)
    def txt_to_list(self):
        walls = []
        with open(self.now, 'r') as file:
            for row in file:
                walls.append(list(row.rstrip()))
        return walls
    def coor_walls(self):
        rects = []
        rects2 = []
        for row_index, row in enumerate(self.walls):
            for col_index, col in enumerate(row):
                if col == '#':
                    rects += [(col_index * self.size, row_index * self.size)]
                if col == '*':
                    rects2 += [(col_index * self.size, row_index* self.size)]
        return rects, rects2
    def level_downloader(self):
        levelName = []
        for root, dirs, files in os.walk('level/'):
            for filename in files:
                direct = f'{root}/{filename}'
                print(direct)
                levelName += [direct]
        return levelName
    def update(self):
        if self.game.snake.score / 4 >= len(self.levels):
            return
        self.level = self.game.snake.score/4
        self.now = self.levels[int(self.level)]
        self.walls = self.txt_to_list()
        if self.game.snake.score == 0:
            self.rect_walls = self.coor_walls()
        elif self.game.snake.score%4 == 0 and self.game.snake.score != 0:
            self.levelischange = True
            self.rect_walls, self.safe_positions = self.coor_walls()
            if (self.game.snake.rect.x - 1, self.game.snake.rect.y - 1) in self.game.wall.rect_walls:
                self.game.snake.direction = pygame.math.Vector2(0, 0)
                x = random.choice(self.safe_positions)
                self.game.snake.rect.center = (x[0] + 5, x[1] + 5)
            self.levelischange = False
        else:
            self.rect_walls = self.coor_walls()


    def draw(self):
        try:
            for rect in self.rect_walls:
                pygame.draw.rect(self.game.screen, 'black', pygame.Rect(rect, (10, 10)), 4)
        except:
            pass



class Snake:
    def __init__(self, game):
        self.game = game
        self.size = game.TITLESIZE
        self.rect = pygame.rect.Rect([0, 0, self.size - 2, self.size - 2])
        self.rect.center = self.get_random_pos()
        self.direction = pygame.math.Vector2(0, 0)
        self.last_direction = 0
        self.step_delay = 100
        self.time = 0
        self.length = 1
        self.segments = []
        self.score = 0
    def control(self, event):
        if event.type == KEYDOWN:
            if event.key == K_w and [0, self.size] != self.last_direction:
                self.direction = pygame.math.Vector2(0, -self.size)
                self.last_direction = self.direction
            if event.key == K_a and [self.size, 0] != self.last_direction:
                self.direction = pygame.math.Vector2(-self.size, 0)
                self.last_direction = self.direction
            if event.key == K_s and [0, -self.size] != self.last_direction:
                self.direction = pygame.math.Vector2(0, self.size)
                self.last_direction = self.direction
            if event.key == K_d and [-self.size, 0] != self.last_direction:
                self.direction = pygame.math.Vector2(self.size, 0)
                self.last_direction = self.direction
    def update(self):
        self.check_wall()
        self.check_border()
        self.check_food()
        self.check_in_segments()
        self.move()
    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > 50:
            self.time = time_now
            return True
        return False
    def get_random_pos(self):
        return (random.randrange(self.size//2, self.game.WIDTH - self.size//2, self.size),
                random.randrange(self.size // 2, self.game.WIDTH - self.size//2, self.size))
    def move(self):
        if self.delta_time():
            self.rect.move_ip(self.direction)
            self.segments.append(self.rect.copy())
            self.segments = self.segments[-self.length:]
    def draw(self):
        for segment in self.segments:
            pygame.draw.rect(self.game.screen, 'black', segment)
    def check_border(self):
        if self.rect.left < 0 or self.rect.right > self.game.WIDTH:
            self.game.new_game()
        if self.rect.top < 0 or self.rect.bottom > self.game.HEIGHT:
            self.game.new_game()
    def check_food(self):
        if self.rect.center == self.game.food.rect.center:
            self.length += 1
            self.score += 1
            self.game.food.rect.center = self.game.food.get_random_pos()
    def check_in_segments(self):
        if len(self.segments) != len(set(segment.center for segment in self.segments)):
            self.game.new_game()
    def check_wall(self):
        if not self.game.wall.levelischange:
            print(self.game.wall.levelischange)
            if (self.rect.x - 1, self.rect.y - 1) in self.game.wall.rect_walls:
                self.game.new_game()
class Food:
    def __init__(self, game):
        self.game = game
        self.size = game.TITLESIZE
        self.rect = pygame.rect.Rect([0, 0, self.size - 2, self.size - 2])
        self.rect.center = self.get_random_pos()
        self.step_delay = 10000
        self.time = 0
    def delta_time(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.time > self.step_delay:
            self.time = time_now
            return True
        return False
    def get_random_pos(self):
        self.time = pygame.time.get_ticks()
        pos = (random.randrange(self.size // 2, self.game.WIDTH - self.size // 2, self.size),
               random.randrange(self.size // 2, self.game.WIDTH - self.size // 2, self.size))
        while self.game.snake.rect.center == pos:
            pos = (random.randrange(self.size // 2, self.game.WIDTH - self.size // 2, self.size),
                   random.randrange(self.size // 2, self.game.WIDTH - self.size // 2, self.size))
        return pos
    def update(self):
        self.check_wall()
        if self.delta_time():
            self.rect.center = self.get_random_pos()
    def draw(self):
        pygame.draw.rect(self.game.screen, 'red', self.rect)

    def check_wall(self):

        if (self.rect.x - 1, self.rect.y - 1) in self.game.wall.rect_walls:
            self.rect.center = self.get_random_pos()
class Font:
    def __init__(self, game):
        pygame.font.init()
        self.game = game
        self.font_size = game.TITLESIZE * 3
        self.font = pygame.font.SysFont(name='Aria',size=36)
        self.score = f'Score: {self.game.snake.score}'
        self.level = f'Level: {int(self.game.wall.level)}'
        self.score_render = self.font.render(self.score, True, 'black')
        self.level_render = self.font.render(self.level, True, 'black')
    def draw(self):
        self.game.screen.blit(self.score_render, (self.font_size, self.game.screen.get_height() - self.font_size * 2.5))
        self.game.screen.blit(self.level_render, (self.font_size, self.game.screen.get_height() - self.font_size * 1.5))
    def update(self):
        self.score = f'Score: {self.game.snake.score}'
        self.level = f'Level: {int(self.game.wall.level)}'
        self.score_render = self.font.render(self.score, True, 'black')
        self.level_render = self.font.render(self.level, True, 'black')


pygame.init()
game = Game()
game.run()


