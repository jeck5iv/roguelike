def render_status(player):
    print(f"HP: {player.hp}  Pos: ({player.x},{player.y})")
    if hasattr(player, 'inventory'):
        print("Equipped:")
        for slot, item in player.inventory.equipped.items():
            print(f"  {slot}: {item.name}")
