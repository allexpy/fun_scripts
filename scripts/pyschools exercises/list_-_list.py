"""Function (x, y) that takes in two lists as arguments and returna list
that is the result of removing elements from list1 that can be found in y."""

def subtractList(x, y):
	return sorted(list(set(x) - set(y)))
