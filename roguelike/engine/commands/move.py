from engine.commands.icommand import ICommand

class MoveCommand(ICommand):
    """
    Команда перемещения сущности на карте.
    Если целевая клетка проходима и пуста — происходит перемещение.
    Если занята — выполняется атака по занятию.
    """
    def __init__(self, entity, dx, dy, game_map):
        self.entity = entity
        self.dx = dx
        self.dy = dy
        self.game_map = game_map

    def execute(self):
        """Выполнить перемещение или атаку в зависимости от содержимого цели."""
        new_x = self.entity.x + self.dx
        new_y = self.entity.y + self.dy
        if not (0 <= new_x < self.game_map.width and 0 <= new_y < self.game_map.height):
            print("Out of bounds!")
            return
        tile = self.game_map.get_tile(new_x, new_y)
        if tile.passable and not tile.occupant:
            self.game_map.move_entity(self.entity, new_x, new_y)
        elif tile.occupant:
            self.entity.attack(tile.occupant)
