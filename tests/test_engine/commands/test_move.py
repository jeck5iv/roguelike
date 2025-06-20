from engine.commands.move import MoveCommand
from entities.player import Player
from world.game_map import GameMap
from world.tile import Tile

def test_move_to_empty_tile():
    player = Player(1, 1)
    game_map = GameMap(3, 3)
    cmd = MoveCommand(player, dx=1, dy=0, game_map=game_map)
    cmd.execute()
    assert (player.x, player.y) == (2, 1)
