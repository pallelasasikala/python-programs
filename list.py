'''colours=['red','orange','blue','violet','white']
print(len(colours[0]))
for i in colours:
    if len[i]>5
        print

l=[1.0,1.5,9.0,10.7,2]
print(sorted(l))'''

'''a=['bread','biscuit','cupcake','pastry','pancake']
#a.reverse()
#print(a)
b=str(a)
#print(type(b))
b.find('p')
print(b)'''

'''#To print list of 1- 20 numbers
a = range(1,20)
print(list(map(str,a)))'''

'''#to print list of 1-200 with 10 skip
a=range(1,21)
print([10 * x for x in a])'''

'''letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
#print(letters[7:10])
print(letters[::2])'''


'''
# take an integer as i/p ,after which it should take  n number of i/p's in seperate lines
# & print list in order and zeros must be at the end of list
m=int(input("Enter no.of inputs"))
num=[]
zeros=[]
for i in range(m):
    s=list(map(int,input("Enter a number:").split()))
    if  s != 0 :
        num.append(s)
    else:
       zeros.append(s)
print(num+zeros)'''


# ->Remove empty strings from the list of strings @ method--1
'''a=[' ','apple','banana','gulabjamun','jelebi',' ','  ']
print(a.pop(0))
print(a.pop(5))
print(a.pop(-1))
print(a)'''


# method ---2
'''a=[' ','apple','banana','gulabjamun','jelebi',' ',' ']
while ' ' in a :
    a.remove(' ')
print(a)
'''
#method --3
'''a=[' ','apple','banana','gulabjamun','jelebi',' ',' ']
a=' '.join(a)
print(a)'''


'''
#->Iterate both lists simultaneously
sum=[1,2,3]
sub=[5,6,7]
for (a,b) in zip(sum,sub):
    print(a,b)'''


#->Concatenate two lists in the given order

'''a=[1,2,3,4]
b=[5,6,7,8]
c=a+b
print(c)'''
'''
a = ['1','2','3','4']
b = ['5','6','7','8']
#a=str(a)
#b=str(b)
c=a.join(b)
print(c)'''

#->Turn every item of a list into its square --- method 1
'''a=[1,2,3,4]
for i in a:
    print(i**2)'''

#method ---2
'''
for i in range(1,5):
    print(i*i)'''

#->Concatenate two lists index-wise
'''a=[1,2,3,4]
b=[5,6,7,8]
for i, j in zip(a, b):
    print(i,j)

'''
#->Reverse a list
'''a=[1,2,3,4]
a.reverse()
print(a)'''

'''a=[1,2,3,4]
a.sort(reverse=True)
print(a)'''

'''a=[1,2,3,4]
b=a[::-1]
print(b)'''



'''letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[0::2])'''
'''picnicItems = {'apples': 5, 'cups': 2}
a='I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.'
print(a)'''

#removing duplicates
a=[1,2,3,4,1,1,5,4]
b=set([1,2,3,4,1,1,5,4])
print(b)
c=list(b)
print(c)

'''#updating set from list**
# can update set from list but not list to set
a={1,2,3,4,5}
b=[6,7,8]
set(b)
a.update(b)
print(a)'''

L= ['aaa','red','round','ccc','road','orange']
L1=[]
for i in L:
    if len(i)>=3 and i[0]=='r':
        L1+=[i]
    else:
        continue
print(L1)
******
L= ['aaa','red','round','ccc','road','orange']
L1=[]
for i in L:
    if len(i)>=3 and i.startswith('r'):
        L1.append(i)
print(L1)


'''d={'a':1,'b':2}'''
'''a=int(input("Enter number: "))
b=list(map(int,input().split()))
c=b[:5]
print(c)

#d=(b[5:10:-1]) #+b[:5]
#c.append(d)
d=b[10:4:-1]
print(d)
s=c+d
print(s)'''



'''a=input("Enter a watchman ID:   ")
c=[]
for i in range(1,len(a)):
    b=a[i:]+a[:i]
    a=a.lstrip("0")
    c.append(b)
print(*c)'''

