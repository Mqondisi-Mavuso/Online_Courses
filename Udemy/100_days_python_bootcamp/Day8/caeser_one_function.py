#day 8 (100 days of python bootcamp)
# the Caesar cipher project

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#prompt the user for the relevant arguments
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# this will decode or encode depending on the user's input
def caeser(plain_text, key, direction):
  decoded_text = ""
  key_position = -1
  if direction == "decode":     # make the key negative use in addition later
      key *= -1
  for letter in plain_text:
    key_position = alphabet.index(letter) + key      #shifting to the correct position
    if key_position >= len(alphabet):
      key_position -= len(alphabet)
    decoded_text += alphabet[key_position]       #assign the correct letter to new word
  print(f"The decoded text is {decoded_text}")

#calling the function that will produce the reqired output
caeser(plain_text = text, key = shift, direction = direction)
