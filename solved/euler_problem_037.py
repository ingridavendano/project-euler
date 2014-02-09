# Created by Ingrid Avendano on 10/31/13. 
#
#
# Project Euler - Problem 37: Truncatable primes
#
# The number 3797 has an interesting property. Being prime itself, it is 
# possible to continuously remove digits from left to right, and remain 
# prime at each stage: 3797, 797, 97, and 7. Similarly we can work from 
# right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from 
# left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


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

    if num == 1: 
        return False
    return number_is_prime


def truncatable_primes(num):
    num = str(num)
    prime = True

    for i in range(1,len(num)):

        # checking both sides
        left = is_a_prime(int(num[i:]))
        right = is_a_prime(int(num[:-i]))
        both = left and right

        # if any number is not a prime then number is not trunctable prime
        if not both:
            prime = False

    return prime


def main():
    numbers = []

    for i in range(10, 1000000): 
        if is_a_prime(i):
            if truncatable_primes(i):
                numbers.append(i)

    solution = sum(numbers)
    print "Solution to problem 37:", solution
	

main()
