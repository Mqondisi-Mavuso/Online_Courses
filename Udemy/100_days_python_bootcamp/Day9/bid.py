# day 9 of 100 days python bootcamp 2022 by Angela Wu
# silent bid project

#from replit import clear
#importing the logo from the other file called art
from art import logo
print(logo)

bidders = []
# This function adds the new bidder as a dictionary to the bidders list
def add_new_bidder(bidder_name, bidder_price):
  new_bidder = {}
  new_bidder["name"] = bidder_name
  new_bidder["price"] = bidder_price
  bidders.append(new_bidder)
  
# Loops until the user types 'no' when asked
should_continue = True
while should_continue:
  name = input("What's your name? \n")
  price = int(input("How much do you want to bid? \n$"))
  other_bidders = input("Is there anyone who wants to bid? 'yes' or 'no'\n")
  # calling the function to add the new bidder to the list
  add_new_bidder(bidder_name = name, bidder_price = price)
  
  if other_bidders == 'no':    # will execute if the user type 'no'
    should_continue = False 
  #clear()                      #clear the console to hide other bidders

winner = {}
big_amount = 0
bid_winner = ""

# loops throught the whole list and keep track of the highest bidder
for person in bidders:
  amount = person["price"]
  nam = person["name"]
  if amount > big_amount:
    big_amount = amount
    winner["name"] = nam
    winner["price"] = big_amount

#prints the bidders dictionary
print(bidders)
bid_winner = winner["name"]

print(f"The bid goes to {bid_winner}, with the price of ${big_amount}, CONGRATULATIONS!!!!")