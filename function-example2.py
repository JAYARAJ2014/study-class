# Define the function
a = 120 # global 
def add(n1, n2):
    # a = 90 local variable 
    return n1+n2+a 

#call the function
x = add(3,4)
print ( x)

