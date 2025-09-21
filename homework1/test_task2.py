#Test file for task 2
#Each function checks to see if each main function is actually an instance
#Then double checks the variable type, and verifies expected values 
import task2

def test_integer():
    assert isinstance(task2.returnInteger(), int)
    assert task2.returnInteger() == 1

def test_float():
    assert isinstance(task2.returnFloat(), float)
    assert task2.returnFloat() == 1.5

def test_string():
    assert isinstance(task2.returnString(), str)
    assert task2.returnString() == "Hello"

def test_boolean():
    assert isinstance(task2.returnBoolean(), bool)
    assert task2.returnBoolean() == True