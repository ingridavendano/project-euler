# Created by Ingrid Avendano on 11/5/13. 
#
#
# Project Euler - Problem 41: Pandigital prime
#
# We shall say that an n-digit number is pandigital if it makes use of all the 
# digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is 
# also prime.
#
# What is the largest n-digit pandigital prime that exists?

from math import factorial

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
	top = factorial(16)
	bottom = factorial(4) * factorial(12)

	print top/bottom

	# print "Solution to problem 41:", solution
	

main()
