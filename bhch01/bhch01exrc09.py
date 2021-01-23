price=eval(input('Enter the price of meal: '))
percent_tip=eval(input('Enter the percentage of tip: '))
tip=percent_tip*price/100
print('The tip amount is',tip)
Total_bill=price+tip
print('The Total bill is',Total_bill)
