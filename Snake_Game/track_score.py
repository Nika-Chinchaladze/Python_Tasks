from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.color("dark green")
        self.penup()
        self.goto(0, 270)
        self.watch_score()

    def watch_score(self):
        self.write(f"Score: {self.current_score}", align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.current_score += 1
        self.clear()
        self.watch_score()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over, Your Final Score: {self.current_score}", align=ALIGNMENT, font=FONT)
