from turtle import Turtle
from random import random, choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars_list = []
        self.init_cars()
        self.speed = 0.1

    def init_cars(self):
        for i in range(10):
            self.add_car()

    def move_cars(self):
        for car in self.cars_list:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -320:
                car.hideturtle()
                self.cars_list.remove(car)

    def add_car(self):
        t = Turtle('square')
        t.penup()
        t.shapesize(1, 2)
        t.setheading(180)
        t.color(choice(COLORS))
        t.goto(300, randint(-25, 25) * 10)
        self.cars_list.append(t)

    def collapse(self, player):
        for car in self.cars_list:
            if car.distance(player) <= 20 and car.ycor() >= player.ycor():
                return True
        return False
