'''import re

a = input("Enter your pin:")
s = re.compile(r'^\d{4}$')
t = re.compile(r'^\d{6}$')
if s.match(a) or t.match(a):
    print("valid")
else:
    print("invalid")'''
