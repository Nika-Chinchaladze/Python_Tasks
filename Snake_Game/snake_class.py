from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.snake_head = self.snake_list[0]

    def create_snake(self):
        for loc in START_POSITIONS:
            self.add_snake(loc)

    def add_snake(self, location):
        snake = Turtle(shape="square")
        snake.color("maroon")
        snake.penup()
        snake.goto(location)
        self.snake_list.append(snake)

    def increase_snake(self):
        self.add_snake(self.snake_list[-1].pos())

    def move(self):
        for loc in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[loc - 1].xcor()
            new_y = self.snake_list[loc - 1].ycor()
            self.snake_list[loc].goto(new_x, new_y)
        self.snake_head.forward(MOVE_DISTANCE)

    def crashed_snake(self):
        for snk in self.snake_list[1:]:
            if self.snake_head.distance(snk) < 5:
                return True

    def up(self):
        if self.snake_head.heading() != DOWN:
            self.snake_head.setheading(UP)

    def down(self):
        if self.snake_head.heading() != UP:
            self.snake_head.setheading(DOWN)

    def left(self):
        if self.snake_head.heading() != RIGHT:
            self.snake_head.setheading(LEFT)

    def right(self):
        if self.snake_head.heading() != LEFT:
            self.snake_head.setheading(RIGHT)

    def go_through(self, x, y):
        self.snake_head.goto(x, y)
