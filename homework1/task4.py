#Task 4

def calculateDiscount(price, discount):

    if 0 <= discount <= 100:
        overallPrice = price * (1 - (discount / 100))
        return overallPrice
    
    else:
        print("Discount percentage must be greater then 0, and less then 100")


def main():

   print(calculateDiscount(100, 50))

if __name__ == "__main__":

    main()