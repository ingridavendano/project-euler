# Created by Ingrid Avendano on 9/28/13. 
#
#
# Project Euler - Problem 8: Special Pythagorean triplet
#
# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# 
# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


import math


def main():

	# equations to use:
	#	(1) c = 1000 - a - b
	# 	(2) c = sqrt(a^2 + b^2)

	solution = 0

	for a in range(1,1000):
		for b in range(1,1000):
			eqn1 = 1000 - a - b
			eqn2 = math.sqrt(a**2 + b**2)

			if eqn1 == eqn2:
				c = eqn1
				solution = a*b*c

	print "Solution to problem 9:",solution


main()