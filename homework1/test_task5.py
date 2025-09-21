#Task 5 Lists and Dictionaries
#Test file ensures that these values can be accessed
import task5

#Ensures that the data is properly inputted
def test_data_return():

    books, students = task5.data()
    assert isinstance(books, list)
    assert isinstance(students, dict)

#Ensures that the books title and author can be accessed
def test_books():

    books, students = task5.data()
    assert books[0]["title"] == "The Trail"
    assert books[0]["author"] == "Franz Kafka"

#Ensures that the students and numbers can be accessed 
def test_students():
    
    books, students = task5.data()
    assert students["John"] == 1

