from turtle import Turtle


class WordWriter(Turtle):
    """Writes State's Name On The Screen On Specific Location"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("navy")

    def go_and_write(self, word, x_coordinate, y_coordinate):
        x_location = int(x_coordinate)
        y_location = int(y_coordinate)
        self.goto(x_location, y_location)
        self.write(f"{word.capitalize()}", align="center", font=("Arial", 12, "bold"))
