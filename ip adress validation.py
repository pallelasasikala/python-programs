'''#check match of ip address  format
import re
s=input("enter ip address: ")
a=re.match(r'\d{3}.\d{3}.12\d{2}.\d{3}',s)
print(a)'''