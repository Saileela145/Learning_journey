import numpy as np

def test_numpy_reshape():
    arr = np.array([1, 2, 3, 4])
    reshaped = arr.reshape(2, 2)
    assert reshaped.shape == (2, 2)

def test_numpy_transpose():
    matrix = np.array([[1, 2], [3, 4]])
    transposed = matrix.T
    assert transposed.tolist() == [[1, 3], [2, 4]]

