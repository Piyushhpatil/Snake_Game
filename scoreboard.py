from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score = {self.scores}", move=False, align="center", font=("Arial", 15, "normal"))

    def update(self):
        self.clear()
        self.scores += 1
        self.write(f"score = {self.scores}", move=False, align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", move=False, align="center", font=("Arial", 15, "normal"))
