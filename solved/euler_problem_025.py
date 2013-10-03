# Created by Ingrid Avendano on 10/2/13. 
#
#
# Project Euler - Problem 25: 1000-digit Fibonacci number
#
# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the first term in the Fibonacci sequence to contain 1000 digits?


def main():
	# Fibonacci series
	fn_1 = fn_2 = 1
	fn = fn_1 + fn_2
	n = 3

	while len(str(fn)) < 1000:
		fn_2 = fn_1
		fn_1 = fn
		fn = fn_1 + fn_2
		n += 1
		# print "F%d = %d" % (n, fn)

	print "Solution to problem 25:", n
	

main()