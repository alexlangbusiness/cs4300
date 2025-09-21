#Task 5 Lists and Dictionaries
#Program defines a dictionary of books, and a list of students
#The program wants to ensure that the values within these data structures can be properly accessed
#These values are then printed
def data():

    books = [
        {"title": "The Trail", "author": "Franz Kafka"},
        {"title": "Middlemarch", "author": "George Eliot"},
        {"title": "Moby Dick", "author": "Herman Melville"}
    ]

    students = {
        "John": 1,
        "Debora": 2,
        "Joe": 3,
        "Larissa": 4
    }

    return books, students

def main():

    books,students = data()
    print("Favorite books:", books)
    print("Students: ", students)


if __name__ == "__main__":

    main()