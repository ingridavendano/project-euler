# Created by Ingrid Avendano on 10/1/13. 
#
#
# Project Euler - Problem 20: Factorial digit sum
#
# n! means n x (n - 1) x ... x 3 x 2 x 1
#
# For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!


def main():
	n = 100
	factorial = 1

	for i in range(n):
		factorial *= (n - i)

	factorial_str = str(factorial)

	solution = 0
	for i in range(len(factorial_str)):
		solution += int(factorial_str[i])

	print "Solution to problem 20:", solution


main()