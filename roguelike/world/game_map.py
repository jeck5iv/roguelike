class GameMap:
    def __init__(self, width, height):
        from world.tile import Tile
        self.width = width
        self.height = height
        self.tiles = [[Tile(x, y) for x in range(width)] for y in range(height)]

    def get_tile(self, x, y):
        return self.tiles[y][x]

    def add_entity(self, entity):
        self.get_tile(entity.x, entity.y).occupant = entity

    def move_entity(self, entity, new_x, new_y):
        self.get_tile(entity.x, entity.y).occupant = None
        entity.x, entity.y = new_x, new_y
        self.get_tile(new_x, new_y).occupant = entity

    def get_player(self):
        for row in self.tiles:
            for tile in row:
                if tile.occupant and tile.occupant.__class__.__name__ == "Player":
                    return tile.occupant
        return None
