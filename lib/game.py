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


### 03.23 menu development
# Screen dimensions
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
### 03.23 menu development


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
        
        self.font = pygame.font.Font('resources/font.ttf', FONT_SIZE)

        ### 03.23 menu development
        FONT = pygame.font.Font(None, 36)
        self.main_menu(FONT)
        ### 03.23 menu developmen

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
        
            ### 03.23 menu development

            # Update game state
            # ...

            # Check for game over
            # if game_over:
            #     game_over_menu()

            # Draw game
            # ...

            ### 03.23 menu development

    # TODO: check for if snake hits the boundaries
    def check_collision(self):
        if self.item.pos == self.snake.body[0]: # check for eating apple
            self.item.randomize(self.snake.body)
            self.snake.grow_snake()


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
        self.check_collision()

    def draw_score(self):
        score_text = str(len(self.snake.body) - STARTING_SNAKE_LENGTH)
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



    ### 03.23 menu development

    def draw_text(self, FONT, text, color, x, y):
        surface = FONT.render(text, True, color)
        rect = surface.get_rect()
        rect.midtop = (x, y)
        SCREEN.blit(surface, rect)
    
    def main_menu(self, FONT):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        self.game_loop()

            SCREEN.fill(BLACK)
            self.draw_text(FONT, "Snake Game", GREEN, WIDTH // 2, HEIGHT // 2 - 100)
            self.draw_text(FONT, "Press ENTER to start", WHITE, WIDTH // 2, HEIGHT // 2)
            self.draw_text(FONT, "Press Q to quit", WHITE, WIDTH // 2, HEIGHT // 2 + 100)

            pygame.display.flip()

    def game_over_menu(self):
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
