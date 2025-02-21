from core.map import Map
from core.player import Player
from pynput import keyboard
import config as c
import os

class Maze:
    def __init__(self) -> None:
        self.map = Map(width=c.MAP_SIZE["width"], height=c.MAP_SIZE["height"])
        self.restart()

    def restart(self) -> None:
        self.map.generate_maze()

        self.player = Player(coord=list(self.map.start_coord))
        self.map.place_player(player=self.player)

    def check_move_up(self) -> bool:
        return self.map.map_els[self.player.coord[0] - 1][self.player.coord[1]] in [c.MAZE_PATH, c.MAZE_FINISH] 
    
    def check_move_left(self) -> bool:
        return self.map.map_els[self.player.coord[0]][self.player.coord[1] - 1] in [c.MAZE_PATH, c.MAZE_FINISH] 
    
    def check_move_down(self) -> bool:
        return self.map.map_els[self.player.coord[0] + 1][self.player.coord[1]] in [c.MAZE_PATH, c.MAZE_FINISH] 
    
    def check_move_right(self) -> bool:
        return self.map.map_els[self.player.coord[0]][self.player.coord[1] + 1] in [c.MAZE_PATH, c.MAZE_FINISH] 
    
    def handle_move_up(self) -> None:
        if self.check_move_up():
            self.map.delete_place_player(player=self.player)
            self.player.move_up()
            self.map.place_player(player=self.player)

    def handle_move_left(self) -> None:
        if self.check_move_left():
            self.map.delete_place_player(player=self.player)
            self.player.move_left()
            self.map.place_player(player=self.player)
    
    def handle_move_down(self) -> None:
        if self.check_move_down():
            self.map.delete_place_player(player=self.player)
            self.player.move_down()
            self.map.place_player(player=self.player)

    def handle_move_right(self) -> None:
        if self.check_move_right():
            self.map.delete_place_player(player=self.player)
            self.player.move_right()
            self.map.place_player(player=self.player)

    def is_player_finished(self) -> bool:
        return self.map.finish_coord[0] == self.player.coord[0] and self.map.finish_coord[1] == self.player.coord[1]

    def on_key_release(self, key):
        if key == keyboard.Key.esc:

            return False
        elif key == keyboard.Key.up:
            self.handle_move_up()
        elif key == keyboard.Key.left:
            self.handle_move_left()
        elif key == keyboard.Key.down:
            self.handle_move_down()
        elif key == keyboard.Key.right:
            self.handle_move_right()
        os.system("cls || clear")
        self.map.display_map()

    def run(self) -> None:
        with keyboard.Listener(on_release=self.on_key_release) as listener:
            while True:
                
                
                if self.is_player_finished():
                    self.restart()
                

if __name__ == "__main__":
    maze_game = Maze()
    maze_game.run()