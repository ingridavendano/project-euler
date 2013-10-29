# Created by Ingrid Avendano on 10/28/13. 
#
#
# The nth term of the sequence of triangle numbers is given by, 
# t_n = (1/2)*n*(n+1); so the first ten triangle numbers are:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# By converting each letter in a word to a number corresponding to its 
# alphabetical position and adding these values we form a word value. For 
# example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value 
# is a triangle number then we shall call the word a triangle word.
#
# Using words.txt (right click and 'Save Link/Target As...'), a 16K text file 
# containing nearly two-thousand common English words, how many are 
# triangle words?


def read_in_words():
	text_file = open("data/words.txt")
	str_of_words = text_file.read()
	text_file.close()

	words = str_of_words.split(",")

	# strip the parentheses from each word
	for i in range(len(words)):
		words[i] = words[i][1:-1].lower()

	return words


def get_score_of_word(word):
	total = 0

	for letter in word:
		total += ord(letter)-96

	return total


def main():
	words = read_in_words()
	words_score = []

	numbers = range(1,21)
	triangle_numbers = []

	# create a list of triangle numbers from 1-20
	for n in numbers:
		num = int((1/2.)*n*(n+1))
		triangle_numbers.append(num)

	total_triangle_numbers = 0

	for word in words: 
		score = get_score_of_word(word)

		if score in triangle_numbers:
			total_triangle_numbers += 1

	print "Solution to problem 42:", total_triangle_numbers


main()
