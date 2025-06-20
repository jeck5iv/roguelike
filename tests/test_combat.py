from entities.player import Player
from entities.mob import Mob

def test_combat_kills():
    p = Player(0, 0)
    m = Mob(0, 1)
    p.attack(m)
    p.attack(m)
    assert m.is_dead()
