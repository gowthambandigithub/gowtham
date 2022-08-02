''' A company gives a bonus to employee
    time period service     bonus
    -------------------    -------\
    more then 10 years     10%
    >=and <=10years        8%
    less then 6 years      5%


   Calculate net bonus amount '''
salary=float(input("enter your salary amount: "))
exp=float(input("enter your experince: "))

if (exp>10):
    bonus = salary*0.1
    print ("the net bonus amount is: ",bonus)
elif(exp>=6 and exp<=10):
    bonus = salary*0.08
    print("the net bonus amount is: ",bonus)
else:
    bonus = salary*0.05
    print("the net bonus amount is: ",bonus)

