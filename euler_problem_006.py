# Created by Ingrid Avendano on 9/26/13. 
#
#
# Project Euler - Problem 6:
#
# The sum of the squares of the first ten natural numbers is:
#
# 1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is:
#
# (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
# Hence the difference between the sum of the squares of the first ten natural 
# numbers and the square of the sum is 3025 - 385 = 2640.
#
# Find the difference between the sum of the squares of the first one hundred 
# natural numbers and the square of the sum.

def main():
	sum_of_squares = 0
	total_sum = 0

	# iterates through 100 numbers
	for i in range(1,101):
		sum_of_squares += i**2
		total_sum += i

	square_of_sum = total_sum**2

	# finds difference between two sums
	diff_of_sums = square_of_sum - sum_of_squares

	print "Solution to problem 6:", diff_of_sums


main()