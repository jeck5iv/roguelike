class Entity:
    """
    Базовый класс для всех игровых существ.
    """

    def __init__(self, x, y, hp=10, attack=3):
        self.x = x
        self.y = y
        self.hp = hp
        self.attack_power = attack

    def is_dead(self):
        """Проверить, мертва ли сущность."""
        return self.hp <= 0

    def attack(self, other):
        """Нанести урон другой сущности."""
        other.take_damage(self.attack_power)
        print(f"{type(self).__name__} attacks {type(other).__name__}! {other.hp} HP left.")

    def take_damage(self, amount):
        """Получить урон и проверить на смерть."""
        self.hp -= amount
        if self.hp <= 0:
            print(f"{type(self).__name__} has died.")
