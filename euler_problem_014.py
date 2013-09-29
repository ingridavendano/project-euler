# Created by Ingrid Avendano on 9/29/13. 
#
#
# Project Euler - Problem 14: Longest Collatz sequence
#
# The following iterative sequence is defined for the set of positive integers:
#
# n --> n/2 (n is even)
# n --> 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# It can be seen that this sequence (starting at 13 and finishing at 
# 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), 
# it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.


def collatz_sequence(n):
	chain_length = 1 
	# chain_nums = []

	while n > 1:
		if n%2 == 0:
			n = n/2
		else: 
			n = n*3 + 1
		# chain_nums.append(n)
		chain_length += 1

	return chain_length


def main():
	longest_chain = 0
	longest_chain_num = 0

	for i in range(1,1000000):
		chain = collatz_sequence(i)
		if chain > longest_chain:
			longest_chain = chain
			longest_chain_num = i

	print "Solution to problem 14:", longest_chain_num


main()