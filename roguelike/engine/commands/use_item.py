from engine.commands.icommand import ICommand

class UseItemCommand(ICommand):
    """
    Команда применения предмета.
    """
    def __init__(self, entity, item):
        self.entity = entity
        self.item = item

    def execute(self):
        """Активировать эффект предмета на сущность."""
        self.item.apply_effect(self.entity)
