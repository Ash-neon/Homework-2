'''My Calculator Test'''
from calculator.operations import add, multiply, subtract, divide

def test_addition():
    '''Test that addition works '''    
    assert add(2,2) == 4

def test_subtraction():
    '''Test that subtraction works '''    
    assert subtract(2,2) == 0

def test_multiplication():
    '''Test that multiplication works'''
    assert multiply(2,2) == 4

def test_division():
    '''Test that division works'''
    assert divide(2,2) == 1
