"""Introducing some string methods.


>>> greetings = "Hello World"
>>> greetings.lower() # convert to lower case
'hello world'
>>> greetings.find('o')  # return first occurence of character or substring
4
>>> greetings.replace('World', 'Everyone')
'Hello Everyone'
>>> spam = '    This sentence has leading and trailing spaces.   \n'
>>> spam
'    This sentence has leading and trailing spaces.   \n'
>>> spam.strip()
'This sentence has leading and trailing spaces.'
"""





str1  = 'abcefghxyzThis,is,the,target,string  xyzlkdjf'
idx1 = str1.find('xyz')                    # get the position of 'xyz'
idx2 = str1.find('xyz', idx1+1)            # get the next 'xyz'
str1 = str1[idx1+3:idx2].replace(',','|')    # replace ',' with '|'
str1 = str1.strip()                             # strip trailing spaces.
