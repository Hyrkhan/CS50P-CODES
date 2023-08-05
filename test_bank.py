from bank import value

def test_no1():
    assert value("Hello") == 0

def test_no2():
    assert value("Hello, Newman") == 0

def test_no3():
    assert value("How you doing?") == 20

def test_no4():
    assert value("What's happening?") == 100
