#Write a program that selects random name from a list of name and person selected will have to pay for everybody's food bill
import random 

names_string = input("Give me everybody's name, separated by a commma. ")

# splits a string into a separate components bases on comma
names = names_string.split(",")

# use the len function to get the number of element in a list or the number of characters in a string
number_items = (len(names))
choices = random.randint(0, number_items - 1)
person_buys_meal = names[choices]
print(person_buys_meal + " will pay for the meal")