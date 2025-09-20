#Task 6

def countWords(fileName):

    with open(fileName, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        return len(words)

if __name__ == "__main__":

    main()