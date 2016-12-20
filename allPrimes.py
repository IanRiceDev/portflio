# prints primes to a given range
import primeclass
# imports prime class
z = 1
# defines variable and sets it equal to 1
i = 0
# defines variable and sets it equal to 0
while i < 100:
    x = primeclass.check_if_prime(z)
    print(x)
    i += 1
    z += 1
# loop to print primes to screen