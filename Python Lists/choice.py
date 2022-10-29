# using random.choice function 

import random

print("Hello!")
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal for today. ")
