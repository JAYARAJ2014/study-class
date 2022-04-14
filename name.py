
# Write a program to ask for a name until the user enters END.
# Print the name each time.
# When you are done, print "I am done."

name = ""
while(name!="END"):
    name = input('enter a name')
    print('You entered ',name)

print ('I am done!')