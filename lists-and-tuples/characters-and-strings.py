s = 'This is just a sample text that could have been a million times longer.\n\nYours Johnny'
print(s)
#Count the number of characters including blank spaces.
print(len(s))

#Count the number of characters excluding blank spaces.
print(len(s) - s.count(' '))

#Count the number of words.
s2 = s.replace('\n\n', ' ').split(' ')
print(len(s2)) #Remove double space from string?