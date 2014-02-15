 # Created by Ingrid Avendano on 10/2/13. 
#
#
# Project Euler - Problem 24: Lexicographic permutations
#
# A permutation is an ordered arrangement of objects. For example, 
# 3124 is one possible permutation of the digits 1, 2, 3 and 4. If 
# all of the permutations are listed numerically or alphabetically, 
# we call it lexicographic order. The lexicographic permutations of 
# 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 
# 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# def lexicographic(list_of_digits, variations, depth):

# 	if depth == len(list_of_digits):
# 		return variations

# 	depth += 1

# 	numbers = list_of_digits
	
# 	for i in range(len(variations)):
# 		for digit in numbers:
# 			if not digit in variations[i]:
# 				potential_variation = variations[i] + digit
# 				if not potential_variation in variations:
# 					variations[i] = potential_variation
# 					break

# 	# print "depth:", depth
# 	# for variation in variations:
# 	# 	print variation

# 	return lexicographic(list_of_digits, variations, depth)


def main():
	# print "Solution to problem 24:"


main()
