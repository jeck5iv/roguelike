from engine.commands.icommand import ICommand

class EquipCommand(ICommand):
    """
    Команда экипировки предмета.
    """
    def __init__(self, inventory, item):
        self.inventory = inventory
        self.item = item

    def execute(self):
        """Поместить предмет в слот экипировки."""
        self.inventory.equip(self.item)
