import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.penup()
        self.goto(cor_x, cor_y)

    def refresh(self):
        self.penup()
        cor_x = random.randint(-280, 280)
        cor_y = random.randint(-280, 280)
        self.goto(cor_x, cor_y)

