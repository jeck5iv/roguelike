class IMobStrategy:
    def decide(self, mob, world):
        raise NotImplementedError

class AggressiveStrategy(IMobStrategy):
    def decide(self, mob, world):
        player = world.get_player()
        dx = player.x - mob.x
        dy = player.y - mob.y
        return (1 if dx > 0 else -1 if dx < 0 else 0,
                1 if dy > 0 else -1 if dy < 0 else 0)

class PassiveStrategy(IMobStrategy):
    def decide(self, mob, world):
        return (0, 0)

class FleeingStrategy(IMobStrategy):
    def decide(self, mob, world):
        player = world.get_player()
        dx = mob.x - player.x
        dy = mob.y - player.y
        return (1 if dx > 0 else -1 if dx < 0 else 0,
                1 if dy > 0 else -1 if dy < 0 else 0)
