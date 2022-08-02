'''newtons method to computer display the square of a number.
the algorithm of newtons method following
1 Read x from the user
2 initialize guess to x/2
3 while guess to not good enough do
4 update to be the average of guess and x/guess
  guess contain an apporxiation of the square root of x
  the absolute value of the difference b/w gess*guess and x was less then or equal to10e-12'''


x=int(input("enter the number"))
guess=x/2
while((guess**2)-(x))>=10e-12:
     guess=(guess+x/guess)/2
     print("the square of" ,x,"is" ,guess)
