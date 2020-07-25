import pygame 
from pygame.locals import *

class A_star():
    def __init__(self):
        self.nodes_list = []
        self.start = (0, 0)
        self.end = (0, 0)

    def update_start(self):
        self.start = (user_interface.start[0] // 20, user_interface.start[1] // 20)

    def update_end(self):
        self.end = (user_interface.end[0] // 20, user_interface.end[1] // 20)

    def update_list(self, coord):
        self.nodes_list.append((coord[0] // 20, coord[1] // 20)) 

class UserInterface():
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()
        pygame.display.set_caption("A* pathfinding algorithm")
        self.running = True 
        self.start = (0, 0)
        self.end = (0, 0)
        self.obstacles_list = []
        self.algorithm = A_star()
        self.initialized = 0 # initialized when 
        # self.initialized == 2 (starting and ending node
        # where chosen) 

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and self.initialized < 2:
                if event.button == 1 and self.initialized < 2:
                    coord = pygame.mouse.get_pos()
                    self.obstacles_list.append(coord)
                    self.algorithm.update_list(coord)
                elif event.button == 3 and self.initialized == 0:
                    self.start = pygame.mouse.get_pos()
                    self.initialized += 1
                    self.algorithm.update_start()
                elif event.button == 3 and self.initialized == 1:
                    self.end = pygame.mouse.get_pos()
                    self.initialized += 1
                    self.algorithm.update_end()

    def drawNodes(self):
        l = self.algorithm.nodes_list
        s = self.algorithm.start
        e = self.algorithm.end
        for c in l:
            pygame.draw.rect(self.window, (0, 0, 0), (c[0] * 20, c[1] * 20, 20, 20))
        if self.initialized >= 1:
            pygame.draw.rect(self.window, (0, 255, 0), (s[0] * 20, s[1] * 20, 20, 20))
        if self.initialized == 2:
            pygame.draw.rect(self.window, (255, 0, 0), (e[0] * 20, e[1] * 20, 20, 20))

    def render(self):
        self.window.fill((255, 255, 255))
        # draw grid
        for i in range(1, 30):
            # 20 cases 
            pygame.draw.line(self.window, (0, 0 ,0), (0, 20 * i), (600, 20 * i), 3)
            pygame.draw.line(self.window, (0, 0, 0), (20 * i, 0), (20 * i, 600), 3)
        self.drawNodes()
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
user_interface.run()
pygame.quit()
