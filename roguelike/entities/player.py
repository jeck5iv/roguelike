from entities.entity import Entity

class Player(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, hp=20, attack=4)
