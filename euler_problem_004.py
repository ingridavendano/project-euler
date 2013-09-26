# Created by Ingrid Avendano on 9/24/13. 
#
#
# Project Euler - Problem 4:
#
# A palindromic number reads the same both ways. The largest palindrome made from 
# the product of two 2-digit numbers is 9009 = 91 x 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def isPalindrone(x):
	x = str(x)
	length = len(x)
	result = True

	# checks digits from the beginning against those at the end to see if they 
	# match each other
	for i in range(length/2):
		if x[i] != x[length - 1 - i]:
			result = False
			break

	return result

# start with the highest three digit numbers
a = 999
b = 999
product = 0
highest_palindrone_product = 0

num1 = a
num2 = b

count = 0

# iterate through 999-0
for i in range(a,99,-1): 

	# iterate through 999-0
	for j in range(b,99,-1):
		product = i*j
		count += 1

		# checks if product is the highest valued palidrone
		if isPalindrone(product):
			if product > highest_palindrone_product:
				highest_palindrone_product = product
				num1 = i
				num2 = j

print "Solved! %d x %d = %d" % (num1,num2,highest_palindrone_product)
print "It took %d times" % count
