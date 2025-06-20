from engine.commands.equip import EquipCommand
from entities.player import Player
from items.item import Item

def test_equip_places_item_in_slot():
    player = Player(0, 0)
    item = Item("Helmet", "head", {"defense": +1})
    player.inventory.add(item)
    cmd = EquipCommand(player, item)
    cmd.execute()
    assert player.inventory.equipped["head"] == item
