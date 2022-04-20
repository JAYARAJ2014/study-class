# function defintion 
# in paranthesis we provide the parmeter definition
def evenorodd(n):
    if(n%2==0):
        return 'EVEN' #return value 
    return 'ODD' # function return value 

def isevennumber(n):
    return (n%2==0)
        
def isoddnumber(n):
    return (n%2!=0)


result =  isoddnumber(90)
 # function call OR function invocation
                        # inside parntheis we supply teh value for the parameters called "Arguments"
print(result)