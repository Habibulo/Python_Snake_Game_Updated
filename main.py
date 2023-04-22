import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("grey")
screen.title("My Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
food.refresh()
new_scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtle_head.distance(food) < 15:
        food.refresh()
        snake.extend()
        new_scoreboard.increase_score()


    if snake.turtle_head.xcor() <= -295 \
            or snake.turtle_head.xcor() >= 295 \
            or snake.turtle_head.ycor() <= -295 \
            or snake.turtle_head.ycor() >= 295:
        new_scoreboard.reset()
        snake.reset_snake()

    for segment in snake.all_turtle[1:]:
        if snake.turtle_head.distance(segment) < 10:
            new_scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
