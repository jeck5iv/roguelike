from items.inventory import Inventory
from items.item import Item

def test_add_item_to_inventory():
    inv = Inventory()
    item = Item("Sword", "hand", {"attack": +2})
    inv.add(item)
    assert item in inv.items

def test_equip_item():
    inv = Inventory()
    item = Item("Helmet", "head", {"defense": +1})
    inv.equip(item)
    assert inv.equipped["head"] == item

def test_unequip_item():
    inv = Inventory()
    item = Item("Boots", "feet", {"defense": +1})
    inv.equip(item)
    inv.unequip("feet")
    assert "feet" not in inv.equipped
