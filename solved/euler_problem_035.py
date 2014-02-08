# Created by Ingrid Avendano on 10/31/13. 
#
#
# Project Euler - Problem 35: Circular primes
#
# The number, 197, is called a circular prime because all rotations 
# of the digits: 197, 971, and 719, are themselves prime.
#
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 
# 31, 37, 71, 73, 79, and 97.
#
# How many circular primes are there below one million?


# checks for prime number
def is_a_prime(num):
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


def shift_number(num):
    num = str(num)
    num = int(num[-1] + num[:-1])
    return num


def main():
    numbers = range(2,1000000)
    primes = []
    shift = 0
    total = []

    # checks for list of primes
    while shift <= 6: 
        for i in numbers:
            if is_a_prime(i):
                if len(str(i)) == shift+1:
                    total.append(i)
                else: 
                    primes.append(shift_number(i))
        numbers = primes
        primes = []
        shift += 1

    solution = len(total)
    print "Solution to problem 35:", solution


main()
