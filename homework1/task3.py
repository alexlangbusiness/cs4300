#Task 3 Control strustures

def positiveOrNegative(number):

    if number > 0:

        return "Positive"

    elif number < 0:

        return "Negative"

    else:
        return "Zero"

def primeNumbers():

    primeNumbers = []
    n = 2

    while len(primeNumbers) < 10:

        for i in range(2, int(n**0.5) + 1):

            if n % i ==0:
                break
        
        else:
            primeNumbers.append(n)
        n += 1

    print(primeNumbers)
    return primeNumbers
    

def main():

    positiveOrNegative()
    primeNumbers()




if __name__ == "__main__":

    main()