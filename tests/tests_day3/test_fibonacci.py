from programs.day3.fibonacci_loop import fibonacci_loop
from programs.day3.fibonacci_recursive import fibonacci_recursive

def test_fibonacci_loop():
    assert fibonacci_loop(5) == [0, 1, 1, 2, 3]

def test_fibonacci_recursive():
    assert fibonacci_recursive(5) == [0, 1, 1, 2, 3]

