#!/usr/bin/python3
#factorial calculation
num = int(input("Enter any number:"))
factorial = 1
for i in range (1,num+1):
    factorial = factorial *i
print ("the factorial of", num, "is", factorial)