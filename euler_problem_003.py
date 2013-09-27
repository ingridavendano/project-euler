# Created by Ingrid Avendano on 9/23/13. 
#
#
# Project Euler - Problem 3:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math 


# checks for highest prime factor
def highest_prime_factor(num):
	i = 2

	# only increment through numbers that are less than half of
	# the original number 
	while i*i < num:
		# print "i is: %d" % i

		# checks if the number incremented is divisible by number
		while num%i == 0:
			num = num/i 
		i += 1

	return num


def main(): 
	solution = highest_prime_factor(600851475143)
	print "Solution to problem 3:", solution


main()
