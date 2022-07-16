"""Search String

Write the function search(word, substring) that takes in a word and a substring as arguments
and returns the position (0 indexed) of the substring if it is found in the word.
The function returns -1 if the substring is not found.

Examples

>>> search("apple", 'p')
1
>>> search("google", 'apple')
-1
>>> search("google", 'p')
-1
>>> search("google", 'oo')
1
"""

def search(word, substring):
	x = re.search(substring, word)
	if x is None:
		return -1
	else:
		return word.index(substring)
