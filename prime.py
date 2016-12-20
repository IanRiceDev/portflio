# standalone prime program
numberinput = input("Type any number to see if it is a prime number: ")

message = ""
basePrimes = [2,3,5,7]
notPrimes = [0,1]
listcount = 0
numbertest = str(numberinput)
while True:

    if numbertest.isdigit() == False:
        print("That is not a number")
        break
    if True:
        numberoutput = int(numberinput)
        baseNum = numberoutput
        m2 = baseNum
    if m2 in basePrimes:
        message = numbertest + " is a prime number number."
        break
    if m2 in notPrimes:
        message = numbertest + " is not a prime number."
        break
    if m2 % 2 == 0:
        message = numbertest + " is not a prime number."
        break
    if m2 % 3 == 0:
        message = numbertest + " is not a prime number."
        break
    if m2 % 5 == 0:
        message = numbertest + " is not a prime number."
        break
    if m2 % 7 == 0:
        message = numbertest + " is not a prime number."
        break
    else:
        message = numbertest + " is a prime number."
        break



print("\n")
print(message)
print("\n")
input("Press the enter key to exit")
