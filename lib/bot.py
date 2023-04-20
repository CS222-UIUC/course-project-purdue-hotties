from pygame import Vector2
# global variables
NUM_DIRE = 4

EMPTY = 0
SNAKE = 1
APPLE = 2

DIRE_LOOKUP = {
    0 : (0, -1), # UP
    1 : (-1, 0), # LEFT
    2 : (0, 1), # DOWN
    3 : (1, 0), # RIGHT
}

VECTOR_LOOKUP = { 
    (0, -1) : 0, # UP
    (-1, 0) : 1, # LEFT
    (0, 1)  : 2, # DOWN
    (1, 0)  : 3, # RIGHT
}

class Bot:
    def __init__(self, map_size) -> None:
        self.map_size = map_size
        self.map = [[[EMPTY] * NUM_DIRE] * self.map_size for _ in range(self.map_size)]  

    def reset_graph(self):
        self.map = [[[EMPTY] * NUM_DIRE] * self.map_size for _ in range(self.map_size)]  

    def _vector2_to_pair(self, vector):
        return (int(vector.x), int(vector.y))

    def update_graph(self, snake_pos, apple_pos):
        self.map[int(apple_pos.x)][int(apple_pos.y)] = [APPLE] * NUM_DIRE
        for blk in snake_pos:
            self.map[int(blk.x)][int(blk.y)] = [SNAKE] * NUM_DIRE

    def get_move(self, snake_pos, snake_dir, apple_pos):
        self.reset_graph()
        self.update_graph(snake_pos, apple_pos)
        self.snake_head = snake_pos[0]
        print(apple_pos)
        pos, path_history = self.bfs(self.snake_head, snake_dir)


        return self.backtrack(pos, path_history)

    def bfs(self, loc, dir):
        queue = []
        prev = {}

        for k, v in VECTOR_LOOKUP.items():
            if k == (self._vector2_to_pair(-dir)): 
                continue
            queue.append((int(loc.x), int(loc.y), v))
            prev[(int(loc.x), int(loc.y), v)] = (-1, -1, -1)

        visited = set()

        while len(queue):
            curr_pos = queue[0]
            x, y, d = curr_pos
            queue.pop(0)
            

            if self.map[x][y][d] == APPLE:
                return curr_pos, prev

            dir = DIRE_LOOKUP[d]
            next_x = x + dir[0]
            next_y = y + dir[1]
            
            if next_x < 0 or next_x >= self.map_size or next_y < 0 or next_y >= self.map_size:
                continue
            
            for i in range(4):
                next_coord = (next_x, next_y, i)
                if next_coord not in visited:
                    visited.add(curr_pos)
                    prev[next_coord] = (x, y, d)
                    queue.append(next_coord)

    def backtrack(self, pos, path_history):
        if path_history[pos][0] == int(self.snake_head.x) and path_history[pos][1] == int(self.snake_head.y):
            return path_history[pos][2]
        
        return self.backtrack(path_history[pos], path_history)


if __name__ == "__main__":
    bot = Bot(20)
    print(bot.get_move(
            [Vector2(12, 10),Vector2(12, 11),Vector2(12, 12),],
            Vector2(0, -1),
            Vector2(6, 5)
            ))

    # print(bot.get_move(
    #         [Vector2(12, 10),Vector2(12, 11),Vector2(12, 12),],
    #         Vector2(0, -1),
    #         Vector2(10, 10)
    #         ))


        