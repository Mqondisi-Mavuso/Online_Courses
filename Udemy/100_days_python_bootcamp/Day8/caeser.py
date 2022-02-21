#day 8 (100 days of python bootcamp)
# the Caesar cipher project


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#prompt the user for the relevant arguments
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# encrypt function that will encrypt the given letter using our algorithm
def encrypt(text, shift):
  cipher_text = ''
  new_position = -1
  for letter in text:
    i = alphabet.index(letter)
    #add the shift to the current position and assign it to the new position
    new_position = i + shift
    if new_position >= len(alphabet):  # to avoid out of range bug
      new_position -= len(alphabet)
    cipher_text += alphabet[new_position]
  print(f"The encoded text is {cipher_text}")

# decrypt function that will decrypt the text back to it's original meaning
def decrypt(encoded_text, key):
  decoded_text = ""
  key_position = -1
  for letter in encoded_text:
    key_position = alphabet.index(letter) - key      #subtract the key from the current position to get n_position
    if key_position >= len(alphabet):
      key_position -= len(alphabet)
    decoded_text += alphabet[key_position]
  print(f"The decoded text is {decoded_text}")

# depending on what the user wants, call the relevant function
if direction == 'encode':
  encrypt(text, shift)
elif direction =="decode":
  decrypt(encoded_text = text, key = shift)
