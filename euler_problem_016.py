# Created by Ingrid Avendano on 9/29/13. 
#
#
# Project Euler - Problem 16: Power digit sum
#
# 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2^1000?


def main():
	solution = 0
	number = 2**1000
	str_of_digits = str(number)

	# converts array of characters to int to sum up for a solution
	for digit in str_of_digits:
		solution += int(digit)

	print "Solution to problem 16:",solution

main()