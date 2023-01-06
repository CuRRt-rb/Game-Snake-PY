from turtle import Screen, Turtle
from snake import Snake
from mouse import Mouse
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("grey")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
mouse = Mouse()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True #Moving
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Mouse and snake ADD
    if snake.head.distance(mouse) < 20:
        mouse.restart()
        snake.extension()
        score.scoring()

    #Wall crash
    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < - 380:
        game_on = False
        score.game_over()

    #Tail touching
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
