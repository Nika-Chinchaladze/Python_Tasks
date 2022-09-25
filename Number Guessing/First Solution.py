import random as rd
from art import logo

numbers = [i for i in range(1,101)]
computer_number = rd.choice(numbers)
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  life = 10
elif difficulty == "hard":
  life = 5

while life > 0:
  print(f"You have {life} remaining to guess the number!")
  answer = int(input("Make a guess: "))
  if answer > computer_number:
    life -= 1
    if life == 0:
      print("You Lose Game, You don't have attemps!")
    else:
      print("Too high.")
      print("Guess again.")
  elif answer < computer_number:
    life -= 1
    if life == 0:
      print("You Lose Game, You don't have attemps!")
    else:
      print("Too low.")
      print("Guess again.")
  else:
    print("Right Answer, You Won!")
    print(f"computer's number {computer_number}")
    break