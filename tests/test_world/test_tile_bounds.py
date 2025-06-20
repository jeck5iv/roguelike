from world.game_map import GameMap

def test_map_out_of_bounds_protection():
    game_map = GameMap(3, 3)
    try:
        _ = game_map.get_tile(-1, 0)
        assert False, "Should raise IndexError"
    except IndexError:
        pass

    try:
        _ = game_map.get_tile(3, 3)
        assert False, "Should raise IndexError"
    except IndexError:
        pass
