import task7

def test_calculate_abs():

    assert task7.calculate_abs(-1) == 1
    assert task7.calculate_abs(8) == 8

def test_add_values():

    assert task7.add_numbers(1, 2) == 3
    assert task7.add_numbers(5, 6) == 11
