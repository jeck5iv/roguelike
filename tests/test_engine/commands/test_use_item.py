from engine.commands.use_item import UseItemCommand
from entities.player import Player
from items.item import Item

def test_use_item_modifies_entity():
    player = Player(0, 0)
    
    class HealingPotion(Item):
        def __init__(self):
            super().__init__("Potion", None, {})
        def apply_effect(self, entity):
            entity.hp += 5

    potion = HealingPotion()
    player.inventory.add(potion)
    cmd = UseItemCommand(player, potion)
    cmd.execute()
    assert potion not in player.inventory.items
    assert player.hp > 20
