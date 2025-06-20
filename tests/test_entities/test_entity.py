from entities.entity import Entity

def test_entity_takes_damage():
    e = Entity(0, 0, hp=10)
    e.take_damage(3)
    assert e.hp == 7
    assert not e.is_dead()

def test_entity_dies():
    e = Entity(0, 0, hp=2)
    e.take_damage(3)
    assert e.is_dead()
