from bank import detective


def test_hello():
    assert detective("hello") == "$0"


def test_h():
    assert detective("hey") == "$20"


def test_else():
    assert detective("yo") == "$100"
