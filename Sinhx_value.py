'''evalute then the value of e**x upto 10 terms
sinhx= x+ x**3/3!+x**3/3!+.........x**(2k+1)/(2k+1)!'''
x=int(input("enter a x value: "))
n=int(input("enter a no.of.terms"))
sinh_x=0

for k in range(1,n):
    fact=1
    for j in range(1,k+1):
        fact=fact*j
        sinh_x=x+x**(2*k+1)/(2*k+1)*(fact)

        print(sinh_x)
                            
