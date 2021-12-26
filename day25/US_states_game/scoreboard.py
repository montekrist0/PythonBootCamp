from turtle import Turtle

START_POSITION = (0, 250)


class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.speed('fastest')
        self.score = 0
        self.goto(START_POSITION)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Your Score is: {self.score}/50", font=("Verdana", 25, "normal"), align='center')

    def congrats(self):
        self.clear()
        self.goto(0, 0)
        if 0 <= self.score < 5:
            self.write("Too bad. Try again 😊", font=("Verdana", 25, "normal"), align='center')
        elif 5 <= self.score < 10:
            self.write("Could be better!", font=("Verdana", 25, "normal"), align='center')
        elif 10 <= self.score < 20:
            self.write("Not bad!", font=("Verdana", 25, "normal"), align='center')
        elif 20 <= self.score < 30:
            self.write("Awesome!", font=("Verdana", 25, "normal"), align='center')
        else:
            self.write("UNBELIEVABLE! YOU ARE AMAZING", font=("Verdana", 25, "normal"), align='center')

