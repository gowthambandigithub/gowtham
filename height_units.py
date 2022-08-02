'''number feet from the user followed by a number of inches display the equivalent
   of centimeter
   Hint:one feet is 12 inches
   one inch is 2.54 centimeters'''


feet=float(input("enter your feets: "))
    
inches=float(input("enter your inches: "))


feet_cen=feet*12*2.54
inches_cen=inches*2.54
height_cen=feet_cen+inches_cen

print("your height in centimeters: ",height_cen)
             
