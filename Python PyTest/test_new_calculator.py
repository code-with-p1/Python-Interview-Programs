import pytest
from calculator import Calculator

@pytest.fixture
def cls():
    return Calculator()

def test_addition(cls):
    assert cls.addition(5,5) == 10