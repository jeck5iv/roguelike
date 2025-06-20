from entities.player import Player

def test_player_defaults():
    p = Player(0, 0)
    assert p.hp == 20
    assert p.attack_power == 4
