# Day 26 of 100
# Nato phonetic code project
import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {word.letter: word.code for(index, word) in nato_data_frame.iterrows()}    # using dictionary comprehension

user_name = input("Please input your name here: ").upper()                              # get username from keyboard
phonetic_code = [nato_dict[letter] for letter in user_name]                             # using list comprehension

print(phonetic_code)
