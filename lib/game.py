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
                pygame.display.update()

    # def movement(): 
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()
    #         if event.type == SCREEN_UPDATE:
    #             main_game.update()
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_UP:
    #                 if main_game.snake.direction.y != 1:
    #                     main_game.snake.direction = Vector2(0,-1)
    #             if event.key == pygame.K_RIGHT:
    #                 if main_game.snake.direction.x != -1:
    #                     main_game.snake.direction = Vector2(1,0)
    #             if event.key == pygame.K_DOWN:
    #                 if main_game.snake.direction.y != -1:
    #                     main_game.snake.direction = Vector2(0,1)
    #             if event.key == pygame.K_LEFT:
    #                 if main_game.snake.direction.x != 1:
    #                     main_game.snake.direction = Vector2(-1,0)





if __name__ == "__main__":
    pass