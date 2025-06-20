from world.map_generator import generate_map

def test_generated_map_has_mobs():
    game_map = generate_map(5, 5)
    found = False
    for row in game_map.tiles:
        for tile in row:
            if tile.occupant:
                found = True
    assert found
