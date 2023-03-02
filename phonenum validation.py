''''def phonenum():
    return p.match(s)
import re
s = input("Enter your phone number: ")
p = re.compile(r'\(\d{3}\)\s\d{3}[-]\d{4}')
if p.match(s):
    print("true")
else:
    print("false")
phonenum()'''
