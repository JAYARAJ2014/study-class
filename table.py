number = int(input ('Which number do you want the table for?'))
limit = int(input('Limit?'))
counter=1
print ('Printing multiplication table of ' + str(number) + ' up to ' +str(limit) )
maxlength = len(str(number*limit))
while counter<=limit: 
    print (str(number).rjust(maxlength,' ')+' x ' + str(counter).rjust(maxlength,' ') + ' = ' + str(number*counter).rjust(maxlength,' '))
    counter+=1   # counter= counter +1 


   
    ### Validate input and handle gracefully