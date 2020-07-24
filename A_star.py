import pygame 
from pygame.locals import *

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
        self.initialized = 0 # initialized when 
        # self.initialized == 2 (starting and ending node
        # where chosen) 

    def processInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and self.initialized < 2:
                    self.obstacles_list.append(pygame.mouse.get_pos())
                if event.button == 3 and self.initialized == 0:
                    self.start = pygame.mouse.get_pos()
                    self.initialized += 1
                if event.button == 3 and self.initialized == 1:
                    self.end = pygame.mouse.get_pos()
                    self.initialized += 1

    def render(self):
        self.window.fill((255, 255, 255))
        # draw grid
        for i in range(1, 30):
            pygame.draw.line(self.window, (0, 0 ,0), (0, 20 * i), (600, 20 * i), 3)
            pygame.draw.line(self.window, (0, 0, 0), (20 * i, 0), (20 * i, 600), 3)
        pygame.display.update()

    def run(self):
        while self.running:
            self.processInput()
            self.render()
            self.clock.tick(60)

user_interface = UserInterface()
user_interface.run()
pygame.quit()
