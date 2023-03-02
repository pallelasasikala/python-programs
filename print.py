'''x = ("apple", "banana", "cherry")
print(x) '''
#sep='separator' 	Optional. Specify how to separate the objects, if there is more than one. Default is ' '
print("Hello", "how are you?", sep="---")

# code for disabling the space
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('Biriyani', 'Hyderabad', sep='@')

print('G', 'F', sep='', end='')
print('G')
# \n provides new line after printing the year
print('09', '12', '2016', sep='-', end='\n')

print('Hyderabad', 'Biriyani', sep='', end='@')
print('so Delicious')

# using a comma separator
print('apples', 'oranges', 'bananas', sep=', ')
# output: apples, oranges, bananas

# using a semicolon separator
print('one', 'two', 'three', sep=';')
# output: one;two;three

# using an emoji separator
print('????', '????', '????', sep='????')
# output: ????????????????????