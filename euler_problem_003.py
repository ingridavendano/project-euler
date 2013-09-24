# Created by Ingrid Avendano on 9/23/13. 
#
#
# Project Euler - Problem 3:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


num = 600851475143
# num = 13195

# checks if a number is prime
def isPrime(x):
	result = True

	for i in range(2,x):
		if x%i==0:
			result = False

	return result

# finds prime factors
def largestPrime(x):
	factor = 1
	prime = 1

	for i in range(1,x):
		if x%i==0: 
			factor = i
			if isPrime(factor):
				prime = factor
				print i
	return prime

# do not run - it will take forever
largestPrime(num)
