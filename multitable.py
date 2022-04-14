# I want the result int his format

# 1 x 10 = 10
# 2 x 10 = 20
# 3 x 10 = 30
# counter x number = result 


number = int(input('Enter the number for which table is needed: '))
counter = 1
limit = 10

while (counter<=limit):
    print(counter,' X ',number, ' = ' , counter*number)
    counter+=1
    


