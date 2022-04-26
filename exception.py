try:
    num1 = int(input("Enter a number "))
    num2 = int(input("Enter another number "))
    print(num1/num2)
except ZeroDivisionError:
    print('Division by zero is not defined in math')
except:
    print('Some major problem occured')