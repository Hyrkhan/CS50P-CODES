from fuel import convert, gauge
import pytest

def test_valueerror1():
    with pytest.raises(ValueError):
        assert convert("1.5/3")

def test_valueerror2():
    with pytest.raises(ValueError):
        assert convert("three/four")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")

def test_no1():
    assert convert("3/4") == 75

def test_no2():
    assert convert("1/4") == 25

def test_no3():
    assert gauge(99) == "F"

def test_no4():
    assert gauge(1) == "E"
