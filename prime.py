# PRIME Number
# 2  - Prime
# 3  - Prime
# 4  - Non Prime
# 5  - Prime
# 6  - Non Prime
# 7  - Prime
# 8  - Non Prime
# 9  - Non Prime
# 10 - Non Prime
# 11 - Prime

# Find whether a given number is prime or Not
# A number that is not fully divisible by any other number less than it.
# fully divisible means the remainder should be zero
# Given number is 7
# 7 % 2 == 0  false
# 7 % 3 == 0  false
# 7 % 4 == 0  false
# 7 % 5 == 0  false
# 7 % 6 ==0  false 
# I could not divde 7 by anything less than 7 . So 7 is prime


# Given number is 9
# 9 % 2 == 0 false
# 9 % 3 == 0 true. NOT A PRIME


number = int(input('Enter a number: '))
counter =2 
isprime = True  

while counter < number:
    if( number%counter==0):
        isprime = False 
        break
    counter +=1

if isprime:
    print('PRIME')
else:
    print('NOT PRIME')


    # isprime (number)



    