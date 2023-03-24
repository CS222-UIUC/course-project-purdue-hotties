from lib.snake import Snake
from lib.item import Item
from lib.map import Map
from pygame.math import Vector2

import pygame
import sys

# global variables
SIZE_PER_CELL = 40
NUM_CELLS = 25
BACKGROUND_COLOR = (163, 214, 28)
GRASS_COLOR = (158, 207, 31)
EVENT_CYCLE = 150  # ms


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (NUM_CELLS * SIZE_PER_CELL, NUM_CELLS * SIZE_PER_CELL))
        self.screen.fill(BACKGROUND_COLOR)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, EVENT_CYCLE)
        self.draw_grass()
        self.snake = Snake(SIZE_PER_CELL)
        # TODO: this should be a list of item in the future
        self.item = Item(SIZE_PER_CELL)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    self.update()
                self.movement(event)

            self.draw_elements()
            pygame.display.update()
            self.clock.tick(60)

    def is_collision (self.snake.body,self.item.pos):
            x1 = self.snake.body[1][1]
            x2 = self.item.pos[1]
            y1 = self.snake.body[1][2]
            y2 = self.item.pos[2]
            if x1 >= x2 and x1 < x2 + NUM_CELLS:
                if y1 >= y2 and y1 < y2 + NUM_CELLS:
                    return True
            return False
    

    def play(self):
        self.snake.walk()
        self.item.draw_item

        if self.is_collision(self.snake.body[1], self.item.pos):
            self.snake.grow
            self.item.draw_item


    def movement(self, event):
        running = True
        while running: 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    key = event.key
                    if key == pygame.K_UP or key == pygame.K_w:
                        if self.snake.direction.y != 1:
                            self.snake.direction = Vector2(0, -1)
                            running = False
                        # print("up")
                    if key == pygame.K_RIGHT or key == pygame.K_d:
                        if self.snake.direction.x != -1:
                            self.snake.direction = Vector2(1, 0)
                            running = False
                        # print("right")
                    if key == pygame.K_DOWN or key == pygame.K_s:
                        if self.snake.direction.y != -1:
                            self.snake.direction = Vector2(0, 1)
                            running = False
                        # print("down")
                    if key == pygame.K_LEFT or key == pygame.K_a:
                        if self.snake.direction.x != 1:
                            self.snake.direction = Vector2(-1, 0)
                            running = False
                        # print("left")
            self.play()
        

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

    # TODO: check for if snake hits the boundaries
    def draw_elements(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grass()
        self.snake.draw_snake(self.screen)
        self.item.draw_item(self.screen)

    def update(self):
        self.snake.move_snake()

    @staticmethod
    def get_map_size():
        return NUM_CELLS
