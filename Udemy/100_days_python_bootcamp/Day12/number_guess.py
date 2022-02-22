#day 12 of 100 number guessing game

from random import randint
from art import logo

print(logo)
print("Welcome the Guess The Number Game! \nI am thinking of a number between 1 and 100...")
level = input("Choose the difficulty level: 'easy' or 'hard'? ").lower()
secrete_number = randint(1, 100 + 1)

def check(guessed_int, unk_number):
  """Takes two intergers returns output based on the given numbers"""
  if guessed_int < unk_number:
    print("Too Low")
  elif guessed_int > unk_number:
    print("Too High")
  else:
    print(f"Correct Guess, the secrete number was {unk_number}")

if level == 'easy':
  turns = 10
elif level == 'hard':
  turns = 5

#this will run until the user is out of turns
while turns:
  guess = int(input("Guess the number: "))
  check(guess, secrete_number)
  turns -= 1
  if turns:
    print(f"You have {turns} turn(s) left")
  else:
    print(f"You are out of turns, the secrete number was {secrete_number}")
