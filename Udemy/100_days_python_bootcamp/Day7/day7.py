# 16 september (100 days python bootcamp)
# The hangman game
import random
import hangman_art as art
import hangman_words as words

word_list = words.word()
chosen_word = random.choice(word_list)

# Welcome art to the hangman game
art.h_logo()

# get the stages list from the other module we just imported
stages = art.h_stages()

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

# The player will get six lives each time they guess wrong the lose 1
lives = 6
# This is the list we'll use to display the letters of the mystry word as the user tries to guess the word
display = []
for i in range(len(chosen_word)):
  display += "_"

# the "selected" is for storing all the letters already guessed
selected = []
t = True
while t == True:
  guess = input("Guess a letter: ").lower()

  if guess in selected: # this will take the player back to line 28
    print(f"You have already selected '{guess}'")
    continue             #ensures that the code below is not excuted

  # this will go throght the entire word and check for the guessed letter
  for i in range(len(chosen_word)):
    if chosen_word[i] == guess:
      print(f"You have chosen the correct letter '{guess}'")
      display[i] = guess
  if guess not in chosen_word:
    print(f"You have chosen the wrong letter '{guess}'")
    lives -= 1
    print("You just lost a life")

  print(stages[lives])
  print(display)

  # this will execute if the user has ran of lives
  if not lives:
    print("Game over!! you are out of lives")
    print(f"The correct word was '{chosen_word}'")
    t = False

  # this will execute if the user has guessed all the letters and still has life
  elif "_" not in display:
    print("You won!!")
    t = False

  selected += guess        # Add the guessed letter to this list

print(display)
