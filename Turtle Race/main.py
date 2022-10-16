from turtle import Turtle, Screen
from random import randint
from add_specifications import draw_line, turn_around, draw_path, draw_start_line, return_back

# define screen:
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("medium aquamarine")
screen.title("Turtle Race")

# define window title and game welcome phrase
reader = Turtle()
reader.hideturtle()
reader.penup()
writer = Turtle()
draw_start_line(writer)
draw_line(writer)
x_start = -390
y_start = 160
for i in range(5):
    draw_path(writer, x_start, y_start)
    y_start -= 80
writer.hideturtle()
writer.penup()
writer.goto(0, 260)
writer.write("Welcome To Turtle Race", move=False, align="center", font=("Arial", 14, "bold"))

# create turtles
my_colors = ["red", "indian red", "green", "blue", "purple"]
y_positions = [-190, -110, -30, 50, 130]
my_turtles = []
user_score = 0

for i in range(5):
    turtle_name = Turtle(shape="turtle")
    turtle_name.turtlesize(2)
    turtle_name.color(my_colors[i])
    turtle_name.penup()
    turtle_name.goto(-370, y_positions[i])
    my_turtles.append(turtle_name)

# small questionare window popup
want_continue = True
while want_continue:
    user_guess = screen.textinput(title="Make your bet:", prompt="Participants: Red, Green, Indian red, Blue, Purple."
                                                                 " \nWhat Do you think, Which Racer will win? ").upper()
    reader.goto(-390, 200)
    reader.pendown()
    reader.pencolor("midnight blue")
    reader.write(f"Your Favourite turtle is: {user_guess}", align="left", font=("Arial", 11, "bold"))
    reader.pencolor("black")
    reader.penup()
    # define important variables
    race = False
    winner = ""

    if user_guess:
        race = True

    while race:
        for turtle in my_turtles:
            if turtle.xcor() >= 315:
                turn_around(turtle)
                winner = turtle.pencolor()
                winner_name = turtle
                race = False
            else:
                step = randint(0, 15)
                turtle.forward(step)

    reader.goto(0, -260)
    reader.pendown()
    if user_guess == winner.upper():
        reader.pencolor("dark green")
        reader.write(f"Congratulations, You've won the game! {winner.upper()} turtle is the Winner!",
                     align="center", font=("Arial", 12, "bold"))
        user_score += 1
    else:
        reader.pencolor("crimson")
        reader.write(f"Unfortunately, You've Lost the game! {winner.upper()} turtle is the Winner", align="center",
                     font=("Arial", 12, "bold"))
    reader.penup()

    reader.goto(285, 200)
    reader.pendown()
    reader.pencolor("dark slate gray")
    reader.write(f"My Score: {user_score}", align="left", font=("Arial", 11, "bold"))
    reader.pencolor("black")
    reader.penup()

    will = screen.textinput(title="Continue | End Game:", prompt="Do You want to Continue? Yes/No ").lower()
    if will == "no":
        want_continue = False
    else:
        reader.clear()
        i = 0
        for racer in my_turtles:
            return_back(racer, y_positions[i])
            i += 1

screen.exitonclick()
