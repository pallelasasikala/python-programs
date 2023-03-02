#find : Three digit number followed by space followed by two digit number
'''import re
str = '12345 123 896 908 99765'
a=re.findall(r'\b[0-9]{3} [0-9]{2}\b',str)
print(a)'''


# to print vowels present in given string
'''import re
a="Happy birthday"

s=re.findall("['a','e','i','o','u']",a)
print(s)'''

#Extracting numbers from a given string
'''import re
s="Welcome to 123 restaurant have a 8923 blast"
d=re.findall(r'\d+',s)
print(d)'''



'''#to print all substrings
import re
s='Twelve:12 Eighty nine:89 thirty-two:32'
#d=re.findall(r'a[A-Za-z\-\s]+',s)
d=re.findall(r'([\D]+):',s)
print(d)'''


#Remove white spaces
'''import re
string = 'abc 12\
de 23 \n f45 6'
d=re.findall(r'\S+',string)
print(d)
'''


#Given string is present or not
'''import re
a="Python is easy to learn ..but only if you practice Python it can be easy"
b=re.findall(r'Python',a)
print(b)'''









'''import re
a="he is a good boy,quiet and punctual guy ,boy "
s = re.compile([^g],a)
matches=s.findall(a)
print(matches)'''