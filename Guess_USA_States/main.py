from turtle import Screen
from State_writer import WordWriter
from Coordinates import check_if_exists, return_location, save_into_csv


# prepare screen:
screen = Screen()
screen.title("USA Game")
screen.setup(width=725, height=491)
screen.bgpic("america.gif")

# create pencil:
pencil = WordWriter()


answered_list = []
play = True
while play:
    question = screen.textinput(title=f"{len(answered_list)}/50 States Correct", prompt="What's another State?").lower()
    if check_if_exists(question) and question not in answered_list:
        destination = return_location(question)
        pencil.go_and_write(question, destination[0], destination[-1])
        answered_list.append(question)
    elif check_if_exists(question) and question in answered_list:
        pass

    if question == "exit":
        save_into_csv(answered_list)
        play = False

screen.exitonclick()
