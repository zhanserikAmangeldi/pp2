import sys, pygame
from pygame.locals import *

'''
draw_item класс, который создает объект для разные слоев к примеру здесь есть 3 слоя, это work, paint и для font.
work - хранить в себе временные  "рисунки", к примеру, границы разных фигур, которые появляются при зажатий ЛКМ
paint - хранить постоянные рисунки
font - описание состояний мыши, и других элементов
'''
class draw_item:

    def __init__(self):
        self.surface = None
        self.left = 0
        self.top = 0

    def add(self, surface, left, top):
        self.surface = surface
        self.left = left
        self.top = top

class Palitra():
    def __init__(self, pos, width, height, color, paint):
        self.color = color
        self.paint = paint
        self.top_rect = pygame.Rect((pos), (width, height))
        self.top_color = color

    def draw(self):
        pygame.draw.rect(self.paint.paint_canvas, self.color, self.top_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.paint.positions = []
                print(1)
                self.paint.color = self.color
class Button():
    def __init__(self, pos, img, name, paint):
        self.paint = paint
        self.name = name
        self.img = pygame.image.load(img)
        self.top_rect = pygame.Rect((pos), (32, 32))

    def draw(self):
        pygame.draw.rect(self.paint.paint_canvas, 'black', self.top_rect)
        self.paint.paint_canvas.blit(self.img, self.top_rect)
        self.click()

    def click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:



                self.paint.positions = []
                print(1)
                print(self.name)
                self.paint.draw_tool = self.name
'''
Класс отвечает за всю программу, там храняться все данные
'''
class paint:
    def __init__(self):
        pygame.init()

        self.BLACK = 0, 0, 0
        self.WHITE = 255, 255, 255
        self.GREY = 100, 100, 100
        self.QUIT = False
        self.mousebutton = None
        self.mousedown = False
        self.mouse_buttons = ['Left Button', 'Middle Button', 'Right Button', 'Wheel up', 'Wheel down']
        self.draw_list = []
        self.mouse_x = self.mouse_y = 0
        self.draw_tool = 'Line'
        self.drawstart_x = -1
        self.drawend_x = -1
        self.drawstart_y = -1
        self.drawend_y = -1
        self.draw_toggle = False
        self.color = 0, 0, 255
        self.positions = []
        self.oldpositions = []
        self.radiusofdraw = 15
        self.points = []
        self.initialize()
        self.colors = [(255, 0, 0), (255, 128, 0), (255, 255, 0), (128, 255, 0), (0, 255, 0), (0, 255, 128), (0, 255, 255), (0, 128, 255), (0, 0, 255)]
        self.tools_img = ['icon/erase.png', 'icon/free_eraser.png', 'icon/marker.png', 'icon/line.png', 'icon/circle.png',
                          'icon/square.png', 'icon/rectangle.png', 'icon/rhombus.png', 'icon/triangle.png', 'icon/rec_triangle.png']
        self.name_of_tools = ['Eraser', 'Free Eraser', 'Draw', 'Line', 'Circle', 'Square', 'Rectangle', 'Rhombus',
                              'Equilateral Triangle', 'Right Triangle']
    # Отвечает за размеры экрана и слой
    def initialize(self):
        self.screen_width = 1000
        self.screen_height = 800
        self.screen_size = (self.screen_height, self.screen_height)
        self.screen = pygame.display.set_mode(self.screen_size)

        self.canvas = pygame.Surface((self.screen_width, self.screen_height))

        self.work_canvas = pygame.Surface((self.screen_width, self.screen_height))
        self.work_canvas.set_colorkey(self.BLACK)

        self.paint_canvas = pygame.Surface((self.screen_width, self.screen_height))

    def crosshair(self):  # создан, чтобы видеть границы ластика(Free Eraser)
        pos = self.mouse_x, self.mouse_y
        self.work_canvas.fill(self.BLACK)
        pygame.draw.circle(self.work_canvas, (self.WHITE), pos, self.radiusofdraw + 2, 1)
        self.draw_tool_template()

    # элементы круга
    def radius(self, rectangle):
        x1, y1, x2, y2 = rectangle
        x = (x2 - x1)
        y = (y2 - y1)
        if x >= y:
            rad = x
        else:
            rad = y
        if rad < 3:
            rad = 3
        return rad / 2

    def center(self, rectangle):
        x1, y1, x2, y2 = rectangle
        x = abs(x2 - x1)
        y = abs(y2 - y1)
        x1 += x / 2
        y1 += y / 2
        return (x1, y1)

    def draw_circle_template(self):
        '''
        Функция для рисования круга
        При зажатий лкм сохраняет местоположение мышки,
        и отпускание сохраняет коорды конечной точке,
        после этого рисует круг

        !!!! Следующий функций у которых в названиях пресутсвуют слово template, работают так же как и эта функция
             Просто будут меняться фигуры, но есть некоторые особенные функций, где вместо обычного pygame.draw.{фигура}
             Используются pygame.draw.polygon(),
        '''
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.work_canvas.fill(self.BLACK)

            try:
                pygame.draw.circle(self.work_canvas, self.GREY,
                                   self.center((self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y)),
                                   self.radius((self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y)),
                                   1)
            except:
                pass

            self.draw_tool_template()


        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.circle(self.paint_canvas, self.color,
                                   self.center((self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y)),
                                   self.radius((self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y)), 2)
            except:
                pass

    def draw_square_template(self):

        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_x - self.drawstart_x)
            self.work_canvas.fill(self.BLACK)

            try:
                pygame.draw.rect(self.work_canvas, self.GREY,
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y), 2)
            except:
                pass

            self.draw_tool_template()


        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.rect(self.paint_canvas, (self.color),
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y), 2)
            except:
                pass

    def draw_equilateral_triangle_template(self):
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_x - self.drawstart_x)
            self.work_canvas.fill(self.BLACK)
            first = self.drawstart_x + (self.drawend_x) / 2, self.drawstart_y
            second = self.drawstart_x, self.drawend_y + self.drawstart_y
            third = self.drawend_x + self.drawstart_x, self.drawend_y + self.drawstart_y
            self.points = [first, second, third]
            try:
                pygame.draw.polygon(self.work_canvas, (self.GREY), self.points, 2)
            except:
                pass

            self.draw_tool_template()

        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.polygon(self.paint_canvas, (self.color), self.points, 2)
            except:
                pass

    def draw_right_triangle_template(self):

        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_y - self.drawstart_y)
            self.work_canvas.fill(self.BLACK)
            first = self.drawstart_x, self.drawstart_y
            second = self.drawstart_x, self.drawstart_y + self.drawend_y
            third = self.drawend_x + self.drawstart_x, self.drawend_y + self.drawstart_y
            self.points = [first, second, third]
            try:
                pygame.draw.polygon(self.work_canvas, (self.GREY), self.points, 2)
            except:
                pass

            self.draw_tool_template()

        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.polygon(self.paint_canvas, (self.color), self.points, 2)
            except:
                pass

    def draw_rhombus_template(self):

        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_y - self.drawstart_y)
            self.work_canvas.fill(self.BLACK)
            second = self.drawstart_x + self.drawend_x / 2, self.drawstart_y
            first = self.drawstart_x, self.drawstart_y + self.drawend_y / 2
            third = self.drawstart_x + self.drawend_x, self.drawstart_y + self.drawend_y / 2
            fourth = self.drawstart_x + self.drawend_x / 2, self.drawstart_y + self.drawend_y
            self.points = [first, second, third, fourth]

            try:
                pygame.draw.polygon(self.work_canvas, (self.GREY), self.points, 2)
            except:
                pass

            self.draw_tool_template()


        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.polygon(self.paint_canvas, (self.color), self.points, 2)
            except:
                pass

    def draw_rectangle_template(self):

        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_y - self.drawstart_y)
            self.work_canvas.fill(self.BLACK)

            try:
                pygame.draw.rect(self.work_canvas, (self.GREY),
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y), 2)
            except:
                pass

            self.draw_tool_template()


        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.rect(self.paint_canvas, (self.color),
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y), 2)
            except:
                pass

    def drawLineBetween(self, index, start, end, width, color_mode):
        c1 = max(0, min(255, 2 * index - 256))
        c2 = max(0, min(255, 2 * index))
        color = color_mode

        if color_mode == (0, 0, 255):
            color = (c1, c1, c2)
        elif color_mode == (255, 0, 0):
            color = (c2, c1, c1)
        elif color_mode == (0, 255, 0):
            color = (c1, c2, c1)

        dx = start[0] - end[0]
        dy = start[1] - end[1]
        iterations = max(abs(dx), abs(dy))

        for i in range(iterations):
            progress = 1.0 * i / iterations
            aprogress = 1 - progress
            x = int(aprogress * start[0] + progress * end[0])
            y = int(aprogress * start[1] + progress * end[1])
            try:
                pygame.draw.circle(self.paint_canvas, color, (x, y), width)
            except:
                self.positions = []
        self.draw_toggle = False
    def draw_line_template(self):
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y

            self.work_canvas.fill(self.BLACK)

            pygame.draw.line(self.work_canvas, (self.GREY),
                             (self.drawstart_x, self.drawstart_y),
                             (self.drawend_x, self.drawend_y), 1)

            self.draw_tool_template()

        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            pygame.draw.line(self.paint_canvas, (self.color),
                             (self.drawstart_x, self.drawstart_y),
                             (self.drawend_x, self.drawend_y),
                             2)

    '''Беря коорды начальной точки и конечной, он создает несколько темных кругов с определенным интервалом'''
    def free_eraser(self, i, start, end, width):
        self.draw_toggle = False
        if self.mousedown and self.mousebutton == 3:
            dx = start[0] - end[0]
            dy = start[1] - end[1]
            iterations = max(abs(dx), abs(dy))

            for i in range(iterations):
                progress = 1.0 * i / iterations
                aprogress = 1 - progress
                x = int(aprogress * start[0] + progress * end[0])
                y = int(aprogress * start[1] + progress * end[1])
                pygame.draw.circle(self.paint_canvas, self.BLACK, (x, y), width)
    # Просто стирает прямоугольную область
    def eraser_template(self):
        if self.draw_toggle == False and self.mousedown and self.mousebutton == 1:
            self.drawstart_x = self.mouse_x
            self.drawstart_y = self.mouse_y
            self.drawend_x = self.mouse_x
            self.drawend_y = self.mouse_y
            self.draw_toggle = True
        elif self.draw_toggle == True and self.mousedown and self.mousebutton == 1:
            self.drawend_x = abs(self.mouse_x - self.drawstart_x)
            self.drawend_y = abs(self.mouse_y - self.drawstart_y)
            self.work_canvas.fill(self.BLACK)

            try:
                pygame.draw.rect(self.work_canvas, (self.GREY),
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y), 2)
            except:
                pass

            self.draw_tool_template()


        elif self.draw_toggle == True and not self.mousedown and self.mousebutton == 1:
            self.draw_toggle = False
            try:
                pygame.draw.rect(self.paint_canvas, (self.BLACK),
                                 pygame.Rect(self.drawstart_x, self.drawstart_y, self.drawend_x, self.drawend_y))
            except:
                pass

    '''
    Отвечает за сохранение данных с мышки, призыв функций отрисовок
    '''
    def mouse_handler(self, events):

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mousedown = True
                self.mousebutton = event.button
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mousedown = False
                self.mousebutton = event.button
            elif event.type == MOUSEMOTION:
                position = event.pos
                self.positions += [position]
                self.positions = self.positions[-256:]
            self.mouse_x, self.mouse_y = pygame.mouse.get_pos()

        if self.draw_tool == 'Line':
            self.draw_line_template()
        if self.draw_tool == 'Circle':
            self.draw_circle_template()
        if self.draw_tool == 'Rectangle':
            self.draw_rectangle_template()
        if self.draw_tool == 'Rhombus':
            self.draw_rhombus_template()
        if self.draw_tool == 'Square':
            self.draw_square_template()
        if self.draw_tool == 'Equilateral Triangle':
            self.draw_equilateral_triangle_template()
        if self.draw_tool == 'Right Triangle':
            self.draw_right_triangle_template()
        if self.draw_tool == 'Eraser':
            self.eraser_template()
        if self.draw_tool == 'Draw':
            i = 0
            while i < len(self.positions) - 1:
                self.drawLineBetween(i, self.positions[i], self.positions[i + 1], self.radiusofdraw, self.color)
                i += 1
        if self.draw_tool == 'Free Eraser':
            self.crosshair()
            i = 0
            while i < len(self.positions) - 1:
                self.free_eraser(i, self.positions[i], self.positions[i + 1], self.radiusofdraw)
                i += 1
        self.show_colors()
        self.show_tool()
        self.show_mousestate()

    # отвечает за текст и как он будет отображаться
    def show_mousestate(self):
        if self.mousebutton and self.mousedown:
            info = "ESC to quit, L for lines, C for Circles"
            info = "    Mouse: " + str(self.mouse_buttons[self.mousebutton - 1])
        else:
            info = "ESC to quit, L for lines, C for Circles"

        info += "   Mouse X= " + str(self.mouse_x) + " Y= " + str(self.mouse_y)
        info += " LeftButtonDown: " + str(self.draw_toggle)
        info += " Radius: " + str(self.radiusofdraw)

        font = pygame.font.Font(None, 20)
        textimg = font.render(info, True, self.WHITE)

        item = draw_item()
        item.add(textimg, 10, 10)
        self.draw_list.append(item)
    def show_colors(self):
        colors = []
        x = 40
        for color in self.colors:
            colors += [Palitra((x, 700), 30, 25, color, self)]
            x += 30

        for color in colors:
            color.draw()
    def show_tool(self):
        tools = []
        x = 10
        i = 0
        for tool in self.tools_img:
            tools += [Button((x, 20), tool, self.name_of_tools[i], self)]
            x += 40
            i += 1

        for tool in tools:
            tool.draw()
    # отвечает за предпросмотр нарисованного
    def draw_tool_template(self):
        item = draw_item()
        item.add(self.work_canvas, 0, 0)
        self.draw_list.append(item)

    # сохрняет нарисованное на полотне
    def canvas_draw(self):
        self.canvas.fill(self.BLACK)

        self.canvas.blit(self.paint_canvas, (0, 0))

        for i in self.draw_list:
            self.canvas.blit(i.surface, (i.left, i.top))

    #  отображает полотно
    def draw(self):
        self.canvas_draw()
        self.screen.blit(self.canvas, (0, 0))

    # очищает лист с рисунками чтобы они не рисовались бесконечно
    def clear(self):
        self.draw_list = []

    def run(self):

        while 1:
            self.clear()

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.QUIT = 1
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.QUIT = 1
                    if event.key == K_l:
                        self.draw_tool = 'Line'
                    if event.key == K_c:
                        self.draw_tool = 'Circle'
                    if event.key == K_r:
                        self.draw_tool = 'Rectangle'
                    if event.key == K_r and pygame.key.get_mods() & KMOD_CAPS:
                        self.draw_tool = 'Rhombus'
                    if event.key == K_s:
                        self.draw_tool = 'Square'
                    if event.key == K_t:
                        self.draw_tool = 'Equilateral Triangle'
                    if event.key == K_t and pygame.key.get_mods() & KMOD_CAPS:
                        self.draw_tool = 'Right Triangle'
                    if event.key == K_e:
                        self.draw_tool = 'Eraser'
                    if event.key == K_e and pygame.key.get_mods() & KMOD_SHIFT:
                        self.positions = []
                        self.draw_tool = 'Free Eraser'
                    if event.key == K_d:
                        self.positions = []
                        self.draw_tool = 'Draw'
                    if event.key == K_r and pygame.key.get_mods() & KMOD_CTRL:
                        self.color = 255, 0, 0
                    if event.key == K_g and pygame.key.get_mods() & KMOD_CTRL:
                        self.color = 0, 255, 0
                    if event.key == K_b and pygame.key.get_mods() & KMOD_CTRL:
                        self.color = 0, 0, 255

                # отвечает за изминения радиуса
                if event.type == MOUSEWHEEL:
                    if 2 < self.radiusofdraw < 199:
                        if self.draw_tool == 'Free Eraser':
                            self.positions = []
                        if event.y == 1 and self.radiusofdraw != 200:
                            self.radiusofdraw += 1
                        if event.y == -1 and self.radiusofdraw - 1 != 2:
                            self.radiusofdraw -= 1

            # условие выхода из программы
            if self.QUIT:
                pygame.quit()
                sys.exit()

            self.mouse_handler(events)

            # отрисовка
            self.draw()

            pygame.display.flip()


# запуск кода
mypaint = paint()
mypaint.run()
