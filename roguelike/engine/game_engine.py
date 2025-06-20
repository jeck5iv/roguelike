from world.map_generator import generate_map
from entities.player import Player
from engine.input_handler import get_command
from render.renderer import render_map
from render.ui import render_status

class GameEngine:
    def __init__(self):
        self.game_map = generate_map(width=10, height=10)
        self.player = Player(x=1, y=1)
        self.game_map.add_entity(self.player)

    def run(self):
        while True:
            render_map(self.game_map)
            render_status(self.player)
            command = get_command(self.player, self.game_map)
            if command:
                command.execute()
