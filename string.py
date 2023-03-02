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
