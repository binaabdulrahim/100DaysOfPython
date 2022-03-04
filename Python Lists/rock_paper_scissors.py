# type 0 for rock, 1 for paper, and 2 for scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


game = [rock, paper, scissors]
user = int(input ("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors  " ))
print(game[user])
computer = random.randint(0,2)
print("Computer choose:")
print(game[computer])


if user == 0 and computer == 2:
    print("You win")
elif user >= 3 or user < 0:
    print("You typed invalid number")
elif computer == 0 and user == 2:
    print ("You lost")
elif user == 2 and computer == 1:
    print("You win")
elif computer == 2 and user == 1:
    print("You lost")
elif user == 0 and computer == 1:
    print("You lost")
elif computer == 0 and user == 2:
    print("You win")
else:
    print("It's a draw")
