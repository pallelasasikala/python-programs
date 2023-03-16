 #to print all the even numbers from 1 to 20
'''for i in range(1, 21):
    if i % 2 == 0:
        print(i)'''
# to print all the odd numbers from 1 to 20
'''for i in range(1, 21):
    if i % 2 != 0:
        print(i)'''
#to print all the multiples of 3 from 1 to 30 
'''for i in range(1, 31):
    if i % 3 != 0:
        continue
    print(i)'''
# to print the sum of all even numbers from 1 to 20
'''sum = 0
for i in range(1, 21):
    if i % 2 != 0:
        continue
    sum += i
print("The sum of all even numbers from 1 to 20 is:", sum)'''

# to print the first 10 even numbers

'''count = 0
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
        count += 1
    if count == 10:
        pass'''

#to print the grade of a student based on the marks

'''
marks = int(input("Enter the marks obtained: "))

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B+")
elif marks >= 60:
    print("Grade: B")
elif marks >= 50:
    print("Grade: C+")
elif marks >= 40:
    print("Grade: C")
else:
    print("Failed!")'''

# Program to check whether a given number is positive, negative or zero

'''num = float(input("Enter a number: "))
if num>0:
    print(num, "is positive")
elif num<0:
    print(num, "is negative")
else:
    print(num, "is zero")'''

#  Program to print the multiplication table of a given number

'''num = int(input("Enter a number: "))
for i in range(1,11):
    print(num, "x", i, "=", num*i)'''


# Program to print the first 10 natural numbers

'''for i in range(1,11):
    pass
    print(i)'''
