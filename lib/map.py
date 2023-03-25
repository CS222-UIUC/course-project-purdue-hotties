from lib.item import Item
from lib.snake import Snake
from pygame.math import Vector2
import random
CELL_NUM = 25
class Map:
    def __init__(self) -> None:
        self.map_grid = [[Item()] * 25 for n in range(25)]

        # TODO: put snake in a random grid
        self.x = random.randint(0, CELL_NUM - 1)
        self.y = random.randint(0, CELL_NUM - 1)
        self.snake = Snake(self.x, self.y)
         

    def tick(self):
        # head advances a grid, erase a tail
        # if the grid where the head is in contains an item:
        self.interact_with(Item())

    def interact_with(self, item: Item):
        if item.item_type() == "apple":
            self.grow_snake()
        elif item.item_type() == "posion":
            self.terminate()

    def terminate(self):
        pass