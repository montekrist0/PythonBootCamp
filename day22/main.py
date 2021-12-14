from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.colormode(255)
screen.title("PONG")
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0)
screen.listen()
_ball = Ball()
l_paddle = Paddle((-350, 0), 'red')
r_paddle = Paddle((350, 0), 'green')
scoreboard = Scoreboard(l_paddle.paddle_color, r_paddle.paddle_color)
print(r_paddle.paddle_color)


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    screen.update()
    _ball.move()
    if (_ball.xcor() > 320 and _ball.distance(r_paddle) < 50) or (_ball.xcor() < -320 and _ball.distance(l_paddle) < 50):
        _ball.bounce_x()
    if _ball.xcor() > 380:
        _ball.restart()
        scoreboard.l_point()

    if _ball.xcor() < -380:
        _ball.restart()
        scoreboard.r_point()




screen.exitonclick()
