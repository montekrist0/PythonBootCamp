import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
screen.onkey(player.move, "Up")


game_is_on = True
counter = 0
while game_is_on:
    time.sleep(car_manager.speed)
    screen.update()
    car_manager.move_cars()
    counter += 1
    if car_manager.collapse(player):
        scoreboard.game_over()
        time.sleep(5)
        scoreboard.score = 0
        scoreboard.update_score()
        player.go_to_start()

    if counter == 6:
        car_manager.add_car()
        counter = 0

    if player.ycor() > 280:
        scoreboard.score += 1
        car_manager.speed *= 0.9
        scoreboard.update_score()
        player.go_to_start()
        screen.update()
        time.sleep(1)

