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


import time

# TODO: make it not so long
def lattice(d, r):
  if r <= 0 and d <= 0:
     return 1
  possibles = 0
  if r > 0:
      possibles += lattice(d, r-1)
  if d > 0:
      possibles += lattice(d-1, r)
  return possibles


def main():

	solution = lattice(20,20)
	print "Solution to problem 15:", solution


main()
