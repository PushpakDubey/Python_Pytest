# Assuming pytest, src and all the functions are available in your Python environment
import pytest
from src.calculator import Calculator

def test_add():
    assert Calculator.add(1, 2) == 3


def test_subtract():
    assert Calculator.subtract(2, 1) == 1


def test_multiply():
    assert Calculator.multiply(2, 3) == 6


def test_divide():
    assert Calculator.divide(6, 3) == 2

def test_square():
    assert Calculator.square(4) == 16
