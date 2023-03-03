import item

class Map:
    def __init__(self) -> None:
        self.map_grid = [[item] * 25 for n in range(25)]