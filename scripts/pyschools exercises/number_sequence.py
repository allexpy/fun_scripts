"""
Number Sequence

Write a function getNumbers(number) that takes in a number as argument and return a list of numbers as shown in the samples given below.

Examples

>>> getNumbers(10)
[100, 64, 36, 16, 4, 0, 4, 16, 36, 64, 100]
>>> getNumbers(9)
[81, 49, 25, 9, 1, 1, 9, 25, 49, 81]
>>> getNumbers(8)
[64, 36, 16, 4, 0, 4, 16, 36, 64]
>>> getNumbers(0)
[0]
"""

def getNumbers(num):
	x = -num
	y = list(range(x, num+1, 2))
	return [i**2 for i in y]
