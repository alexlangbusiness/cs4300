import task4

def test_calculate_discount_with_integers():

    assert task4.calculateDiscount(100, 20) == 80
    

def test_calculate_discount_with_floats():

    assert calculate_discount(100.0, 50.0) == pytest.approx(50.0)