from fuel import convert


def test_full():
    assert convert("3/3") == "F"


def test_empty():
    assert convert("0/3") == "E"


def test_anythingelse():
    assert convert("1/3") == "33%"
    assert convert("2/3") == "66%"
