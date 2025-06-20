from engine.commands.pickup import PickUpCommand
from entities.player import Player
from items.item import Item
from world.tile import Tile

def test_pickup_adds_to_inventory():
    player = Player(0, 0)
    item = Item("Sword", "hand", {"attack": +2})
    tile = Tile(0, 0)
    tile.item = item
    cmd = PickUpCommand(player, tile)
    cmd.execute()
    assert item in player.inventory.items
    assert tile.item is None
