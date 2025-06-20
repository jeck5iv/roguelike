from quests.quest import Quest

def kill_all_mobs_goal(world):
    return not any(e for row in world.tiles for tile in row
                   if tile.occupant and tile.occupant.__class__.__name__ == "Mob")

def generate_kill_quest():
    return Quest("Уничтожь всех мобов", goal=kill_all_mobs_goal, reward="LevelUp")

def generate_random_quest():
    return generate_kill_quest()
