'''My Calculator Test'''
from calculator import Calculator

def test_addition():
    '''Test that addition works '''
    assert Calculator.add(2,2) == 4

def test_subtraction():
    '''Test that substraction works '''
    assert Calculator.subtract(2,2) == 0

def test_multiply():
    '''Test that multiplication works '''
    assert Calculator.multiply(2,2) == 4

def test_divide():
    '''Test that division works '''
    assert Calculator.divide(2,2) == 1
