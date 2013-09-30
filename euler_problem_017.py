# Created by Ingrid Avendano on 9/29/13. 
#
#
# Project Euler - Problem 17: Number letter counts
#
# If the numbers 1 to 5 are written out in words: one, two, three, four, five,
# then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out 
# in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and 
# forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 
# 20 letters. The use of "and" when writing out numbers is in compliance with 
# British usage.


def word_for_one_to_nine(x):
	if x == 0:
		return ""
	elif x == 1:
		return "one"
	elif x == 2:
		return "two"
	elif x == 3:
		return "three"
	elif x == 4:
		return "four"
	elif x == 5:
		return "five"
	elif x == 6:
		return "six"
	elif x == 7:
		return "seven"
	elif x == 8:
		return "eight"
	elif x == 9:
		return "nine"


def word_for_twenty_plus(x):
	if x == 0:
		return ""
	elif x == 1:
		return ""
	elif x == 2:
		return "twenty"
	elif x == 3:
		return "thirty"
	elif x == 4:
		return "forty"
	elif x == 5:
		return "fifty"
	elif x == 6:
		return "sixty"
	elif x == 7:
		return "seventy"
	elif x == 8:
		return "eighty"
	elif x == 9:
		return "ninety"


def word_for_ten_to_nineteen(x):
	if x == 0:
		return "ten"
	elif x == 1:
		return "eleven"
	elif x == 2:
		return "twelve"
	elif x == 3:
		return "thirteen"
	elif x == 4:
		return "fourteen"
	elif x == 5:
		return "fifteen"
	elif x == 6:
		return "sixteen"
	elif x == 7:
		return "seventeen"
	elif x == 8:
		return "eighteen"
	elif x == 9:
		return "nineteen"


def main():
	letter_count = len("onethousand")

	for hundred in range(0,10):
		word_of_number = ""

		for ten in range(0,10):

			for one in range(0,10):
				number = hundred*100 + ten*10 + one

				if hundred > 0:
					word_of_number += word_for_one_to_nine(hundred) + "hundred"

				if hundred > 0 and (one > 0 or ten > 0): 
					word_of_number += "and"

				if ten > 1:
					word_of_number += word_for_twenty_plus(ten)

				if ten == 1: 
					word_of_number += word_for_ten_to_nineteen(one)
				else: 
					word_of_number += word_for_one_to_nine(one)

				letter_count += len(word_of_number)
				word_of_number = ""

	print "Solution to problem 17:",letter_count


main()