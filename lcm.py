# 10 --> 10, 20, 30, 40, 50, 60, 70, 80, 90 , 100
# 20 --> 20, 40, 60, 80, 100
#  lcm is 20


def lcm(num1, num2):
    if num1>num2:
        greater = num1
    else: 
        greater = num2

    while(True):
        if(greater%num1==0) and (greater%num2==0):
            lcm=greater 
            break
        greater+=1

    return lcm 

print(lcm(10,20))