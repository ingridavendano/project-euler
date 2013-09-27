# Created by Ingrid Avendano on 9/25/13. 
#
#
# Project Euler - Problem 5:
#
# 2520 is the smallest number that can be divided by each of the numbers 
# from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of 
# the numbers from 1 to 20?

# goes through to find all the factors for a particular number
def factors_of_each_number(num):
	original_num = num
	factors = []
	i = 2

	while i*i <= num:
		# checks if the number incremented is divisible by number
		while num%i == 0:
			factors.append(i)
			num = num/i 
		i += 1

	# checks to see if the number had any factors besides 1
	if original_num%num == 0:
		factors.append(num)

	return factors


# creates a list of factors that are primary numbers
def list_prime_number_factors(num):
	list_of_factors = []

	# creates a list of factors for each number from 1 to n
	for i in range(1,num):
		factors = factors_of_each_number(i)

		# checks to see if number is not already in the list
		# if it is not in the list then it is added to the list
		for i in factors:
			if i not in list_of_factors:
				list_of_factors.append(i)

	return list_of_factors


# finds the highest power of a primary factor
def list_factors_of(num):
	factors = list_prime_number_factors(num)

	for i in range(len(factors[1:])):
		base = factors[i+1]
		power = 1

		while base**power < num:
			factors[i+1] = base**power
			power += 1
	
	return factors


# finds the product of all the factors
def find_smallest_product(factors):
	product = 1
	for i in factors:
		product *= i

	return product


# set the number range in list_factors
def main():
	factors = list_factors_of(20)
	solution = find_smallest_product(factors)

	print "Solution to problem 5:", solution


main()
