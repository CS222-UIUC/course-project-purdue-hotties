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

        ### 03.23 menu development
        main_menu()
        ### 03.23 menu development

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

            ### 03.23 menu development

            # Update game state
            # ...

            # Check for game over
            # if game_over:
            #     game_over_menu()

            # Draw game
            # ...

            ### 03.23 menu development


    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP or key == pygame.K_w:
                if self.snake.direction.y != 1:
                    self.snake.direction = Vector2(0, -1)
                # print("up")
            if key == pygame.K_RIGHT or key == pygame.K_d:
                if self.snake.direction.x != -1:
                    self.snake.direction = Vector2(1, 0)
                # print("right")
            if key == pygame.K_DOWN or key == pygame.K_s:
                if self.snake.direction.y != -1:
                    self.snake.direction = Vector2(0, 1)
                # print("down")
            if key == pygame.K_LEFT or key == pygame.K_a:
                if self.snake.direction.x != 1:
                    self.snake.direction = Vector2(-1, 0)
                # print("left")

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



    ### 03.23 menu development

    # Screen dimensions
    WIDTH, HEIGHT = 800, 600
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Snake Game")

    # Colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)

    # Fonts
    FONT = pygame.font.Font(None, 36)

    def draw_text(text, color, x, y):
        surface = FONT.render(text, True, color)
        rect = surface.get_rect()
        rect.midtop = (x, y)
        SCREEN.blit(surface, rect)
    
    def main_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()

        SCREEN.fill(BLACK)
        draw_text("Snake Game", GREEN, WIDTH // 2, HEIGHT // 2 - 100)
        draw_text("Press ENTER to start", WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Press Q to quit", WHITE, WIDTH // 2, HEIGHT // 2 + 100)

        pygame.display.flip()

    def game_over_menu():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    game_loop()
                if event.key == pygame.K_q:
                    main_menu()

        SCREEN.fill(BLACK)
        draw_text("Game Over", RED, WIDTH // 2, HEIGHT // 2 - 100)
        draw_text("Press ENTER to play again", WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("Press Q to quit", WHITE, WIDTH // 2, HEIGHT // 2 + 100)

        pygame.display.flip()

    ### 03.23 menu development
