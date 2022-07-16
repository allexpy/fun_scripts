"""Invert Dictionary

Write a function invertDictionary(d) that takes in a dictionary as argument and
return a dictionary that inverts the keys and the values of the original dictionary.

Examples

>>> invertDictionary({'a':1, 'b':2, 'c':3, 'd':2})
{1: ['a'], 2: ['b', 'd'], 3: ['c']}
>>> invertDictionary({'a':3, 'b':3, 'c':3})
{3: ['a', 'c', 'b']}
>>> invertDictionary({'a':2, 'b':1, 'c':2, 'd':1})
{1: ['b', 'd'], 2: ['a', 'c']}
"""

def invertDictionary(d):
	x = {}
	for k, v in d.items():
		key = x.setdefault(v, [])
		key.append(k)
	return x
