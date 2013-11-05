# Created by Ingrid Avendano on 10/31/13. 
#
#
# Project Euler - Problem 28: Number spiral diagonals
#
# Starting with the number 1 and moving to the right in a clockwise 
# direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
# formed in the same way?


# regular print function for a grid
def print_grid(grid):
	for row in grid:
		print row


# finds sum from left to right and right to left diagonals
def diganol_sum(grid):
	y = len(grid) - 1
	total = 0
	for i in range(len(grid)):
		total += grid[i][i]
		total += grid[i][y - i]

	# technically 1 in the middle is added twice so remove 1 in the end
	return total-1


# fills a grid with numbers recursively
def spiral_numbers(grid, size, offset, count):
	y = size - 1 
	x = len(grid) - 1

	if count > 0:
		# move along top right to left
		for i in range(size):
			grid[offset][offset+y-i] = count
			count -= 1
		# move along left side top to bottom
		for i in range(1,size):
			grid[offset+i][offset] = count
			count -= 1
		# move along bottom side left to right
		for i in range(1,size):
			grid[x-offset][i+offset] = count
			count -= 1
		# move along right side bottom to top
		for i in range(1,size-1):
			grid[x-offset-i][offset+y] = count
			count -= 1

		offset += 1
		grid = spiral_numbers(grid, size-2, offset, count)

	return grid


# makes an empty grid
def make_number_grid(size):
	grid = []
	for i in range(size):
		grid.append(['' for i in range(size)])

	return grid


def main():
	size = 1001
	numbers = size*size

	grid = make_number_grid(size)
	grid = spiral_numbers(grid, size, 0, numbers)
	# print_grid(grid)
	solution = diganol_sum(grid)

	print "Solution to problem 28:", solution
	

main()
