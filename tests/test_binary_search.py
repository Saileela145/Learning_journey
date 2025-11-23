from programs.day1.Binary_search_code import binary_search

def test_binary_search_found():
    arr = [2, 3, 5, 7, 43, 45, 87]
    assert binary_search(arr, 43) == 4
    assert binary_search(arr, 2) == 0

def test_binary_search_not_found():
    arr = [2, 3, 5, 7, 43, 45, 87]
    assert binary_search(arr, 100) == -1
