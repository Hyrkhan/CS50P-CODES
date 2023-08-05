from plates import is_valid

def test_no1():
    assert is_valid("CS50") == True

def test_no2():
    assert is_valid("CS05") == False

def test_no3():
    assert is_valid("CS50P") == False

def test_no4():
    assert is_valid("PI3.14") == False

def test_no5():
    assert is_valid("H") == False

def test_no6():
    assert is_valid("OUTATIME") == False
