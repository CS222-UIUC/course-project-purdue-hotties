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
      
  
   def draw_item(self, screen):
       x_pos = int(self.x * self.size_per_cell)
       y_pos = int(self.y * self.size_per_cell)
       item_rect = pygame.Rect(x_pos, y_pos, self.size_per_cell, self.size_per_cell)
       screen.blit(self.apple, item_rect)

