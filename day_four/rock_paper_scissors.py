"""This file contains the rock, paper and scissors challenge"""
# Game_rules:
# Rock wins against paper
# Scissor wins against paper
# Paper wins against rock
import random
print("Welcome to the rock, paper and scissor game")

rock = ''' 
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''

---'   ____)____
          ______)
          _______)
         _______)
---.__________'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''
choice_list = [rock, paper, scissors]
user_input = int(input("What do you choose? Type 0 for rock, 1 paper or 2 Scissors:"))
print(choice_list[user_input])
computer_choice = random.randint(0, 2)
print(f"Computer chose: \n {choice_list[computer_choice]}")
# user_input_check
if user_input >= 3 or user_input < 0:
    print("You've entered a wrong input, you loose")
elif user_input == 0 and computer_choice == 2:
    print("Yo!, You win")
elif computer_choice == 2 and user_input == 0:
    print("OOps,You loose!")
elif computer_choice > user_input:
    print("OOps,You loose!")
elif user_input > computer_choice:
    print("Yo!, You win")
elif computer_choice == user_input:
    print("It's a draw")


