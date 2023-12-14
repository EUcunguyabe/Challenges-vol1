#!/usr/bin/python3
#reverse a given string
string = str(input("Enter any string:"))
reversed_string = ""
for i in string[::-1]:
   reversed_string+= i
print ("Reversed string is", reversed_string)