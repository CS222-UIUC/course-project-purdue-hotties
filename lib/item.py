from pygame.math import Vector2

import pygame
import random

# +------ cursor parking lot ------------+
# |				                         |
# |			                             |
# +--------------------------------------+


class Item:
    def __init__(self, size_per_cell, resource, cell_num):
        self.item_image = pygame.image.load(resource).convert_alpha()
        self.size_per_cell = size_per_cell
        self.cell_num = cell_num

        self.x = random.randint(0, self.cell_num - 1)
        self.y = random.randint(0, self.cell_num - 1)
        self.pos = Vector2(self.x, self.y)

    def randomize(self, snake_body):
        self.x = random.randint(0, self.cell_num - 1)
        self.y = random.randint(0, self.cell_num - 1)
        self.pos = Vector2(self.x, self.y)

        while self.pos in snake_body:
            self.randomize(snake_body)

    def draw_item_util(self):
        x_pos = int(self.x * self.size_per_cell)
        y_pos = int(self.y * self.size_per_cell)
        item_rect = pygame.Rect(
            x_pos, y_pos, self.size_per_cell, self.size_per_cell)
        return (self.item_image, item_rect)

    def draw_item(self, screen):
        asset, loc = self.draw_item_util()
        screen.blit(asset, loc)

    def get_image(self):
        return self.item_image


class Apple(Item):
    def __init__(self, size_per_cell, cell_num):
        super().__init__(size_per_cell, 'resources/apple.png', cell_num)


class Portal(Item):
    def __init__(self, size_per_cell, cell_num):
        super().__init__(size_per_cell, 'resources/portal.png', cell_num)
    
    def randomize(self, snake_body):
        self.x = random.randint(1, self.cell_num - 2)
        self.y = random.randint(1, self.cell_num - 2)
        self.pos = Vector2(self.x, self.y)

        while self.pos in snake_body:
            self.randomize(snake_body)

        
