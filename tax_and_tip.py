'''The cost of meals ordered a restaurent from the user
   computing 18% of tax and tip
   the grand total for meal including both tax and the tip.'''

price = int(input("enter a amount: "))

tax1 = float(input("enter the tax percentage: "))
tip = float(input("enter the tip percentage: "))
tax= price*0.18
tip=price*0.18

total=price+tax+tip

print("total amount is:", total)
