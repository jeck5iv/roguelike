class Inventory:
    def __init__(self):
        self.items = []
        self.equipped = {}

    def add(self, item):
        self.items.append(item)

    def equip(self, item):
        self.equipped[item.slot] = item

    def unequip(self, slot):
        if slot in self.equipped:
            del self.equipped[slot]
