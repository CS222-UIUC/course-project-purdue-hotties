from lib.snake import Snake
from lib.item import Item
from lib.map import Map

import pygame
import sys

class Game(): 
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
    
    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.movement(event)
                pygame.display.update()

    def movement(self, event): 
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP or key == pygame.K_w: 
                print("up")
            if key == pygame.K_RIGHT or key == pygame.K_d:
                print("right")
            if key == pygame.K_DOWN or key == pygame.K_s:
                print("down")                
            if key == pygame.K_LEFT or key == pygame.K_a:
                print("left")
