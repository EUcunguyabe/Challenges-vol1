#!/usr/bin/python3
#count number of vowels in a string
string=str(input("Enter any word:"))
vowels="AaIiUuEeOo"
count=0
for i in string:
    if i in vowels:
        count=count+1
        print (i, end=" ")
#print ("the vowels in a string are:",count) 
print(f"\nNumber of vowels in the string: {count}")

