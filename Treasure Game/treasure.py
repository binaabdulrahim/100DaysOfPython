print('''
      ___________
     /=//==//=/  \
    |=||==||=|    |
    |=||==||=|~-, |
    |=||==||=|^.`;|
jgs  \=\\==\\=\`=.:
      `"""""""`^-,`.
               `.~,'
              ',~^:,
              `.^;`.
               ^-.~=;.
                  `.^.:`.

------------------------------------------------


''')
print("Welcome to Treasure Hunt Games")
print("You're mission is to find the gold")

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right".\n ').lower()


if choice1 == "left":
        choice2 = input('You\'ve reached an ocean. What do you want to do? Type "swim" or "wait".\n ').lower()
        if choice2 == "wait":
            choice3 = input('You\'ve reached 3 different color doors: red, blue, and yellow. What do you pick? Type "red", "blue" or "yellow".\n ').lower()
            if choice3 == "yellow":
                print("You win!")
            elif choice3 == "red":
                print("You are burning in fire")
            else:
                print("Game over!")
        else: 
        	print("Game over!")   
else:
    print("Game over!")
    