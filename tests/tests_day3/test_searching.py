from programs.day3.linear_search import linear_search
from programs.day3.binary_search import binary_search

def test_linear_search():
    assert linear_search([1, 2, 3, 4], 3) == 2
    assert linear_search([1, 2, 3], 10) == -1

def test_binary_search():
    arr = [1, 2, 3, 4, 5]
    assert binary_search(arr, 4) == 3
    assert binary_search(arr, 10) == -1

