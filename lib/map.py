from lib.item import Item
from lib.snake import Snake
from pygame.math import Vector2

class Map:
    def __init__(self) -> None:
        self.map_grid = [[Item()] * 25 for n in range(25)]
        self.snake = Snake(self.surface, 2)
        # TODO: put snake in a random grid
         

    def tick(self):
        # head advances a grid, erase a tail
        # if the grid where the head is in contains an item:
        self.interact_with(Item())

    def interact_with(self, item: Item):
        if item.item_type() == "apple":
            self.grow_snake()
        elif item.item_type() == "posion":
            self.terminate()

    def grow_snake(self):
        # the rest of the body stays the same
        # while the head advances a grid
        self.snake.grow()

    def terminate(self):
        pass