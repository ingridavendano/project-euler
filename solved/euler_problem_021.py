# Created by Ingrid Avendano on 10/2/13. 
#
#
# Project Euler - Problem 21: Amicable numbers
#
# Let d(n) be defined as the sum of proper divisors of n (numbers less 
# than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a != b, then a and b are an amicable 
# pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 
# 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284
# are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.


# goes through to find all the divisors for a particular number
# adds all those divisors
def sum_of_divisors(number):
	divisors = []
	total = 0

	for num in range(1,number/2 + 1):
		if number%num == 0:
			total += num
			divisors.append(num)

	return total


def main():
	amicable_pairs = {}
	number_of_pairs = 0
	pairs = []
	total = 0

	for number in range(0,10000):
		amicable_pairs[number]=sum_of_divisors(number)

	for first_key in amicable_pairs.keys():
		value = amicable_pairs[first_key]

		if value != 1 and value <= 10000:
			if value != sum_of_divisors(value):
				second_key = amicable_pairs[value]

				if first_key == second_key:
					pairs.append(first_key)

	print "Solution to problem 21:", total


main()
