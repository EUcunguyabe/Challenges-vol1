#!/usr/bin/python3
#count number of vowels in a string
string=str(input("Enter any word:"))
#vowels="AaIiUuEeOo"
count=0
for i in string:
    if(i=="a" or i=="A" or i=="I" or i=="i" or i=="u" or i=="U" or i=="e" or i=="E" or i=="o" or i=="O"):
    
    #if i in vowels:
        count=count+1
        print (i, end=" ")
#print ("the vowels in a string are:",count) 
print(f"\nNumber of vowels in the string: {count}")

