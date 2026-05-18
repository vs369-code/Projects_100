# Rock, paper and scissor game!

import random


rock = '''

___________
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''




paper = '''

    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''





scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game_image = [rock, paper, scissor] #List of game images

#User input
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

#Display user choice
if user_choice >= 0 and user_choice <= 2: 
    #compare user input is valid or not
    print(game_image[user_choice])

#Generate random choice for computer and randomly select
computer_choice = random.randint(0, 2)
#randomly select integer between o to 2 (random.randint is starting and ending value are inclusive
print("You chose:")  
#Display computer choice
print(game_image[computer_choice])  

 
#Determine the winner
computer_choice = random.randint (0, 2)
# computer_choice = random.choice([0, 1, 2]
print(f"computer choose {computer_choice}")

#condition for invalid input
if user_choice >= 3 or user_choice < 0:
    #user_choice >= 3 means user input is 3 or more than 3
    print("You typed an invalid number. You lose!")

#conditions for winning and losing
elif user_choice == 0 and computer_choice == 2:
    #== means equal to
    print("You win!")

elif computer_choice == 0 and user_choice == 2:
    print("You lose!")

elif computer_choice > user_choice:
    print("You lose!")

elif user_choice > computer_choice:
    print("You win!")

elif computer_choice == user_choice:
    print("It's a draw!")
 
