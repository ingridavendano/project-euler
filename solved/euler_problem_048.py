# Created by Ingrid Avendano on 10/28/13. 
#
#
# Project Euler - Problem 48: Self powers
#
# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.


def main():
	numbers = range(1,1001)
	total = 0

	for number in numbers:
		total += (number**number)

	str_number = str(total)

	# find the last 10 numbers
	solution = str_number[-10:]

	print "Solution to problem 48:", solution


main()
