from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.speed('slow')
        self.color('white')
        self.x_move = 10
        self.y_move = 10
        self._go_up = True
        self._speed = 0.1

    def bounce_y(self):
        # self.x_move = -self.x_move
        self.y_move = -self.y_move

    def bounce_x(self):
        # self.x_move = -self.x_move
        self.x_move = -self.x_move

    def restart(self):
        # self.bounce_y()
        self.bounce_x()
        self.goto(0, 0)
        if self._speed > 0.005:
            self._speed -= 0.001

    def move(self):
        if abs(self.ycor()) >= 290:
            self.bounce_y()
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
        time.sleep(self._speed)


