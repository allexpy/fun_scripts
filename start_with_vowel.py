"""Returns a substring that starts with the first vowel found in the word.
The function returns 'No vowel' if the word does not contain vowel."""


def startWithVowel(word):
	vowels = ['a','e','i','o','u','A','E','I','O','U']

	vowels_list = [idx for idx, ch in enumerate(word) if ch in vowels]

	if len(vowels_list):
		a = vowels_list[0]

	if not vowels_list:
		return 'No vowel'
	else:
		return ''.join(x for x in word[a:])
