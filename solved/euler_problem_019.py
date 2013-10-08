# Created by Ingrid Avendano on 9/29/13. 
#
#
# Project Euler - Problem 19: Counting Sundays
#
# You are given the following information, but you may prefer to do some
# research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a 
# century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth 
# century (1 Jan 1901 to 31 Dec 2000)?


def days_in_month(month, year):
	# checks if month is September,April, June and November.
	if month in [9,4,6,11]:
		return 30
	# check January, March, May, July, August, October, December
	elif month in [1,3,5,7,8,10,12]:
		return 31
	# check for February 
	elif month is 2:
		if year%4 == 0:
			return 29
		else:
			return 28
	return 0


def sunday_counter(days):
	if days % 7 == 0:
		return 1
	return 0


def main():

	years = 99
	starting_date = 1
	ending_date = 31

	total_number_of_days = 1
	total_sundays = 0
	for year in range(1901,2000):
		for month in range(1,13):
			total_number_of_days += days_in_month(month, year)
			total_sundays += sunday_counter(total_number_of_days)

	print "Solution to problem 19:", total_sundays


main()