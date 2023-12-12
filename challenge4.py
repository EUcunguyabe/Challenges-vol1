#!/usr/bin/python3
#print even numbers from 1 to 50
i = 1
sum = 0
while i <= 50:
    i+= 1
    if (i%2==0):
       # sum = sum + i
        print (i, "is even number")
#sum of all even numbers
        sum = sum + i
print (sum, "is the sum of all even numbers")
