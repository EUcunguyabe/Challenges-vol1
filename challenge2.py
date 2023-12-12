#!/usr/bin/python3
#python numbers in a list to separate out even and odd numbers
#sum of all numbers i a list 
number_list = (1, 2, 3, 4, 5, 6, 7 ,8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
sum = 0
for i in number_list:
    sum = sum + i
    if (i%2==0):
        print (i, "is even number")
    else :
        print (i, "is odd number")
        
#the sum of all numbers in a list 
#sum = 0
#sum = sum + i
print ("sum of the numbers in list is:", sum)
