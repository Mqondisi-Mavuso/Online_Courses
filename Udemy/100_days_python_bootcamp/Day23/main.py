import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Turtle race")

player = Player()
cars = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    if scoreboard.score == 0:
        cars.move_car()
    else:
        cars.increase_speed()
        cars.move_car()

    # for allowing the game to respond to the keyboard keys
    screen.listen()
    screen.onkey(player.move_player, "Up")

    # for incrementing the score board if ever the player reached the top
    if player.ycor() >= 280:
        scoreboard.increase_score()
        cars.increase_speed()
        player.reset_player()

    # for detecting collision with the cars
    for car in cars.all_cars:
        if car.distance(player) < 25:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()
