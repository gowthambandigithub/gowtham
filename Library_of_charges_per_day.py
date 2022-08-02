'''The numbers of days from user and calculate the charges for library


         numbers of days            charges
                                     
         till 5 days                 Rs 2/day
         6 to 10 days                Rs 3/day
         11 to 15 days               Rs 4/day
         after 15 days               Rs 5/day'''


days=int(input("enter days"))
if (days<5):
    bill =days*2
    print("the charges for library is: ",bill)
elif(days>=6 and days<=10):
    bill=days*3
    print("the charges for library is: ",bill)
elif(days>=11 and days<=15):
    bill=days*3
    print("the charges for library is: ", bill)
else:
    bill=days*3
    print("the charges for library is: ", bill)
