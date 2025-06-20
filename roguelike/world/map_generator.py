from world.game_map import GameMap
from entities.mob import Mob

def generate_map(width, height):
    game_map = GameMap(width, height)
    # по умолчанию всегда добавим моба для демонстрации
    mob = Mob(x=3, y=3)
    game_map.add_entity(mob)
    return game_map
