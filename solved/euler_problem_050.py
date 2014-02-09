# Created by Ingrid Avendano on 2/8/14. 
#
#
# Project Euler - Problem 50: Consecutive prime sum
#
# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
#
# This is the longest sum of consecutive primes that adds to a prime 
# below one-hundred.
#
# The longest sum of consecutive primes below one-thousand that adds to a
# prime, contains 21 terms, and is equal to 953.
#
# Which prime, below one-million, can be written as the sum of the most 
# consecutive primes?


# # checks for prime number
def is_prime(num):
    number_is_prime = True
    i = 2

    # only increment through numbers that are less or equal to 
    # half of the original number 
    while i*i <= num:
        if num%i == 0:
            number_is_prime = False
            break
        i += 1

    return number_is_prime


def find_primes():
    primes = []
    for i in range(2, 1000000):
        if is_prime(i):
            primes.append(i)

    return primes


def main():
    primes = find_primes()
    solution = 0

    # starting point to find highest prime
    for start in range(20):
        prime_sum = 0
        i = start
        count = 0

        while prime_sum < 1000000: 
            prime_sum += primes[i]
            count += 1
            i += 1

            if is_prime(prime_sum):
                if solution < prime_sum and prime_sum < 1000000:
                    solution = prime_sum
            
    print "Solution to problem 50:", solution


main()
