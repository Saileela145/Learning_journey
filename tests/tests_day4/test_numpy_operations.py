import numpy as np

def test_numpy_addition():
    a = np.array([1, 2, 3])
    b = np.array([4, 5, 6])
    result = a + b
    assert np.array_equal(result, np.array([5, 7, 9]))

def test_numpy_multiplication():
    a = np.array([2, 3])
    b = np.array([4, 5])
    result = a * b
    assert np.array_equal(result, np.array([8, 15]))
