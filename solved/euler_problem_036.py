# Created by Ingrid Avendano on 10/29/13. 
#
#
# Project Euler - Problem 36: Double-base palindromes
#
# The decimal number, 585 = 10010010012 (binary), is palindromic 
# in both bases.
#
# Find the sum of all numbers, less than one million, which are 
# palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not 
# include leading zeros.)


def is_palindrome(num):
	num = str(num)
	palindrome = True

	for i in range(len(num)/2):
		if num[i] != num[-1-i]:
			palindrome = False
			break

	return palindrome


def main():
	numbers = range(1,1000000)

	palindromes = []
	sum_of_palidrones = 0

	for number in numbers:
		if is_palindrome(number):
			binary_num = bin(number)[2:]

			if is_palindrome(binary_num):
				palindromes.append(number)
				sum_of_palidrones += number

	print "Solution to problem 36:", sum_of_palidrones


main()
