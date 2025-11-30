from programs.day3.factorial_loop import factorial_loop
from programs.day3.factorial_recursive import factorial_recursive

def test_factorial_loop():
    assert factorial_loop(5) == 120

def test_factorial_recursive():
    assert factorial_recursive(5) == 120
