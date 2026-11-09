# Week 1.7, Session 1: Task 4 - unit tests for methods in Money

import pytest

from money import Money

def test_invalid_type_pound():
    with pytest.raises(TypeError) as excinfo:
        Money(1.2, 99)
    assert str(excinfo.value) == "pounds must be an integer"


def test_invalid_value_pound():
    with pytest.raises(ValueError) as excinfo:
        Money(-1, 0)
    assert str(excinfo.value) == "pounds must be >= 0"


def test_add_invalid_type():
    m1 = Money(5, 0)
    with pytest.raises(TypeError) as excinfo:
        m1 + 42
    assert str(excinfo.value) == "other object must be a Money"


def test_invalid_type_pence():
    with pytest.raises(TypeError) as ex:
        m = Money(0, "ten trillion pence")
    assert str(ex.value) ==  "pence must be an integer"   
        

def test_invalid_value_pence():
    with pytest.raises(ValueError) as ex:
        m = Money(0, 100)
    assert str(ex.value) == "pence must be in range 0-99"

def test_valid_add():    
    assert str(Money(0,0) + Money(50, 0)) == "£50.00"
    assert str(Money(0,99) + Money(50, 0)) == "£50.99"
    assert str(Money(1,99) + Money(50, 2)) == "£52.01"