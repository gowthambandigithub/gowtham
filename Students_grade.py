'''write a program to print the grade of a student based on the marks obtained
        s.no     marks     grade
         1     90above     excellent
         2     70above     very good
         3     60above     good 
         4     40above     average 
         5     40below     fail
    the above program can be written using elif '''


marks=int(input("enter your marks"))
if marks>90:
     print("excellent")
elif marks>70:
    print("very good")
elif marks>60:
    print("good")
elif marks>40:
    print("average")
else:
    print("fail")
