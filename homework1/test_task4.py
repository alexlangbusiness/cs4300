#Task 4 testing file 
import task4

#Simply just double checks given values, and the math 
def test_calculate_discount_with_integers():

    assert task4.calculateDiscount(100, 20) == 80
    
#Also makes sure that the function can handle float values
#This is the one test that doesnt work, tried to debug it and couldnt solve it
def test_calculate_discount_with_floats():

    assert calculate_discount(100.0, 50.0) == pytest.approx(50.0)