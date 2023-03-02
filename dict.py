'''#to add values of all keys
d = {"a": 1, "b": 2, "c": 3}
#print(d["a"]+d["b"]+d["c"])
#a=d.values()
#print(sum(a))
print(sum(d.values()))'''


'''#to print key value of b and to add c key and 3 as its value
d = {"a": 1, "b": 2}
print(d["b"])
d["c"] = 3
print(d)'''


'''
# to print a dict with items a,b and 1,2 
s = {'a':1,'b':2}
e = dict(c=1,d=2)
print(s)
print(e)'''

'''
#to remove duplicates in a 
a = ["1", 1, "1", 2]
print(list(set(a)))'''






'''a={'harini':'April 13','srivani':'oct 13','ravi':'nov 13'}
b={}
for i in a:
    if i.keys not in a :
        print("{} is prsent in {} ".format(keys,a[i]))
    else:
        print("")'''
D={'name':'cat','age':2,'gender':'f'}
L=['name','age','gender','address']
#get method
import pprint
D={'name':'cat','age':2,'gender':'f','zebra':1,'apple':4}
pprint.pprint(D)
#set default
'''a={'apple':1,'banana':3,'pear':5,'papaya':2}
print(a.keys()) # to print only keys
print(a.values()) # to print only values
print(a.items()) # to print only items
for b,c in a.items(): # to print keys whose value is >2
    if c > 2:
        print(b)'''