
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
print("Welcome to the Game!")
player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if player >=3 or player < 0:
    print("You typed an invalid number, you lose!")
else:
    comp = random.randint(0, 2)
    game_images = [rock, paper, scissors]
    print(f"You chose:{game_images[player]} ")
    print(f"Computer chose: {game_images[comp]}")

    if player == 0 and comp == 2:
        print("You win!")
    if comp == 0 and player == 2:
        print("you lose!")
    if comp > player:
        print("You lose!")
    if player > comp:
        print("You win!")
    if comp == player:
        print("it is a draw!")
