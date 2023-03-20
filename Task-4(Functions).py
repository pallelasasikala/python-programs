#If we want to store the output of the method/function into a variable so that in further we can use that-
# data again and again then we go with return statement.
# while return is used to exit a function and return a value to the caller.
'''def sum(a,b):
    e=a+b
    return e
e=sum(2,3)
print(e)
f=e*5
print(f)
'''
#Return value and with Arguments
'''def even_or_odd(n):
    if n%2==0:
        return ('it is even')
    else:
        return ('it is odd')
result=even_or_odd(90)
print(result)'''


#No return value and without Argument
'''def even_or_odd():
    n=int(input('enter a number: '))
    if n%2==0:
        print('{} is even'.format(n))
    else:
        print('{} is odd'.format(n))
even_or_odd()'''


#Return value and without Argument
'''def even_or_odd():
    n=int(input('enter a number: '))
    if n%2==0:
        return ('{} is even'.format(n))
    else:
        return ('{} is odd'.format(n))
result=even_or_odd()
print(result)'''


#No return value and with Arguments
'''def even_or_odd(n):
    n=int(input('enter a number: '))
    if n%2==0:
        print('{} is even'.format(n))
    else:
        print('{} is odd'.format(n))
even_or_odd(30)'''

'''
def fun(address) :
    for i in address:
        if i%2==0 :
           continue
           print(i)
        else:
            print("not divisble by 2: ",i)
add=[1,2,3,4]
fun(add)'''

#A function that adds two numbers:
'''
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 7)
print(result)'''

#  A function that calculates the area of a rectangle:


'''def rectangle_area(width, height):
    return width * height

result = rectangle_area(3, 4)
print(result) 
'''
#A function that checks if a number is even or odd:

'''def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

result = is_even(5)
print(result) 
'''
# A function that prints a message a given number of times:
'''
def print_message(message, times):
    for i in range(times):
        print(message)

print_message("Hello", 3)'''

#A function that returns the maximum value from a list of numbers:


'''def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

result = find_max([2, 6, 3, 8])
print(result) '''



#to print unique values from a list
'''
def number():
    nums = [1, 2, 2, 3, 4, 5, 4, 4, 5, 5, 6, 7]
    nums1 = list()
    nums1.append(nums[0])
    for item in nums:
        if item != nums1[-1]:
            nums1.append(item)
            #return nums1
    print(nums1)
number()'''

#A function that converts Celsius to Fahrenheit:

'''def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

result = celsius_to_fahrenheit(20)
print(result)
'''
#A function that calculates the average of a list of numbers:
'''
def avg(numbers):
    sum_numbers = sum(numbers)
    count_numbers = len(numbers)
    average = sum_numbers / count_numbers
    return average
a = avg([4, 6, 8, 2])
print(a)
'''
#A function that checks if a string is a palindrome:

'''
def is_palindrome(string):
    reverse_string = string[::-1]
    if string == reverse_string:
        return True
    else:
        return False
result = is_palindrome("racecar")
print(result)'''

# A function that calculates the area and perimeter of a rectangle:

'''def rec_properties(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

c = rec_properties(4, 6)
print(c)'''
