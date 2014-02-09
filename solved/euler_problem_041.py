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


# checks for prime number
def is_prime(num):
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


def pandigital(num, total):
	num = str(num)
	num_sum = sum([int(i) for i in list(num)])

	if total[len(num)] == num_sum: 
		pandigital_prime = True

		for i in range(1, len(num)+1):
			if str(i) not in num:
				pandigital_prime = False
				break

		return pandigital_prime

	return False


def main():
	digit_sum = {}
	digit_total = 0
	solution = 0

	for i in range(1,10):
		digit_total += i
		digit_sum[i] = digit_total

	# guess range 
	for number in range(10000000, 1000000, -1):
		if is_prime(number): 
			if pandigital(number, digit_sum):
				solution = number 
				break 

	print "Solution to problem 41:", solution
	

main()
