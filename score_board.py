from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.scoreUpdate()

    def scoreUpdate(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}", True, align="center", font=("Arial", 20, "normal"))

    def score_increase(self):
        self.score += 1
        self.scoreUpdate()

    def game_over(self):
        self.goto(0,0)
        self.write("Game over", True, align="center", font=("Arial", 20, "normal"))



