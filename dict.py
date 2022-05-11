birthdays = {'Priya':'Aug 19', 'Saithya': 'Nov 1', 'Jay':'Nov 18'}

print(birthdays['Priya'])

# adding two single quote in the string when a single quote is required.
if('Mithun'not in birthdays.keys()):
    print ('Mithun''s brithday not recorded')

# add an item to teh dictionary
birthdays['Mithun']='Nov 22'

if('Mithun'not in birthdays.keys()):
    print ('Mithun''s brithday not recorded')
else:
    print('Now you have Mithus birthday')