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


# create a matrix and display how many routes it takes for each 
# column and row and build the following columns and rows off that
def lattice(columns, rows):
	# creates an empty matrix of zeros
	matrix = [[0 for col in range(columns)] for row in range(rows)]

	for col in range(columns):
		for row in range(rows):
			# base cases matrix[0][0]
			if row == 0 and col == 0:
				matrix[col][row] = 2
			# deals with the column on the far left
			elif row == 0:
				matrix[col][row] = 1 + matrix[col-1][row]
			# builds up the number of routes made from adjacent routes
			elif 0 < row and row < col:
				matrix[col][row] = matrix[col][row-1] + matrix[col-1][row]
			# doubles the route before it 
			elif col == row:
				matrix[col][row] = 2 * matrix[col][row-1]

	# # prints the matrix all pretty
	# for row in matrix:
	# 	print row

	return matrix[columns-1][rows-1]


def main():
	solution = lattice(20,20)
	print "Solution to problem 15:", solution

main()
