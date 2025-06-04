import pytest

def square(n):
    return n**2

def cube(n):
    return n**3

def test_square(n):
    assert square(2)==4, "Test Failed: square of 2 should be 4"
    assert square(3)==9, "Test Failed: square of 3 should be 9"

def test_cube(n):
    assert cube(2)==8, "Test Failed: Cube of 2 should be 8"
    assert cube(3)==27, "Test Failed: Cube of 3 should be 27"
    

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string") 