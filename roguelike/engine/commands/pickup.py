from engine.commands.icommand import ICommand

class PickUpCommand(ICommand):
    """
    Команда подбора предмета с клетки.
    """
    def __init__(self, entity, tile):
        self.entity = entity
        self.tile = tile

    def execute(self):
        """Добавить предмет из клетки в инвентарь игрока."""
        if self.tile.item:
            self.entity.inventory.add(self.tile.item)
            print(f"Picked up {self.tile.item.name}")
            self.tile.item = None
