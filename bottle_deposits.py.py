
"""write a program thats read the number of container of each size from the user your program should continue by computing and display the refund that wil be
receivedfor returning these containers format the output so that includes a doller sign and two digits to the right of the decimal point"""

bottle_above_lit=(input("enter the number of bottles (above lit): "))
bottles_below_lit=(input("enter the number 0f bottles(below lit): "))

refund=(bottle_above_lit*0.25)+(bottles_below_lit*0.1)
print("he total refund amount=", refund)
