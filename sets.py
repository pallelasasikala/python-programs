# printing common things
a = {"cakes", "choclates", "biscuits", "cupcake"}
b = {"cupcake", "rice", "fruits", "vegetables", "choclates"}
c = a.intersection(b)
print(c)

'''#converting set to list
a={1,2,3,4,1,1,5,4}
b=list(a)
print(b)'''

# discard and remove methods in set used to remove elements
# difference is discard returns none if removed an element which is not there
'''remove throws key error
a={'sasi','hima','hari','swathi','sasi'}
#a.remove("sasi")
#a.discard("sasi")
a.remove("y")
print(a)
#clear
a={'sasi','hima','hari','swathi','sasi'}
a.clear()
print(a)'''

'''L=[1,2,2,3,4,4,5,5,6,1]
L1=[]
set(L)'''

'''birthdays = {'harini': 'April 13', 'srivani': 'oct 13', 'ravi': 'nov 13'}
L = {'leela': 'sep 13'}
user = input("Enter your name:")
if user in birthdays:
    print("IT is present and is on:")
else:
    birthdays.update(L)
    print("IT is not present and ")
    print(birthdays)
    '''

'''birthdays={'harini':'April 13','srivani':'oct 13','ravi':'nov 13'}

user=input("Enter your name:")
if user in birthdays:
    print("{}'s birthday is on {}".format(user, birthdays[user]))
else:
    L = input("{} is not found. Please enter the birthday: ".format(birthdays))
    birthdays[user]=L
    print(birthdays)'''



   ''' data = {'name1': "january", 'name2': "feb", 'name3': "march"}
    for i in range(1, 10):
        n = input("do you want to perform the task yes/no:")
        if n == "yes":
            str1 = input("enter a name")
            if str1 in data.keys():
                print("name exists in the dict and its value is:", data[str1])
            else:
                data[str1] = "new month"
                print("new data is:", data)
        else:
            print("thanks")
            break'''

'''    birthdays = {'harini': "April 12", "shravani": "oct 13", "ravi": "nov"}

    name = input("Enter a name: ")

    if name in birthdays.keys():
        print("{}'s birthday is on {}".format(name, birthdays[name]))
    else:
        birthday = input("{} is not found. Please enter the birthday: ".format(name))
        birthdays[name] = birthday
        print("{} is added to the dictionary with birthday {}".format(name, birthdays[name]))
        print(birthdays)
        '''




'''birthday={"hari":"april","sri":"oct","dev":"june"}
n=input("enter the name")
for i in birthday:
    if i==n:
        print("name exist in the dict and its value is ",birthday.get(n))
        break
    else:
        print("not matched")
        break
month=input("enter the month")
birthday.update({n:month})
print(birthday)
------------------------------------------------------

birthday={"harini":"aprial13","srivani":"oct21","ravi":"oct"}
n=(input("enter a name"))

for i in birthday:
    if i==n:
        print("birthdayis",birthday.get(n))
        break
    else:
        print("not matched than update")
        break
birthday.update({n:""})
month=input("enter mont")
birthday.update({n:month})
print(birthday)
'''

    '''
        a = int(input("Enter numbers: "))
        s = list(map(int, input().split()))
        s.sort()
        print(s[1])
        print(s[3])
        '''
    

       ''' a = ['1', 1, '1', 2]
        print(set(a))
    '''
