# This program prints HELLO 100 times

number = int(input ('Please enter a number '))
counter = 1
fact = 1;

while counter<=number: 
    fact *= counter
    counter+=1   # counter= counter +1 


print (number,'!=',fact)
