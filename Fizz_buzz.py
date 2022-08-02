'''Fizz buzz is a game that is some time played by a children to help them learn about division
      if the players numbers is divisible by 3 then the player say fizz instead of there number
    if the players number is divisible by 3 then the player says fizz instead of there number
    A player must say both fizz and buzz for number that are divisible by both3 and 5
    to display the ans for the first 100 numbers in the fizz buzz game'''


for i in range (1,16):
    if(i%3 ==0 and i%5==0):
        print("fizzbuzz")
    elif(i%3 ==0):
        print("fizz")
    elif(i%5 ==0):
        print("buzz")
    else:
        print(i)
            
