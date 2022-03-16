#day 24 of 100 days of python
# reading to and from files

PLACEHOLDER = "[name]"

#opening the file as read only using relative path
with open("input/names/invited_names.txt") as file:
    name_list = file.readlines()

#open the file starting_letter and store it's content on the letters variable
with open("input/letters/starting_letter.txt") as letter:
    letters = letter.read()
    for name in name_list:
        stripped_name = name.strip() # removing the new lines at the end of each word
        new_letter = letters.replace(PLACEHOLDER, stripped_name)

        #write each letter on a new text file and save it on the output folder
        with open(f"output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as final_letter:
            final_letter.write(new_letter)
