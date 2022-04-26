country_list = ['USA','CA','PORTUGAL', 'INDIA','MEXICO','DUBAI']

# method 1:
# for index in range(0 , len(country_list)):
#     print(country_list[index])
    
# method 2:
index = 0
while index< len(country_list):
    print(country_list[index])
    index+=1


# try:
#     index = int(input('Please enter the index of a country '))
#     print(country_list[index])
# except IndexError:
#     print ('You have entered a wrong index')
# except:
#     print('Something terrible happened')
