#day 8 (100 days of python bootcamp)
# the Caesar cipher project

#logo
from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# this will decode or encode depending on the user's input
def caeser(plain_text, key, direction):
  decoded_text = ""
  key_position = -1
  if direction == "decode":     # make the key negative use in addition later
      key *= -1
  for letter in plain_text:
    #keep the spaces and digits, continue will force the loop to start over
    if letter == " " or letter.isdigit():
      decoded_text += letter
      continue
    key_position = alphabet.index(letter) + key      #shifting to the correct position
    if key_position >= len(alphabet):
      key_position -= len(alphabet)
    decoded_text += alphabet[key_position]       #assign the correct letter to new word
  print(f"The decoded text is {decoded_text}")


#prompt the user for the relevant arguments
restart = True
while restart:
  restart_program = input("Type 'yes' to restart the program and 'no' to quit:\n")
  if restart_program == "no":
    break
  else:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    #this modifies the shift to accomodate the total number of letters in the list
    if shift > 26:
      shift %= 26
    #calling the function that will produce the reqired output
    caeser(plain_text = text, key = shift, direction = direction)
