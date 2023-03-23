from pygame.math import Vector2

import pygame
import random

CELL_NUM = 25

# TODO: create identifiers for different types of items

class Item:
    def __init__(self, size_per_cell):
        # self.type = "apple" # placeholder for different types
        self.apple = pygame.image.load('resources/apple.png').convert_alpha()
        self.size_per_cell = size_per_cell


        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.pos = Vector2(self.x, self.y)
        
    
    def draw_item_util(self):
        x_pos = int(self.x * self.size_per_cell)
        y_pos = int(self.y * self.size_per_cell)
        item_rect = pygame.Rect(x_pos, y_pos, self.size_per_cell, self.size_per_cell)
        return (self.apple, item_rect)

    def draw_item(self, screen):
        asset, loc = self.draw_item_util()
        screen.blit(asset, loc)
        
    def item_type(self) -> str:
        return "item"

class Apple(Item):
    def __init__(self, size_per_cell):
        super().__init__(size_per_cell)

    def item_type(self) -> str:
        return "apple"
    
class Posion(Item):
    def __init__(self, size_per_cell):
        super().__init__(size_per_cell)
    
    def item_type(self) -> str:
        return "posion"