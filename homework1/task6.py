#Task 6
#Program counts the number of words in a text file
#The text is inputted, extracted, and uses pythons built in len function to count the characters

def countWords(fileName):

    with open(fileName, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        return len(words)

if __name__ == "__main__":

    main()