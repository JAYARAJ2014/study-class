number = int(input ('Which number do you want the table for?'))
limit = int(input('Limit?'))
counter=1
print ('Printing multiplication table of ' + str(number) + ' up to ' +str(limit) )
while counter<=limit: 
    print (str(number)+' x ' + str(counter) + ' = ' + str(number*counter))
    counter+=1   # counter= counter +1 


    ### Future improvement opportunity: equalize the spacing
    ### Validate input and handle gracefully