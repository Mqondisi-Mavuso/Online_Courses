from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong game")
screen.tracer(0)            # This is for stopping any animation until further notice

r_paddle = Paddle((290, 0))
l_paddle = Paddle((-300, 0))

ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "W")
screen.onkey(l_paddle.go_down, "S")

game_is_on = True
while game_is_on:
    time.sleep(0.0001)
    screen.update()
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce()

screen.exitonclick()
