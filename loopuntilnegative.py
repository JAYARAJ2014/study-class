
# keeep asking for an input until the user enters -ve number
# if the number is negative then stop 
# print the sum of numbers all the positive numbers entered so far.


sum = 0
number=0
while (number >= 0):
     number= int(input ('Please enter a number '))
     if(number>0):
        sum += number 


print (sum)
