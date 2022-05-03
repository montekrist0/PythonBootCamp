from tkinter import *
from quiz_brain import QuizBrain
import time

THEME_COLOR = "#375362"


def check():
    return 1


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.score = 0
        self.cur_question = "Here will be a question"
        self.window.config(bg=THEME_COLOR, padx=20)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280,
                                                     text=self.quiz.next_question(),
                                                     font=("Arial", 20, "italic"),
                                                     fill="black"
                                                     )
        self.canvas.grid(row=1, column=0, columnspan=2)
        # --------------------SCORE LABELS-------------------------
        self.score_label = Label(self.window, text=f"Score: {self.quiz.score}", background=THEME_COLOR)
        self.score_label.grid(row=0, column=1, padx=20, pady=20)
        # --------------------BUTTONS-------------------------
        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_true)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_false)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text, text=self.quiz.next_question())
        else:
            self.canvas.itemconfig(self.question_text, text="THE END")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def check_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(background="green")
            self.score_label.config(text=f"Score: {self.quiz.score}")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)
