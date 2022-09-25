from random import randint
from art import logo

# variables: --------------------------------------
easy = 10
hard = 5

# first function: ---------------------------------
def Check_guess(answer, computer_number, tries):
  if answer > computer_number:
    print("Too high!")
    return tries - 1
  elif answer < computer_number:
    print("Too low!")
    return tries - 1
  else:
    print(f"You guess number, computer's number was {computer_number}")

# second function: --------------------------------
def define_level():
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if difficulty == "easy":
    return easy
  elif difficulty == "hard":
    return hard

def Guess_number():
  computer_number = randint(1,100)
  print(logo)
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  
  tries = define_level()

  answer = 0
  while answer != computer_number:
    print(f"You have {tries} remaining to guess the number!")
    answer = int(input("Make a guess: "))
    tries = Check_guess(answer, computer_number, tries)
    if tries == 0:
      print("You Lose, You run out of attempts!")
      return
    elif answer != computer_number:
      print("Guess Again!")

Guess_number()
  