from turtle import Turtle
from TxtManager import WorkTxt
reading = WorkTxt()
ALIGNMENT = "center"
FONT = ("Arial", 16, "bold")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.highest_score = int(reading.read_txt())
        self.hideturtle()
        self.color("dark green")
        self.penup()
        self.watch_score()

    def watch_score(self):
        self.clear()
        self.setposition(0, 270)
        self.reset_highest_score()
        self.write(f"Score: {self.current_score} | Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)

    def write_score(self):
        self.current_score += 1
        self.clear()
        self.watch_score()

    def reset_highest_score(self):
        if self.current_score > self.highest_score:
            self.highest_score = self.current_score
            reading.write_txt(self.highest_score)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"Game Over, Your Final Score is: {self.current_score}", align=ALIGNMENT, font=FONT)
