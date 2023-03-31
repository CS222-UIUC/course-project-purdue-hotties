from pygame.math import Vector2

import pygame
import random

CELL_NUM = 25

# TODO: create identifiers for different types of items


class Item:
    def __init__(self, size_per_cell):
        # self.type = "apple" # placeholder for different types
        self.item_image = pygame.image.load(
            'resources/apple.png').convert_alpha()  # depends on item type
        self.size_per_cell = size_per_cell

        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.pos = Vector2(self.x, self.y)

    def randomize(self, snake_body):
        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
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
