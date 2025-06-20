class Quest:
    def __init__(self, description, goal, reward):
        self.description = description
        self.goal = goal
        self.reward = reward
        self.completed = False

    def check_completion(self, world):
        self.completed = self.goal(world)
        return self.completed
