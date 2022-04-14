 
# Accept a number from the console  / terminal

# the user keys in a number. We are converting it to integer and
# storing it in a variable named number 
number = int(input ('Please enter a number '))
# initialize a counter to 1 
counter = 1
# Initialized as one because, factorial of zero and one is equal to 1
factorial = 1; ## accumulator variable

while counter<=number: 
    # factorial = factorial * counter
    factorial *=  counter
    counter+=1   # counter= counter +1 


print (number,'!=',factorial)
