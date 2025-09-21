#Task 3 Control strustures

#Simple function that checks to see if a number is positive, negative, or zero
def positiveOrNegative(number):

    if number > 0:

        return "Positive"

    elif number < 0:

        return "Negative"

    else:
        return "Zero"

#Function that returns a list of the first 10 prime numbers
def primeNumbers():

    primeNumbers = []
    n = 2

    #While there is less then 10 numbers in the array, math is done to see if a specfic number is prime
    #If the number is prime, the number is then appended to the array
    while len(primeNumbers) < 10:

        for i in range(2, int(n**0.5) + 1):

            if n % i ==0:
                break
        
        else:
            primeNumbers.append(n)
        n += 1

    print(primeNumbers)
    return primeNumbers
    
#Main just calls the 2 functions
def main():

    positiveOrNegative()
    primeNumbers()



#If script is ran directly for testing, call main
if __name__ == "__main__":

    main()