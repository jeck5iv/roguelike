from quests.quest import Quest

def test_quest_completion():
    dummy_world = object()
    q = Quest("Test", goal=lambda w: True, reward="XP")
    assert not q.completed
    assert q.check_completion(dummy_world)
    assert q.completed
