"""
Pairwise Comparison Of DNA Sequences.

Pairwise comparision of DNA sequences is a popular technique used in Bioinformatics.
It usually involves some scoring scheme to express the degree of similarity.
Write a function that compares two DNA sequences based on the following scoring
scheme: +1 for a match, +3 for each consecutive match and -1 for each mismatch.

Examples

>>> print pairwiseScore("ATTCGT", "ATCTAT")
ATTCGT
||   |
ATCTAT
Score: 2
>>> print pairwiseScore("GATAAATCTGGTCT", "CATTCATCATGCAA")
GATAAATCTGGTCT
 ||  |||  |
CATTCATCATGCAA
Score: 4
>>>

"""

def pairwiseScore(seqA, seqB):
	score = 0
	prevMatch = ""
	for (A, B) in zip (seqA, seqB):
		if A == B:
			score += 3 if len(prevMatch) > 0 and prevMatch[-1] == '|' else 1
		else:
			score -= 1
		prevMatch += '|' if (A == B) else ' '
	return "{}\n{}\n{}\nScore: {}".format(seqA, prevMatch, seqB, score)
