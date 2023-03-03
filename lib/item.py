import random
from pygame.math import Vector2

CELL_NUM = 25

# TODO: create identifiers for different types of items

class Item:
    def __init__(self):
        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.pos = Vector2(self.x, self.y)