from art import logo
from random import randint

# print logo
print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []

def blackJack(player_cards):
  if (11 in player_cards and 10 in player_cards):
    return True
  else: return False

def valid_points(player_cards):
  if total_score(player_cards) <= 22:
    return True
  else:
    return False

def total_score(p_cards):
  return sum(p_cards)

def pick_card():
  card_position=randint(1, 12)
  chosen_card = cards[card_position]
  return chosen_card

def winner(player_cards, computer_cards):
  if blackJack(computer_cards):
    print(f"Your final card's: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("BlackJack! You lose")
  elif sum(player_cards) > 21:
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("You went over. You lose")
  elif sum(computer_cards) > 21:
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("Computer went over. You win")
  elif blackJack(player_cards) and not blackJack(computer_cards):
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("Blackjack!! You win")
  elif blackJack(player_cards) and blackJack(computer_cards):
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("Draw")
  elif sum(player_cards) == sum(computer_cards):
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("Draw")
  elif sum(player_cards) > sum(computer_cards):
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("You win!")
  elif sum(player_cards) < sum(computer_cards):
    print(f"Your final cards: {player_cards}, current score: {total_score(player_cards)}")
    print(f"Computer's final cards: {computer_cards}, current score: {total_score(computer_cards)}")
    print("You lose!")

def computer_play(computer_cards):
  computer_sum = sum(computer_cards)
  if len(computer_cards) == 0:    # pick two cards the first time
    computer_cards.append(pick_card())
    computer_cards.append(pick_card())
    if blackJack(computer_cards):
      return
  else:                  # pick just one card per turn
    while computer_sum < 16:
      if pick_card() == 11 and sum(computer_cards) > 21:
        computer_cards.append(1)
      else: computer_cards.append(pick_card())
      computer_sum = sum(computer_cards)

def play():
  should_continue = True
  while should_continue:
    pick = input("Type 'y' to pick a card, 'n' to stay: ")
    if pick == 'y':
      if len(player_cards) == 0:
        player_cards.append(pick_card())
        player_cards.append(pick_card())
        computer_play(computer_cards)
      else:
        if pick_card() == 11 and sum(player_cards) > 10:
          player_cards.append(1)
        else: player_cards.append(pick_card())

      total = total_score(player_cards)
      if total_score(player_cards) > 21:
        winner(player_cards, computer_cards)
        break
      print(f"Your cards: {player_cards}, current score: {total}")

    elif pick == 'n':
      should_continue = False
      computer_play(computer_cards)


    if should_continue:
      print(f"Computer's first card: {computer_cards[0]}")
    else:
      winner(player_cards, computer_cards)
play()
