from lib.snake import Snake
from lib.item import Item
from lib.map import Map
from pygame.math import Vector2

import pygame
import sys

# global variables
SIZE_PER_CELL = 40
NUM_CELLS = 25
FONT_SIZE = 25
EVENT_CYCLE = 150  # ms
STARTING_SNAKE_LENGTH = 3

# styling options
BACKGROUND_COLOR = (163, 214, 28)
GRASS_COLOR = (158, 207, 31)
SCORE_TEXT_COLOR = (0, 0, 0)
SCORE_BOX_BG_COLOR = (167, 209, 61)
SCORE_BOX_OUTLINE_COLOR = (0, 0, 0)
SCORE_BOX_OUTLINE_WIDTH = 3

SCORE_COORDINATES = (SIZE_PER_CELL * (NUM_CELLS - 1), SIZE_PER_CELL)


# 03.23 menu development
# Screen dimensions
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
# 03.23 menu development


class Game():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(
            (NUM_CELLS * SIZE_PER_CELL, NUM_CELLS * SIZE_PER_CELL))
        self.screen.fill(BACKGROUND_COLOR)
        self.clock = pygame.time.Clock()
        pygame.time.set_timer(pygame.USEREVENT, EVENT_CYCLE)
        self.font = pygame.font.Font('resources/font.ttf', FONT_SIZE)

    def reset_game(self):
        self.score = 0
        self.snake = Snake(SIZE_PER_CELL)
        self.item = Item(SIZE_PER_CELL)

    def game_start(self):
        # 03.23 menu development
        font = pygame.font.Font(None, 36)
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.main_menu(font)
            # 03.23 menu developmen
            self.reset_game()
            self.game_loop()
            self.game_over_menu(font)

    def game_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.USEREVENT:
                    self.update()
                self.movement(event)
                if self.check_collision():
                    return

            self.draw_elements()
            pygame.display.update()
            self.clock.tick(60)

    def movement(self, event):
        if event.type == pygame.KEYDOWN:
            key = event.key
            if key == pygame.K_UP or key == pygame.K_w:
                if self.snake.direction.y != 1:
                    self.snake.direction = Vector2(0, -1)
            if key == pygame.K_RIGHT or key == pygame.K_d:
                if self.snake.direction.x != -1:
                    self.snake.direction = Vector2(1, 0)
            if key == pygame.K_DOWN or key == pygame.K_s:
                if self.snake.direction.y != -1:
                    self.snake.direction = Vector2(0, 1)
            if key == pygame.K_LEFT or key == pygame.K_a:
                if self.snake.direction.x != 1:
                    self.snake.direction = Vector2(-1, 0)

    # TODO: check for if snake hits the boundaries

    def check_collision(self):
        if self.item.pos == self.snake.body[0]:  # check for eating apple
            self.item.randomize(self.snake.body)
            self.snake.grow_snake()
            self.score += 1

        if self.snake.snake_collision():  # check snake collide
            return True

        return False

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

    def draw_elements(self):
        self.screen.fill(BACKGROUND_COLOR)
        self.draw_grass()
        self.snake.draw_snake(self.screen)
        self.item.draw_item(self.screen)
        self.draw_score()

    def update(self):
        self.snake.move_snake()

    def draw_score(self):
        score_text = str(self.score)
        score_font = self.font.render(score_text, True, SCORE_TEXT_COLOR)
        score_rect = score_font.get_rect(
            center=(SCORE_COORDINATES[0], SCORE_COORDINATES[1]))

        score_box_margin = 5
        item_rect = self.item.get_image().get_rect(
            midright=(score_rect.left, score_rect.centery))
        score_bg_rect = pygame.Rect(item_rect.left, item_rect.top, item_rect.width +
                                    score_rect.width + score_box_margin, item_rect.height)

        pygame.draw.rect(self.screen, SCORE_BOX_BG_COLOR, score_bg_rect)
        self.screen.blit(score_font, score_rect)
        self.screen.blit(self.item.get_image(), item_rect)
        pygame.draw.rect(self.screen, SCORE_BOX_OUTLINE_COLOR,
                         score_bg_rect, SCORE_BOX_OUTLINE_WIDTH)

    @staticmethod
    def get_map_size():
        return NUM_CELLS

    # 03.23 menu development

    def draw_text(self, FONT, text, color, x, y):
        surface = FONT.render(text, True, color)
        rect = surface.get_rect()
        rect.midtop = (x, y)
        SCREEN.blit(surface, rect)

    def main_menu(self, font):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            SCREEN.fill(BLACK)
            self.draw_text(font, "Snake Game", GREEN,
                           WIDTH // 2, HEIGHT // 2 - 100)
            self.draw_text(font, "Press ENTER to start",
                           WHITE, WIDTH // 2, HEIGHT // 2)
            self.draw_text(font, "Press Q to quit", WHITE,
                           WIDTH // 2, HEIGHT // 2 + 100)

            pygame.display.flip()

    def game_over_menu(self, font):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        return
                    if event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()

            SCREEN.fill(BLACK)
            self.draw_text(font, "Game Over", RED,
                           WIDTH // 2, HEIGHT // 2 - 100)
            self.draw_text(font, "Score: " + str(self.score), WHITE,
                           WIDTH // 2, HEIGHT // 2 - 50)
            self.draw_text(font, "Press ENTER to continue",
                           WHITE, WIDTH // 2, HEIGHT // 2)
            self.draw_text(font, "Press Q to quit", WHITE,
                           WIDTH // 2, HEIGHT // 2 + 100)

            pygame.display.flip()

    # 03.23 menu development
