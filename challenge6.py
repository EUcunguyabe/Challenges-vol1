#!/usr/bin/python3
#multiplication table for a given number
number = int(input("enter number:"))
for i in range (1,13):
    multiplication = number * i
    print (number, "x", i, "=" ,multiplication)