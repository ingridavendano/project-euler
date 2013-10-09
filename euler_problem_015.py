# Created by Ingrid Avendano on 9/29/13. 
#
#
# Project Euler - Problem 15: Lattice paths
#
# Starting in the top left corner of a 2x2 grid, and only being able 
# to move to the right and down, there are exactly 6 routes to the bottom
# right corner.
#
# *** Image of grid at: http://projecteuler.net/problem=15
#
# How many such routes are there through a 20x20 grid?


def num_of_paths(grid_size):
	pass


def main():
	# read txt file with triangle of numbers
	text_file = open("/data/triangle.txt")
	triangle = text_file.read()
	text_file.close

	# separates items in a list 
	names = sorted(triangle.split())

	print "Solution to problem 15:"


main()
