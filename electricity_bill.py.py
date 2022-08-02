"""write a program to calculate the electricity bill (accept number of unit from user)according to the following criteria:
   unit                 price

   first 100 units      0
   next 100 units     rs 5 per unit
   after200 unitds    rs 10 per unit

(for example if input unit is 350 then total bill amount is rs 2000)"""


units=int(input("enter the number of units: "))

if (units<100):
    print("the bill is zero: ")
elif (units>=100 and units<=200):
    bill=5*(units-100)
    print(" total bill is payable is: ",bill)
else:
    bill=10*(units-200)+5*100
    print("the total bill is payable is:",  bill)
    
