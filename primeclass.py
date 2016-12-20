# defines this file as a class
def check_if_prime(numberinput):

    # defines variable
    numbertest = str(numberinput)
    message = ""
    basePrimes = [2,3,5,7]
    notPrimes = [0,1]

    # Loop where the work of the class takes place
    while True:
        # Checks if the in put is a number before math of the class
        if numbertest.isdigit() == False:
            print("That is not a number")
            break
        # Defines variable in the scope of the loop
        if True:
            numberoutput = int(numberinput)
            baseNum = numberoutput
            basePrime = baseNum
        # Checks if number is a part of base primes
        if basePrime in basePrimes:
            message = numbertest+" is a prime number number."
            break
        # Checks if number is a part of numbers that can not be prime
        if basePrime in notPrimes:
            message = numbertest+" is not a prime number."
            break
        # Uses models operator to test remainder of division for primes
        if basePrime % 2 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 3 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 5 == 0:
            message = numbertest+" is not a prime number."
            break
        if basePrime % 7 == 0:
            message = numbertest+" is not a prime number."
            break
        # Else must be prime
        else:
            message = numbertest+" is a prime number."
            break
    # Returns variable message
    return message
