from replit import clear
import random as rd
from logo import logo

# 1 ------------------------
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = rd.choice(cards)
    return card
  
# 2 ------------------------
def calculate(cards):
  if len(cards) == 2 and sum(cards) == 21:
    return 0
  if 11 in cards and sum(cards) >= 11:
    cards.remove(11)
    cards.append(1) 
  return sum(cards)

def compare(user, computer):
  if user == computer:
    return "it's draw!"
  elif computer == 0:
    return "computer won, with blackjack!"
  elif user == 0:
    return "player won, with blackjack!"
  elif user > 21:
    return "computer won the game!"
  elif computer > 21:
    return "player won the game!"
  elif user > computer:
    return "player bit the computer!"
  else:
    return "computer bit the player!"
  
  
# 3 ------------------------
def BlackJack():
  print(logo)
  user_card = []
  computer_card = []
  for i in range(2):
      user_card.append(deal_card())
      computer_card.append(deal_card())
  
  # 4 ------------------------
  end_game = False
  while end_game != True:
    user_score = calculate(user_card)
    computer_score = calculate(computer_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer's first card: {computer_card[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_game = True
    else:
      user_bet = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_bet == "y":
        user_card.append(deal_card())
      else:
        end_game = True
  
  while computer_score != 0 and computer_score < 17:
    computer_card.append(deal_card())
    computer_score = calculate(computer_card)
  
  print("\n")
  print("---------------------------------------------")
  print(f"Player's cards: {user_card}, Player's score: {user_score}")
  print(f"Computer's cards: {computer_card}, Computer's score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play Game? yes / no \n") == "yes":
  clear()
  BlackJack()
