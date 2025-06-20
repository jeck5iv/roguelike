from engine.commands.move import MoveCommand

def get_command(entity, game_map):
    key = input("Move (WASD): ").lower()
    moves = {'w': (0, -1), 's': (0, 1), 'a': (-1, 0), 'd': (1, 0)}
    if key in moves:
        dx, dy = moves[key]
        return MoveCommand(entity, dx, dy, game_map)
    return None
