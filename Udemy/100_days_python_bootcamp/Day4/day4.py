# Day 4 project (100 days python bootcamp)
# rock paer scissor game with the computer
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

#Write your code below this line 👇
import random
User_choice = int(input("What do you want to choose? Type 0 for rock, 1 for paper and 2 for scissors \n"))
# generate a random integer to use for the game
computer_choice = random.randint(0, 2)

if ((computer_choice == 0) and (User_choice == 1)):
  print(paper)
  print("Computer chose: \n ")
  print(rock)
  print("Congratulations, you won!")
elif ((computer_choice == 0) and (User_choice == 2)):
  print(scissors)
  print("Computer chose: \n")
  print(rock)
  print("You lose!")
elif ((computer_choice == 1) and (User_choice == 2)):
  print(scissors)
  print("Computer chose: \n")
  print(paper)
  print("Congratulations, you won!")
elif ((computer_choice == 1) and (User_choice == 0)):
  print(rock)
  print("Computer chose: \n")
  print(paper)
  print("You lose!")
elif ((computer_choice == 2) and (User_choice == 0)):
  print(rock)
  print("Computer chose: \n")
  print(scissors)
  print("Congratulations, you won!")
elif ((computer_choice == 2) and (User_choice == 1)):
  print(paper)
  print("Computer chose: \n")
  print(scissors)
  print("You lose!")
else:
  print("Draw, you chose the same thing as the computer!")
