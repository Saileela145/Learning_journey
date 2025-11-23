from ..programs.day2.task1.print_sum_of_first_n_numbers import natural

def test_natural_sum():
    assert natural(5) == 15
    assert natural(1) == 1
    assert natural(0) == 0
