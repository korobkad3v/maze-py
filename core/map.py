import config as c
import random
from typing import List
from core.player import Player

class Map:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        
        self.start_coord = None
        self.finish_coord = None

    def generate_maze(self):
        self.map_els = [[c.MAZE_BLOCK for _ in range(self.width)] for _ in range(self.height)]
        finish = self.generate_finish()
        start = self.generate_start(finish)

        stack = [start]
        visited_cells = set([start])

        while stack:
            x, y = stack[-1]
            neighbors = [(x + dx, y + dy) for dx, dy in [(0, 2), (2, 0), (0, -2), (-2, 0)]]
            random.shuffle(neighbors)
            valid_neighbors = [neighbor for neighbor in neighbors if self.is_valid_cell(neighbor) and neighbor not in visited_cells]

            if valid_neighbors:
                next_cell = random.choice(valid_neighbors)
                nx, ny = next_cell
                self.map_els[ny][nx] = c.MAZE_PATH
                visited_cells.add(next_cell)
                stack.append(next_cell)

                mx, my = (x + nx) // 2, (y + ny) // 2
                self.map_els[my][mx] = c.MAZE_PATH

                if len(stack) == 2:
                    self.start_coord = start
                    self.finish_coord = finish

                    
                    
            else:
                stack.pop()
        
        self.map_els[self.start_coord[0]][self.start_coord[1]] = c.MAZE_START
        self.map_els[self.finish_coord[0]][self.finish_coord[1]] = c.MAZE_FINISH
        

    def generate_start(self, finish_coord):
        
        min_distance = max(self.width, self.height) // 2
        while True:
            start = (random.randint(1, (self.width - 1) // 2) * 2 - 1, random.randint(1, (self.height - 1) // 2) * 2 - 1)
            distance = abs(start[0] - finish_coord[0]) + abs(start[1] - finish_coord[1])
            if distance >= min_distance:
                return start
            
    def generate_finish(self):
        return (
            random.randint(1, (self.width - 1) // 2) * 2 - 1,
            random.randint(1, (self.height - 1) // 2) * 2 - 1
        )

    

    def place_player(self, player: Player) -> None:
        self.map_els[player.coord[0]][player.coord[1]] = c.MAZE_PLAYER

    def delete_place_player(self, player: Player) -> None:
        self.map_els[player.coord[0]][player.coord[1]] = c.MAZE_PATH

    def is_valid_cell(self, cell):
        x, y = cell
        return 0 < x < self.width - 1 and 0 < y < self.height - 1



    def display_map(self) -> None:
        
        for row in self.map_els:
            print(" ".join(str(cell) for cell in row))