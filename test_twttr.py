from twttr import shorten

def test_no1():
    assert shorten("Twitter") == "Twttr"

def test_no2():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_no3():
    assert shorten("CS50") == "CS50"

def test_no4():
    assert shorten("hellO") == "hll"
