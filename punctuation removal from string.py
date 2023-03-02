# Python Program to Remove Punctuation from a String
punctuations="''''''!@#$%^&?*()_+,."
a=input("Enter the string:")
s=""
for c in a:
    if c not in punctuations:
        s+=c
print(s)