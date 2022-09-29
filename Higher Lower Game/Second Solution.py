from art import logo, vs
from get_data import data
import random as rd
from replit import clear

def define_data(celebrity):
  name = celebrity['name']
  desc = celebrity['description']
  country = celebrity['country']
  return f"{name}, {desc}, from {country}"

def check_answer(first_one, second_one, chosen):
  if chosen == 'a':
    return first_one > second_one
  else:
    return second_one > first_one


print(logo)
player_score = 0
second = rd.choice(data)

end_game = False
while end_game != True:
  first = second
  second = rd.choice(data)
  while first == second:
    second = rd.choice(data)
  
  print(f"Compare A: {define_data(first)}")
  print(vs)
  print(f"Against B: {define_data(second)}")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  first_quantity = first['follower_count']
  second_quantity = second['follower_count']
  correct = check_answer(first_quantity, second_quantity, answer)
  
  if correct:
    player_score += 1
    clear()
    print(logo)
    print(f"You're right! Current score: {player_score}")
  else:
    print(f"Sorry, that's wrong! Final score: {player_score}")
    end_game = True