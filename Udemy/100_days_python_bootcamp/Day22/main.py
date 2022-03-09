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

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(0.00001)
    screen.update()
    ball.move()

    # for bouncing off the top wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # for bouncing off the paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    #for detecting if the ball passed the right paddle
    if ball.xcor() > 380:
        ball.reset_position()

    # detecting when the ball has passed the left paddle
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
