from entities.strategy import AggressiveStrategy, PassiveStrategy, FleeingStrategy
from entities.state import PanicState
from entities.mob import Mob
from entities.player import Player
from world.game_map import GameMap

def test_aggressive_strategy_moves_toward():
    m = Mob(1, 1)
    p = Player(2, 1)
    world = GameMap(3, 3)
    world.add_entity(p)
    m.x, m.y = 1, 1
    s = AggressiveStrategy()
    dx, dy = s.decide(m, world)
    assert dx == 1 and dy == 0

def test_fleeing_strategy_moves_away():
    m = Mob(2, 2)
    p = Player(1, 2)
    world = GameMap(3, 3)
    world.add_entity(p)
    m.x, m.y = 2, 2
    s = FleeingStrategy()
    dx, dy = s.decide(m, world)
    assert dx == 1 and dy == 0

def test_panic_state_replaces_strategy():
    base = AggressiveStrategy()
    panic = PanicState()
    modified = panic.modify_strategy(base)
    assert isinstance(modified, FleeingStrategy)
