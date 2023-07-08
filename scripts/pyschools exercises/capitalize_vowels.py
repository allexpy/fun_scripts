"""
Capitalize Vowels

Write the function capitalizeVowels(word) that returns the word with all the vowels capitalized.

Examples

>>> capitalizeVowels('apple')
'ApplE'
>>> capitalizeVowels('google')
'gOOglE'
"""

def capitalizeVowels(word):
	vowels = ['a','e','i','o','u']
	return ''.join(c.upper() if c in vowels else c.lower() for c in word)
