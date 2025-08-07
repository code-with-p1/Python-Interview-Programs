import pytest
from calculator import Calculator

@pytest.fixture
def cls():
    return Calculator()

def test_addition(cls):
    assert cls.addition(2, 3) == 5
    assert cls.addition(3, 5) == 8
    assert cls.addition(2, 0) == 2

def test_substraction(cls):
    assert cls.substraction(5, 3) == 2
    assert cls.substraction(8, 5) == 3
    assert cls.substraction(2, 0) == 2

def test_multiply(cls):
    assert cls.multiply(2, 3) == 6
    assert cls.multiply(3, 5) == 15
    assert cls.multiply(2, 0) == 0

def test_division(cls):
    assert cls.division(10, 2) == 5
    assert cls.division(6, 2) == 3
    assert cls.division(8, 4) == 2


'''

Test Commands : 

pytest

pytest test_calculator.py

pytest test_calculator.py::test_multiply

pytest -v test_calculator.py

pytest -v test_calculator.py::test_multiply

'''