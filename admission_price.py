age =int(input("enter a number"))
cost=1

while(age!=0):
 if(age<=2):
     cost=cost+0
 elif(age>=3 and age<=12):
     cost=cost+14
 elif(age>=65):
     cost=cost+18
 else:
     cost=cost+23
     age=int(input("enter the another person"))
 print("the total cost for the group is: ",cost)
             
