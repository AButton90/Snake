from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 14:
        food.refresh()
        snake.extend()
        score.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        game_on = False

    # Detect collision with tail
    for block in snake.block_list[1:]:
        if snake.head.distance(block) < 10:
            game_on = False

score.game_over()









screen.exitonclick()