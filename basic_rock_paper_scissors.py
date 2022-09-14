import random as rd

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

items = [rock, paper, scissors]
indexes = [0, 1, 2]
# gamer
my_number = int(input("my choise: "))
if my_number <= 2:
    my_choice = items[my_number]
    print(my_choice)
    # computer
    comp_choice = rd.choice(indexes)
    print("Computer chose:")
    print(items[comp_choice])

    if my_number == 0:
        if comp_choice == 0:
            print("Equal Results!")
        elif comp_choice == 1:
            print("Computer Won, You Lose!")
        elif comp_choice == 2:
            print("You Won, Computer Lose!")

    elif my_number == 1:
        if comp_choice == 0:
            print("You Won, Computer Lose!")
        elif comp_choice == 1:
            print("Equal Results!")
        elif comp_choice == 2:
            print("Computer Won, You Lose!")

    elif my_number == 2:
        if comp_choice == 0:
            print("Computer Won, You Lose!")
        elif comp_choice == 1:
            print("You Won, Computer Lose!")
        elif comp_choice == 2:
            print("Equal Results!")
else:
    print("Please enter only 0, 1 or 2!")
