#Task 4
#Function that calculates new price of somthing given a price and discount
#The function makes sure that the discount is between the given requirements
#Then calculates the new price based on given paramaters 
def calculateDiscount(price, discount):

    if 0 <= discount <= 100:
        overallPrice = price * (1 - (discount / 100))
        return overallPrice
    
    else:
        print("Discount percentage must be greater then 0, and less then 100")


def main():

   print(calculateDiscount(100, 50))

#If script is ran directly for testing, call main
if __name__ == "__main__":

    main()