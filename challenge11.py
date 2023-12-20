#!/usr/bin/python
string=input ("Enter the string:")
reverse=string[::-1]
if (string == reverse):
    print("this is a palindrome")
else:
    print ("this is not palindrome")
