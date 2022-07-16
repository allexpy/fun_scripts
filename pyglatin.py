pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha(): #if there is a word and there are no numbers
    word = original.lower() #make the word lowercase
    first = word[0] #capture the first letter
    new_word = word + first + pyg #concatenate first letter with the word and ay
    new_word = new_word[1:len(new_word)] #eliminate the first letter
    print new_word 
else:
    print 'empty'
