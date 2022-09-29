from replit import clear
import random as rd
from get_data import data
from art import vs, logo

basic = [item for item in data]
first = rd.randint(0, len(basic) - 1)

print(logo)
player_score = 0
correct = True
while correct:
  print(
    f"Compare A: {basic[first]['name']} - {basic[first]['description']}, from {basic[first]['country']}"
  )
  f_quantity = basic[first]['follower_count']
  #-------------------- logo -----------------------#
  print(vs)
  #---------- different  second index --------------#
  second = rd.randint(0, len(basic) - 1)
  while second == first:
    second = rd.randint(0, len(basic) - 1)
  print(
    f"Against B: {basic[second]['name']} - {basic[second]['description']}, from {basic[second]['country']}"
  )
  s_quantity = basic[second]['follower_count']
  #--------------- check answer -------------------#
  chosen = input("Who has more followers? Type 'A' or 'B'! ").upper()
  if chosen == 'A' and f_quantity > s_quantity:
    player_score += 1
    first = second
    clear()
    print(logo)
    print(f"You're right! Current Score {player_score}.")
  elif chosen == 'A' and f_quantity < s_quantity:
    print(f"Sorry, that wrong! Final Score {player_score}.")
    correct = False
  elif chosen == 'B' and f_quantity > s_quantity:
    print(f"Sorry, that wrong! Final Score {player_score}.")
    correct = False
  elif chosen == 'B' and f_quantity < s_quantity:
    player_score += 1
    first = second
    clear()
    print(logo)
    print(f"You're right! Current Score {player_score}.")
