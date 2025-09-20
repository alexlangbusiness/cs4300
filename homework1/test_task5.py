import task5

def data():

    assert task4.calculateDiscount(100, 20) == 80

def test_data_return():

    books, students = task5.data()
    assert isinstance(books, list)
    assert isinstance(students, dict)

def test_books():

    books, students = task5.data()
    assert books[0]["title"] == "The Trail"
    assert books[0]["author"] == "Franz Kafka"

def test_students():
    
    books, students = task5.data()
    assert students["John"] == 1

