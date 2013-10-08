# Created by Ingrid Avendano on 10/2/13. 
#
#
# Project Euler - Problem 22: Names scores
#
# Using names.txt (right click and 'Save Link/Target As...'), a 46K text 
# file containing over five-thousand first names, begin by sorting it into 
# alphabetical order. Then working out the alphabetical value for each name, 
# multiply this value by its alphabetical position in the list to obtain a 
# name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which 
# is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, 
# COLIN would obtain a score of 938 x 53 = 49714.
#
# What is the total of all the name scores in the file?


def main():
	# read txt file with triangle of numbers
	text_file = open("../data/names.txt")
	triangle = text_file.read()
	text_file.close

	# separates items in a list 
	names = sorted(triangle[1:-1].split("\",\""))

	rank = 1
	total_scores = 0

	for name in names:
		score = 0
		for letter in name:
			score += (ord(letter) - 64)

		score *= rank
		total_scores += score
		
		rank += 1
	
	print "Solution to problem 22:",total_scores


main()
