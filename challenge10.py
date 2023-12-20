#!/usr/bin/python3
#prime numbers 
Start = int(input("Enter the starting range:"))
End = int(input("Enter the ending range:"))
if Start > 1:
    count = 0
for i in range (Start, End+1):
    if i>1:
        for j in range (2, i):
            if i % j == 0:
                break
        else :
           print (i, end =" ")
else:
    print("this is prime number")
