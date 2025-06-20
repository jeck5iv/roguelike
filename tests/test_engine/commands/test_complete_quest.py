from engine.commands.complete_quest import CompleteQuestCommand
from quests.quest import Quest

def test_complete_quest_if_goal_met():
    world = type("DummyWorld", (), {})()
    quest = Quest("Test", goal=lambda w: True, reward=None)
    cmd = CompleteQuestCommand(quest, world)
    cmd.execute()
    assert quest.completed
