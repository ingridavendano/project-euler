# Created by Ingrid Avendano on 9/28/13. 
#
#
# Project Euler - Problem 10: Summation of primes
#
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.


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
	solution = 0
	i = 2

	while i < 2000000:
		if is_a_prime(i):
			solution += i
		i += 1

	print "Solution to problem 10:",solution


main()