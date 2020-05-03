from addOne import add_one

def test_answer():
    assert add_one(1) == 2
    assert add_one(2) == 3
    assert add_one(3) != 0
