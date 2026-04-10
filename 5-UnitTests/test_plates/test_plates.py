from plates import is_valid


def test_length():
    assert is_valid("WAYTOOLONG") == False


def test_begginum():
    assert is_valid("12Skip") == False


def test_ischar():
    assert is_valid(":,.ABC") == False


def test_middlenum():
    assert is_valid("AB12RT") == False
    assert is_valid("ABCD3F") == False


def test_valid():
    assert is_valid("AAAAHH") == True
