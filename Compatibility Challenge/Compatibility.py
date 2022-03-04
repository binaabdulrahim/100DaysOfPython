print("Welcome to Love Calulator! ")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#use lower function which changes all the letters in a string to lower case
#use count function which gives the name of times a letter occurs in a string

combined_names = name1 + name2
lower_case = combined_names.lower()

t = lower_case.count("t")
r = lower_case.count("r")
u = lower_case.count("u")
e = lower_case.count("e")
true = t + r + u + e 
l = lower_case.count("l")
o = lower_case.count("o")
v = lower_case.count("v")
e = lower_case.count("e")
love = l + o + v + e

add_true_love = str(true) + str(love)