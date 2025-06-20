class QuestSystem:
    def __init__(self):
        self.quests = []

    def add_quest(self, quest):
        self.quests.append(quest)

    def update(self, world):
        for quest in self.quests:
            if not quest.completed:
                quest.check_completion(world)
