from lib.item import Item
from pygame.math import Vector2

class Map:
    def __init__(self) -> None:
        self.map_grid = [[Item()] * 25 for n in range(25)]
