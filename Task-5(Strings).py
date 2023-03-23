'''# to print all vowels in the sentence in the same order

sentence=" I LOVE CODING"
vowels=['A','E','I','O','U']
s=[]
for i in sentence:
     if i in vowels:
         s.append(i)
         print(s)'''

#string split
#str1 = "I am walking in the park with the pond in it"set1= set(str1.split())
'''str1="hai welcome to python best programming best is python"
list1=str1.split(" ")

print(set(list1))'''

# reverse a string
'''
a="abcdefghijk"
s=a[0:4]
print(s)
b=a[10:3:-1]
print(b)
d=s+b
print(d)
#copy a sting to another string
a="hi"
b="hello"
#=print(" {} is one string ,{} is another string".format(a,b))
d= a+'  '+''.join(b)
print(d)

s='a1b2c3'
i=()'''
#b=s.find('a-z')
#print(b)



# remove whitespace in a string with no space and $
'''
a='abc 12\n de 23 \n  f45 6'
#s=a.replace(" ","")
s=a.replace(" ",'$')
print(s)'''

# to check whether the given word is there in string or not
'''a="Python is easy to learn ..but only if you practice Python it can be easy"

if 'Python' in a :
    print(" python is there in b")
else:
    print("python not there in b")'''

# to print number from a given string
'''a=input("Enter your string: ")
#a = "There are 8 monkeys sitting on 4 trees"
print("The original string : " + a)
b= [int(i) for i in a.split() if i.isdigit()]
print("The numbers list is : " + str(b))'''


#count how many times a letter appears in a string
'''a=input("Enter a letter:")
sentence="this is a sentence"
s=sentence.count(a)
if a in sentence:
  print("{} appeared {} times".format(a,s))
else:
    print("{} doesn't exist in sentence".format(a))'''


'''

str="I LOVE CODING"
vowels=['a','e','i','o','u']
c=[]
for i in str:
    if i in vowels:
        c.append(i)
        print(c)'''
# Reverse a string:
'''
string = "hello"
reversed_string = string[::-1]
print(reversed_string)'''

#Count the number of occurrences of a character in a string:

'''string = "hello world"
char = "l"
count = string.count(char)
print(count)'''

#Check if a string is a palindrome:


'''
string = "racecar"
reversed_string = string[::-1]
if string == reversed_string:
    print("Palindrome")
else:
    print("Not a palindrome")'''

#Split a string into a list of words:


'''string = "hello world"
words = string.split()
print(words)'''

#Join a list of words into a single string:
'''
a = ["sasi", "kala"]
string = " ".join(a)
print(string)'''


# Print the first three characters of a string:
'''
string = "hello world"
print(string[:3])'''

# Print the last three characters of a string:
'''
string = "hello world"
print(string[-3:])'''

# Print every other character of a string:

'''string = "hello world"
print(string[::2])
'''
# Print a substring between two indexes:
'''
string = "hello world"
print(string[3:8])'''

# Print a substring starting from an index and going until the end of the string:

'''string = "hello world"
print(string[6:])'''

# Print the last three characters of a string:

'''string = "hello world"
print(string[-3:])
'''
#  Print every other character of a string in reverse order:

'''string = "hello world"
print(string[::-2])'''

#  Print a substring between two indices in reverse order:

'''string = "hello world"
print(string[8:3:-1])'''

#  Print a substring starting from an index and going until the beginning of the string:
'''
string = "hello world"
print(string[6::-1])'''

# Print a substring starting from an index and going backwards until the end of the string:

'''
string = "hello world"
print(string[:-5:-1])'''