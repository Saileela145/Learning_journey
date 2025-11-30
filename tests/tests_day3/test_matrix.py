from programs.day3.matrix_addition import matrix_addition
from programs.day3.matrix_transpose import matrix_transpose

def test_matrix_addition():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    assert matrix_addition(A, B) == [[6, 8], [10, 12]]

def test_matrix_transpose():
    A = [[1, 2, 3], [4, 5, 6]]
    assert matrix_transpose(A) == [[1, 4], [2, 5], [3, 6]]
