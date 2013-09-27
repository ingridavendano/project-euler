# Created by Ingrid Avendano on 9/24/13. 
#
#
# Project Euler - Problem 4:
#
# A palindromic number reads the same both ways. The largest palindrome made 
# from the product of two 2-digit numbers is 9009 = 91 x 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_a_palindrone(num):
	num = str(num)
	length_of_num = len(num)
	result = True

	# checks digits from the beginning against those at the end to see if they 
	# match each other
	for i in range(length_of_num/2):

		if num[i] != num[-1-i]:
			result = False
			break

	return result


def main():
	# start with the highest three digit numbers
	highest_palindrone_product = 0
	product = 0

	# iterate through 999 to 0
	for i in range(999,99,-1): 

		# iterate through whatever i is to 0
		for j in range(i,99,-1):
			product = i*j
			# count += 1

			# checks if product is the highest valued palidrone
			if is_a_palindrone(product):
				if product > highest_palindrone_product:
					highest_palindrone_product = product

	print "Solution to problem 4:", highest_palindrone_product
	

main()
