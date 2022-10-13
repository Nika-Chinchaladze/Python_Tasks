from turtle import Turtle, Screen, colormode
from random import choice

messi = Turtle()
messi.hideturtle()
messi.speed("fastest")
colormode(255)

my_colors = [(40, 7, 178), (87, 248, 180), (219, 156, 111), (146, 6, 81), (239, 45, 119), (11, 211, 85), (12, 139, 60),
             (215, 115, 177), (111, 104, 234), (249, 249, 60), (55, 232, 70), (184, 179, 246), (210, 103, 11),
             (40, 35, 246), (159, 124, 235), (241, 45, 37)]

messi.penup()
messi.goto(-300, -230)


def move_forward():
    for j in range(10):
        messi.forward(30)
        messi.dot(20, choice(my_colors))
        messi.forward(30)


def start_again():
    messi.left(90)
    messi.forward(50)
    messi.left(90)
    messi.forward(600)
    messi.setheading(0)


for i in range(10):
    move_forward()
    start_again()


screen = Screen()
screen.exitonclick()
