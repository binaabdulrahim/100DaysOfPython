''' A prime number is a number that is only divisible by one and itself. A prime number is a number that can't be broken to smaller parts other than one and itself. Write a function that checks whether if the number passed into it is a prime number or not.
'''
#Write your code below this line 👇
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
     if number % i == 0:
         is_prime = False
    if is_prime: 
        print(f"It's a prime number. ")
    else:
        print(f"It's a not a prime {number} number. ")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)