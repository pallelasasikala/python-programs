import re
a=input("Enter your email")
s=re.match(r'\w+[.]\w+[@]\w+[.com]',a)

print(s)