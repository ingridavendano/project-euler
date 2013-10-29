# Created by Ingrid Avendano on 10/29/13. 
#
#
# Project Euler - Problem 34: Digit factorials
#
# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the 
# factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.


# converts a number *str* into a factorial number
def factorial(number_str):
	total = 1
	for number in range(1,int(number_str)+1):
		total *= number

	return total


# finds the factorial of every digit in a number
def factorial_sum(num):
	str_num = str(num)
	total = 0

	for digit in str_num:
		total += factorial(digit)

	return total


def main():
	sum_of_factorial_numbers = 0

	# both 1! and 2! don't count so start at 3 to a million
	for number in range(3,1000001):
		number_factorial_sum = factorial_sum(number)

		# check to see if the factorial of a number is the number
		if number_factorial_sum == number:
			sum_of_factorial_numbers += number

	print "Solution to problem 34:", sum_of_factorial_numbers
	

main()
