userinput = input ('Enter an integer ')
value = int(userinput)
if (value % 3 == 0 ) and (value % 5 ==0) :
    print ('FizzBuzz')
elif (value % 3 == 0) :
    print ('Fizz')
elif (value % 5 == 0) :
    print ('Buzz')
else: 
    print('This number does not fall in the FizBuzz criteria')

print ('Program Completed')


# WRONG Exaple Below
# if (value % 3 == 0):
#     print('Fizz')
# elif (value % 5 == 0) :
#     print ('Buzz')
# elif (value % 3 == 0 ) and (value % 5 ==0) :
#     print ('FizzBuzz')
# else   :
#     print('This number does not fall in the FizBuzz criteria')

# print ('next line program')