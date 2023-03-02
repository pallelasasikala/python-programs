'''s = 'toy'
p = []
for i in s:
    p.append(i+i)
    print(*p)'''


'''d = {"a": 1, "b": 2, "c": 3}
s = {}
for k,v in d.items():
    if v <= 1:
        print(d.items())
        print(s)'''

'''a=int(input("Enter a num :"))
value=0
for i in range(1,a+1):
  value=value+i
print("sum of N natural numbers is:",a)'''


'''data = {'name1': "january", 'name2':"feb", 'name3':"march"}
for i in range(1,10):
    n=input("do you want to perform the task yes/no:")
    if n=="yes":
        str1 = input("enter a name")
        if str1 in data.keys():
            print("name exists in the dict and its value is:",data[str1])
        elif:
            data[str1]="new month"
            print("new data is:",data)
    else:
        print("thanks")
        break'''



'''
l={'name':'cat','age':2,'gender':'f'}
s=['name','cat','age','gender','address']
for s in l:
    if s not in l:
        print("item is in dict",l)
    else:
        print("adress is not present in l")
        break 
print(l.items())'''


'''D={'name':'cat','age':2,'gender':'f'}
L=['name','age','gender','address']
for item in L:
    if item in D.keys():
        print(f'key:{item}, value:{D[item]}')
    else:
        print(f'{item} is not in list D')'''

