from replit import clear
from image import logo

print(logo)
print("Welcome to the secret auction programm!")

def find_winner(records):
  person = ""
  maximum = 0
  for key, value in records.items():
    if value > maximum:
      maximum = value
      person = key
  print(f"The winner is {person} with a bid of ${maximum}")

bidder = {}
will = "yes"
while will != "no":
  first = input("What is your name? ")
  second = int(input("What's your bid? $"))
  will = input("Are there any other bidders? Type 'yes' or 'no'! \n")
  bidder[first] = second
  if will == "yes":
    clear()

find_winner(bidder)
