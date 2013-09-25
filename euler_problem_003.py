# Created by Ingrid Avendano on 9/23/13. 
#
#
# Project Euler - Problem 3:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math 

num = 600851475143
# num = 13195


# checks for highest prime factor
def highestPrimeFactor(x):
	i = 2

	# only increment through numbers that are less than half of
	# the original number 
	while i*i < x:
		print "i is: %d" % i

		# checks if the number incremented is divisible by number
		while x%i == 0:
			x = x/i 

		print "x is now: %d" % x

		i += 1

	return x


print highestPrimeFactor(num)
