"""Remove Vowels

Write the function removeVowels(word) that removes all the vowels ('a', 'e', 'i', 'o', 'u')
 in a word and returns the remaining letters in the word.

Examples

>>> removeVowels('apple')
"ppl"
>>> removeVowels('Apple')
"ppl"
>>> removeVowels('Banana')
'Bnn'
"""

def removeVowels(word):
	vowels = ['a','e','i','o','u','A','E','I','O','U']
	return ''.join(c for c in word if c not in vowels)
