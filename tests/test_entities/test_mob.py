from entities.mob import Mob

def test_mob_defaults():
    m = Mob(1, 1)
    assert m.hp == 6
    assert m.attack_power == 2
