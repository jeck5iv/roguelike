from engine.commands.icommand import ICommand

class CompleteQuestCommand(ICommand):
    """
    Команда для принудительной проверки и завершения квеста.
    """
    def __init__(self, quest, world):
        self.quest = quest
        self.world = world

    def execute(self):
        """Проверить выполнение и отметить квест завершённым, если выполнен."""
        if self.quest.check_completion(self.world):
            print(f"Quest '{self.quest.description}' completed!")
