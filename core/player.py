from typing import List

class Player():
    def __init__(self, coord: List[int]) -> None:
        self.coord = coord

    def move_up(self) -> None:
        self.coord[0] -= 1
    
    def move_down(self) -> None:
        self.coord[0] += 1
    
    def move_right(self) -> None:
        self.coord[1] += 1

    def move_left(self) -> None:
        self.coord[1] -= 1
    


    