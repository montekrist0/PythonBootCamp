from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, init_coords, paddle_color='white'):
        super().__init__()
        self.paddle_color = paddle_color
        self.color(paddle_color)
        self.shape('square')
        self.shapesize(5, 1)
        self.penup()
        self.speed('fastest')
        self.goto(init_coords)
        # self.color('white')

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)


