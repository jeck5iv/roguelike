def render_map(game_map):
    for y in range(game_map.height):
        row = ""
        for x in range(game_map.width):
            tile = game_map.get_tile(x, y)
            if tile.occupant:
                row += "@" if tile.occupant.__class__.__name__ == "Player" else "M"
            else:
                row += "."
        print(row)
    print()
