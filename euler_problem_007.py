# Created by Ingrid Avendano on 9/26/13. 
#
#
# Project Euler - Problem 7:
#
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
# see that the 6th prime is 13.
#
# What is the 10 001st prime number?


# checks for highest prime factor
def is_prime_factor(num):
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


# finds the nth prime number
def nth_prime(num):
	prime_at_nth = 0
	number_of_primes = 0
	i = 2
	
	while number_of_primes < num:

		# only increments the number_of_primes if it is a 
		# prime number 
		if is_prime_factor(i):
			number_of_primes += 1

		if num==number_of_primes:
			prime_at_nth = i 

		i += 1

	print "Prime number at %d is %d." % (number_of_primes, prime_at_nth)

nth_prime(10001)
