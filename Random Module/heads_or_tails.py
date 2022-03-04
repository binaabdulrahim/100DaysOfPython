#create a virtual coin toss program that will randomly tell the users "heads" or "tails".

import random

#randint will generate int between a starting number and ending number
random_side = random.randint(0,1)
#write an if statement to check if the random side that was generated is equal to one
if random_side == 1: 
    print("Heads")
else: 
    print("Tails")
