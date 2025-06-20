from engine.commands.attack import AttackCommand
from entities.player import Player
from entities.mob import Mob

def test_attack_reduces_hp():
    p = Player(0, 0)
    m = Mob(0, 1)
    cmd = AttackCommand(p, m)
    cmd.execute()
    assert m.hp < 6
