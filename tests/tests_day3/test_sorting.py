from programs.day3.bubble_sort import bubble_sort
from programs.day3.selection_sort import selection_sort
from programs.day3.insertion_sort import insertion_sort

def test_sorting_algorithms():
    arr = [5, 3, 1, 4, 2]
    expected = [1, 2, 3, 4, 5]

    assert bubble_sort(arr) == expected
    assert selection_sort(arr) == expected
    assert insertion_sort(arr) == expected
