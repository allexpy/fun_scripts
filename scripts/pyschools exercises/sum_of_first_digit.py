"""
Sum Of First Digit

Write a function getSumOfFirstDigit(numList) that takes in a list of positive numbers and returns the sum of all the first digit in the list.

Examples
>>> getSumOfFirstDigit([12, 23, 34, 45, 56])
15
>>> getSumOfFirstDigit([1, 23, 456, 7890])
14
>>> getSumOfFirstDigit([])
0
"""


def getSumOfFirstDigit(num):
	sum_list = [str(i)[0] for i in num]
	x = [int(a) for a in sum_list]
	return sum(x)
