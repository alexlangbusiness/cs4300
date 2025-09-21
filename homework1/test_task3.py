#Test file for task 3
import task3

#Tests postiveOrNegative function
#Verifies that expected values result in the correct string
def test_positiveOrNegative():

    assert isinstance(task3.positiveOrNegative(5), str)
    assert task3.positiveOrNegative(5) == "Positive"
    assert task3.positiveOrNegative(-5) == "Negative"
    assert task3.positiveOrNegative(0) == "Zero"

#Tests primenumbers function
#Verifies that the first 10 prime numbers are returned 
def test_primeNumbers():

    returnValue = task3.primeNumbers()
    assert returnValue == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    
