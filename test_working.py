from working import convert
import pytest

def test_number1():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
def test_number2():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"
def test_number3():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"
def test_number4():
    assert convert("10:30 PM to 8:50 AM") == "22:30 to 08:50"
def test_error1():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")
def test_error2():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
def test_error3():
    with pytest.raises(ValueError):
        convert("09:00 AM - 17:00 PM")
