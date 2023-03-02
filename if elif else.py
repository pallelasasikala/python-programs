
'''s={"Harini":"April 13","Srivani":"Oct 13","Ravi":"Nov13","Tejaswini":"Oct6"}
a=input("Enter your name: ")

if a in s:
   #print("{} is present".format(a))
   #print("{} birthday is on {}".format(a,))
   print(a+ " birthday is on "+ s[a])
   t=print("Do you want to continue yes or no:")

   if t=="yes":
      a=input("Enter your name: ")
   else:
        print("Have a nice day")
      break
else:
   b=input("Enter your name: ")
   c=input("enter your dob: ")
   s.setdefault(b,c)
print(s)'''


s={"Harini":"April 13","Srivani":"Oct 13","Ravi":"Nov13","Tejaswini":"Oct6"}
a=input("Enter your name: ")
if a in s:
    # print("{} is present".format(a))
    # print("{} birthday is on {}".format(a,))
    print(a + " birthday is on " + s[a])

    t = input("Do you want to continue yes/no :")
    if t == "yes":
        a = input("Enter your name: ")
    else:
        print("Have a nice day")


    #print("Do you want to continue :")

else:
    b = input("Enter your name: ")
    c = input("enter your dob: ")
    s.setdefault(b, c)

print(s)