"""
Change Case

Write the function changeCase(word) that changes the case of all the letters in a word and returns the new word.

Examples

>>> changeCase('aPPle')
"AppLE"
>>> changeCase('BaNaNa')
'bAnAnA'
"""

def changeCase(word):
	return ''.join(c.lower() if c.isupper() else c.upper() for c in word)
