from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, l_color='white', r_color='white'):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.l_score_color = l_color
        self.r_score_color = r_color
        self.r_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.color(self.l_score_color)
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.color(self.r_score_color)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    def l_point(self):
        self.l_score += 1
        self.refresh()

    def r_point(self):
        self.r_score += 1
        self.refresh()
