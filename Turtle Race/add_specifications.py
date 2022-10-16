def draw_line(turtle):
    turtle.turtlesize(1)
    turtle.speed("fastest")
    turtle.shape("square")
    turtle.penup()
    # first line:
    for i in range(10):
        turtle.color("brown")
        turtle.goto(340, (150-(i*40)))
        turtle.stamp()
    # second line
    for i in range(9):
        turtle.goto(360, (130-(i*40)))
        turtle.stamp()
    turtle.color("black")


def turn_around(turtle):
    turtle.setheading(180)


def draw_path(turtle, x, y):
    turtle.speed("fastest")
    turtle.pensize(2)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(x, y)
    # one circle
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(720)
    turtle.right(90)
    turtle.penup()
    turtle.forward(60)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(720)


def draw_start_line(turtle):
    turtle.hideturtle()
    turtle.turtlesize(1)
    turtle.pensize(2)
    turtle.pencolor("crimson")
    turtle.speed("fastest")
    # move:
    turtle.penup()
    turtle.goto(-390, 160)
    turtle.setheading(270)
    for i in range(5):
        turtle.pendown()
        turtle.forward(60)
        turtle.penup()
        turtle.forward(20)


def return_back(participant, y_position):
    participant.speed(5)
    participant.penup()
    participant.setheading(180)
    participant.goto(-370, y_position)
    participant.setheading(0)
