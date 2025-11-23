import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from programs.day2.task2.Sort_list import sorting

def test_sorting():
    assert sorting([3, 1, 2]) == [1, 2, 3]
    assert sorting([10, -1, 2]) == [-1, 2, 10]
    assert sorting([5]) == [5]
    assert sorting([]) == []
