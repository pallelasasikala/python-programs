#random.randint() method returns a random integer between the specified integers.
'''import random
#random.randint(1,100)
random.randrange(1, 10)'''

import random
#Getting random value with choice
'''l=[10,20,30,40,50]
print(random.choice(l))'''

#Getting random values with choices
'''l=[10,20,30,40,50]
print(random.choices(l,k=3))
print(random.choices(l,k=4))'''

#Getting random value with in the range
'''print(random.randrange(10,15,2))'''

'''print(random.random())'''

#Getting random values in given list
'''l=[10,20,30,40,50]
random.shuffle(l)
print(l)'''

#Getting random object value in the given range
'''print(random.uniform(10,15))'''