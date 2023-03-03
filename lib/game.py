from lib.snake import Snake
from lib.item import Item
from lib.map import Map

import pygame
import sys

# global variables
SIZE_PER_CELL = 40
NUM_CELLS = 25
BACKGROUND_COLOR = (163, 214, 28)
GRASS_COLOR = (158, 207, 31)


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (NUM_CELLS * SIZE_PER_CELL, NUM_CELLS * SIZE_PER_CELL))
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grass()
        self.snake = Snake(SIZE_PER_CELL)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.movement(event)
                pygame.display.update()
                self.snake.draw_snake(self.screen)

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

    def draw_grass(self):
        for row in range(NUM_CELLS):
            for col in range(NUM_CELLS):
                if row % 2 == 0 and col % 2 == 0:
                    grass_blk = pygame.Rect(
                        row * SIZE_PER_CELL, col * SIZE_PER_CELL, SIZE_PER_CELL, SIZE_PER_CELL)
                    pygame.draw.rect(self.screen, GRASS_COLOR, grass_blk)
                elif row % 2 != 0 and col % 2 != 0:
                    grass_blk = pygame.Rect(
                        row * SIZE_PER_CELL, col * SIZE_PER_CELL, SIZE_PER_CELL, SIZE_PER_CELL)
                    pygame.draw.rect(self.screen, GRASS_COLOR, grass_blk)

    @staticmethod
    def get_map_size():
        return NUM_CELLS
