from turtle import Screen
from paddle import Paddle
from ball import Ball
from score_board import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.screensize(800, 600)
screen.title("Pong game")
screen.tracer(0)            # This is for stopping any animation until further notice

r_paddle = Paddle((291, 0))
l_paddle = Paddle((-300, 0))

# constructing the ball
ball = Ball()
score_board = Scoreboard()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
move_speed = 0.1        # for increasing the speed of the ball everytime it's hits the paddles
while game_is_on:
    time.sleep(move_speed)
    screen.update()
    ball.move()

    # for bouncing off the top wall
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # for bouncing off the paddles
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 or ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        move_speed *= 0.7

    #for detecting if the ball passed the right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        move_speed = 0.1
        score_board.l_point()

    # detecting when the ball has passed the left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        move_speed = 0.1
        score_board.r_point()

screen.exitonclick()
