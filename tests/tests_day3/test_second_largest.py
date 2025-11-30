from programs.day3.second_largest import second_largest

def test_second_largest():
    assert second_largest([1, 3, 2]) == 2
    assert second_largest([10, 10, 9]) == 9
    assert second_largest([5, 5, 5]) is None
