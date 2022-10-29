#Write a program that automatically prints the solution to this game
#Write a program that prints each number from 1 to 100 in turn.
#Number divisible by 3 print "Fizz"
#Number divisible by 5 print "Buzz"
#Number divisible by 3 & 5 print "FizzBuzz"

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0: 
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else: 
        print(number)


