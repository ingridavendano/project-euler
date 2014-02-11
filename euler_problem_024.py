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
	nums = [str(i) for i in range(3)]
	shift = len(nums) - 2
	current = ""
	count = 0

	print nums[:shift] + nums[shift+1:] + [nums[shift]]
	while count < 10:
		print "".join(nums)
		if shift == len(nums) - 1:
			shift = 0


		nums = nums[:shift] + nums[shift+1:] + [nums[shift]]
		shift += 1
		count += 1

	# print "".join(nums)

	# size = 3
	# digits = []

	# for i in range(size):
	# 	digits.append(str(i))

	# variations = []
	# for digit in range(size):
	# 	for variety in range(size-1):
	# 		variations.append(str(digit))


	# print digits
	# list_of_variations = lexicographic(digits, variations, 1)

	# for number in list_of_variations:
	# 	print number

	# print "Solution to problem 24:"


main()
