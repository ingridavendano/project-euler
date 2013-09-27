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
def has_prime_factor(num):
	i = 2
	has_prime = False

	# only increment through numbers that are less than half of
	# the original number 
	while i*i < num:
		# checks if the number incremented is divisible by original number
		if num%i == 0:
			has_prime = True
			break
		i += 1

	return has_prime

# finds the nth prime number
def nth_prime(num):
	run = True
	count = 0
	prime_at_nth = 0
	i = 2
	while num > 0:

		if has_prime_factor(i):
			num -= 1
			count += 1

		if num==0:
			prime_at_nth = i - 2

		i += 1

	print "Prime number at %d is %d" % (count, prime_at_nth)

nth_prime(10001)
