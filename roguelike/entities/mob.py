from entities.entity import Entity

class Mob(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, hp=6, attack=2)
