from engine.commands.icommand import ICommand

class AttackCommand(ICommand):
    """
    Команда атаки одной сущности по другой.
    """
    def __init__(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender

    def execute(self):
        """Нанести урон защитнику."""
        self.attacker.attack(self.defender)
