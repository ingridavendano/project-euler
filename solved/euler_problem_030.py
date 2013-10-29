# Created by Ingrid Avendano on 10/29/13. 
#
#
# Project Euler - Problem 30: Digit fifth powers
#
# Surprisingly there are only three numbers that can be written as the 
# sum of fourth powers of their digits:
#
# 1634 = 1^4 + 6^4 + 3^4 + 4^4
# 8208 = 8^4 + 2^4 + 0^4 + 8^4
# 9474 = 9^4 + 4^4 + 7^4 + 4^4
# As 1 = 1^4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of 
# fifth powers of their digits.


# finds the sum of fifth powers of digits in a number
def fifth_power_sum(num):
	str_num = str(num)
	total = 0

	for digit in str_num:
		total += (int(digit)**5)

	return total


def main():
	sum_of_fifth_digit_power_numbers = 0

	# both 1! and 2! don't count so start at 3 to a million
	for number in range(2,1000001):
		sum_of_digit_powers = fifth_power_sum(number)

		# check to see if the factorial of a number is the number
		if sum_of_digit_powers == number:
			sum_of_fifth_digit_power_numbers += number
			print number

	print "Solution to problem 30:", sum_of_fifth_digit_power_numbers
	

main()
