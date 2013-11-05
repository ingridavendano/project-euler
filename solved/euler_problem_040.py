# Created by Ingrid Avendano on 10/31/13. 
#
#
# Project Euler - Problem 40: Champernowne's constant
#
# An irrational decimal fraction is created by concatenating the 
# positive integers:
#
# 0.123456789101112131415161718192021...
#
# It can be seen that the 12th digit of the fractional part is 1.
#
# If dn represents the nth digit of the fractional part, find the 
# value of the following expression.
#
# d_1 x d_10 x d_100 x d_1000 x d_10000 x d_100000 x d_1000000


def main():
	numbers = range(1,1000000)
	str_fraction = "0."
	d = [1, 10, 100, 1000, 10000, 100000, 1000000]
	solution = 1

	for number in numbers:
		str_fraction = str_fraction + str(number)

	for number in d:
		# +1 for shift in "0.1" str added at the beginning
		digit = int(str_fraction[number + 1]) 
		solution *= digit

	print "Solution to problem 40:", solution
	

main()
