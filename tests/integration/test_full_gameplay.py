from engine.game_engine import GameEngine
from entities.player import Player
from entities.mob import Mob
from engine.commands.move import MoveCommand
from engine.commands.attack import AttackCommand
from world.game_map import GameMap

def test_game_start_and_move():
    # Проверяем, что игрок может сдвинуться на одну клетку вправо
    engine = GameEngine()
    p = engine.player
    old_pos = (p.x, p.y)

    cmd = MoveCommand(p, 1, 0, engine.game_map)
    cmd.execute()

    assert (p.x, p.y) == (old_pos[0] + 1, old_pos[1])

def test_combat_and_mob_death():
    # Проверяем, что атака игрока убивает моба
    game_map = GameMap(5, 5)
    player = Player(1, 1)
    mob = Mob(2, 1)

    game_map.add_entity(player)
    game_map.add_entity(mob)

    # Имитация нескольких атак
    cmd = AttackCommand(player, mob)
    cmd.execute()
    cmd.execute()
    cmd.execute()  # моб должен погибнуть

    assert mob.is_dead()

def test_move_and_attack_sequence():
    # Проверяем, что игрок не может встать на клетку с мобом, но атакует его
    game_map = GameMap(5, 5)
    player = Player(1, 1)
    mob = Mob(2, 1)
    game_map.add_entity(player)
    game_map.add_entity(mob)

    move = MoveCommand(player, 1, 0, game_map)
    move.execute()  # должен сработать attack, а не move

    assert mob.hp < 6  # моб получил урон
    assert (player.x, player.y) == (1, 1)  # игрок остался на месте
