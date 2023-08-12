from seasons import validate_date
import pytest

def test_validation():
    date = validate_date("2001-11-24")
    assert date.year == 2001
    assert date.month == 11
    assert date.day == 24

def test_exception():
    with pytest.raises(SystemExit):
        validate_date("January")

