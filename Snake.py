import time
import turtle
from turtle import Turtle

STARTING_POSITIONS = [(0,0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

# Angle for the direction
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_part = []
        self.create_snake()
        self.head = self.snake_part[0]

    def create_snake(self):
        for _ in STARTING_POSITIONS:
            self.add_body_part(_)

    def add_body_part(self, position):
        tim = Turtle()
        tim.shape("square")
        tim.penup()
        tim.goto(position)
        self.snake_part.append(tim)

    def length_increase(self):
        self.add_body_part(self.snake_part[-1].position())

    def move(self):
            for sp in range(len(self.snake_part) -1, 0, -1):
                new_x = self.snake_part[sp - 1].xcor()
                new_y = self.snake_part[sp - 1].ycor()
                self.snake_part[sp].goto(new_x, new_y)
            self.snake_part[0].forward(20)
    #Direction move
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)







