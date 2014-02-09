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


def main():
    primes = []
    prime_sum = 0
    highest_prime_sum = (0,0)

    for i in range(2,100000):
        if is_a_prime(i):
            primes.append(i)
            prime_sum += i
            # print prime_sum
            print prime_sum, len(primes)
            if is_a_prime(prime_sum):
                # print True, prime_sum, len(primes)
                if prime_sum < 1000:
                    # print True, prime_sum, len(primes)
                    highest_prime_sum = (prime_sum, len(primes))
                else: 
                    break


            #     # highest_prime_sum = (prime_sum, len(primes))

            # if prime_sum < 1000:
            #     if is_a_prime(prime_sum):
            #         highest_prime_sum = (prime_sum, len(primes))
            # else:
            #     break

    # print 
    print highest_prime_sum

    # print is_a_prime(953)



	# print "Solution to problem 50:", solution
	

main()
