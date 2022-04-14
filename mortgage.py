
# accept loan amount , interest rate, duration of the loan
# print amortization schedule

loanamount = float(input('Please enter your loan amount: '))
rateofinterest = float(input('Please enter interest rate: '))
duration = int(input('Please enter duration in years: '))

totalinterest = loanamount * rateofinterest * duration /100
print (totalinterest)