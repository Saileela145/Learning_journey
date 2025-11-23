import sys
import os

# Add root folder to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from programs.day2.task3.linear_search import linear_search

def test_linear_search():
    assert linear_search([10, 20, 30], 20) == 1
    assert linear_search([5, 6, 7], 7) == 2
    assert linear_search([1, 2, 3], 4) == -1
    assert linear_search([], 5) == -1
