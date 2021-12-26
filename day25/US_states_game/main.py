import turtle
import pandas as pd
from scoreboard import scoreboard

states = pd.read_csv("50_states.csv")
score_board = scoreboard()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
user_answers = []
all_states = states.state.to_list()
text = turtle.Turtle()
text.hideturtle()
text.penup()
text.speed('fastest')
total_answered = 0
while total_answered < 50:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()
    if (answer_state in states["state"].values) and (answer_state not in user_answers):
        score_board.score += 1
        score_board.update_score()
        user_answers.append(answer_state)
        x = int(states[states.state == answer_state].x)
        y = int(states[states.state == answer_state].y)
        text.goto(x, y)
        text.write(answer_state, font=("Verdana", 10, "normal"), align='center')
        total_answered += 1
        all_states.remove(answer_state)
    if answer_state == 'Q':
        score_board.congrats()
        break

states_to_learn = pd.DataFrame({"state": all_states})
states_to_learn.to_csv('states_to_learn.csv')