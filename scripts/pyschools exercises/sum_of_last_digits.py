"""
Function getSumOfLastDigits() takes in a list of positive numbers
and returns the sum of all the last digits in the list

Examples

>>> getSumOfLastDigits([2, 3, 4])
9
>>> getSumOfLastDigits([1, 23, 456])
10

"""

def getSumOfLastDigits(numList):
	x = 0
	for item in numList:
		x += int(str(item)[-1])
	return x
