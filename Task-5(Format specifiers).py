#%s - Used to format a string.

'''name = "John"
print("Hello, %s!" % name)'''

#Output: Hello, John!

#%d - Used to format an integer.

'''age = 25
print("You are %d years old." % age)'''

#Output: You are 25 years old.

#%f - Used to format a float.

'''price = 9.99
print("The price is %.2f dollars." % price)'''

#Output: The price is 9.99 dollars.

# %x - Used to format an integer as a hexadecimal string.

'''
number = 255
print("The hexadecimal representation of %d is %x." % (number, number))'''

#Output: The hexadecimal representation of 255 is ff.

#%c - Used to format a character.

'''letter = 'a'
print("The character is %c." % letter)'''

#Output: The character is a.

#  %o - Used to format an integer as an octal string.
'''
number = 8
print("The octal representation of %d is %o." % (number, number))'''

#Output: The octal representation of 8 is 10.

#%e - Used to format a float in scientific notation.

'''value = 123456789.12345
print("The value is %.2e." % value)'''

#Output: The value is 1.23e+08.

# Python 3 also introduced a new way of formatting strings using f-strings.

'''name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")'''

#Output: My name is John and I am 25 years old.

#In f-strings, the variables are enclosed in curly braces {} and their values are inserted into the string at runtime.
# You can also use format specifiers with f-strings. For example:

'''
price = 9.99
print(f"The price is {price:.2f} dollars.")'''

#Output: The price is 9.99 dollars.