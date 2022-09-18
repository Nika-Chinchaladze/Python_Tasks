from replit import clear
import random as rd
import pictures as pc
import words as wd

print(pc.logo)
chosen_word = rd.choice(wd.word_list)
length = len(chosen_word)
print(chosen_word)

display = []
for i in chosen_word:
    display.append("_")

entered = []
ending = False
lives = 7
place = 6
while not ending:
    guess = input("Please guess a letter! \n").lower()
    clear()
    for position in range(length):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess in entered:
        print(f"You have already entered this letter - {guess}!")
    elif guess not in chosen_word:
        lives -= 1
        print(f"{guess} is wrong letter! Left {lives} lives!")
        print(pc.stages[place])
        place = place - 1
        if lives == 0:
            print("You Lose the Game!")
            break

    entered.append(guess)
    print(display)

    if "_" not in display:
        ending = True
        print("You won the game!")
