import time
import turtle
from turtle import Turtle, Screen
from Snake import Snake
from food import Food
from score_board import ScoreBoard

# Initial the screen and animation
screen = Screen()
screen.setup(600, 600)
turtle.tracer(0)
screen.title("Snack Game")

# Initial object
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Initial event
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game condition
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Interaction with food
    if (snake.head.distance(food) < 15):
        print("Mon Mon Mon")
        scoreboard.score_increase()
        snake.length_increase()
        food.refresh()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        game_is_on = False

    #Detect collision with tail
    for accident in snake.snake_part[1:]:
        if snake.head.distance(accident) < 10:
            scoreboard.game_over()
            game_is_on = False

# Screen exit
screen.exitonclick()
