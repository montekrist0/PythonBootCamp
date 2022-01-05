import tkinter.messagebox

import pandas as pd
from tkinter import *
from random import choice

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pd.read_csv("data/words_to_learn.csv").to_dict('records')
except FileNotFoundError:
    data = pd.read_csv("data/english_russian_words.csv").to_dict('records')
except pd.errors.EmptyDataError:
    data = pd.read_csv("data/english_russian_words.csv").to_dict('records')


# ser = pd.Series(data.Russian.values, index=data.English).to_dict()
# my_list = [
#     {key: value} for key, value in ser.items()
# ]
# print(my_list)

word = None


def flip():
    if len(data):
        canvas.itemconfig(canvas_image, image=card_back)
        canvas.itemconfig(card_title, text="Russian", fill='white')
        canvas.itemconfig(card_word, text=word['Russian'], fill='white')


def update_word():
    global word, flip_timer, data
    if len(data) == 0:
        play_again = tkinter.messagebox.askokcancel(title="There is no words in your dictionary!",
                                                    message="Do you want to repeat words again?")
        if play_again:
            data = pd.read_csv("data/english_russian_words.csv").to_dict('records')
            update_word()
        else:
            window.destroy()
    else:
        window.after_cancel(flip_timer)
        word = choice(data)
        canvas.itemconfig(canvas_image, image=card_front)
        canvas.itemconfig(card_title, text="English", fill='black')
        canvas.itemconfig(card_word, text=word['English'], fill='black')
        flip_timer = window.after(3000, flip)


def remove_word_and_update():
    global word, data
    if len(data):
        data.remove(word)
        df = pd.DataFrame(data)
        df.to_csv("data/words_to_learn.csv", index=False)
        update_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, flip)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="English", font=("Ariel", 40, "italic"), fill="black")
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

button_right = Button(image=right_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=remove_word_and_update)
button_right.grid(row=1, column=0)
button_wrong = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=update_word)
button_wrong.grid(row=1, column=1)
update_word()

window.mainloop()
