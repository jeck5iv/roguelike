class Tile:
    def __init__(self, x, y, passable=True):
        self.x = x
        self.y = y
        self.passable = passable
        self.occupant = None
