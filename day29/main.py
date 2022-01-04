import tkinter.messagebox
from tkinter import *
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def gen_password():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list = [random.choice(letters) for x in range(nr_letters)]
    password_list += [random.choice(symbols) for x in range(nr_symbols)]
    password_list += [random.choice(numbers) for x in range(nr_numbers)]
    random.shuffle(password_list)
    password = ''.join(password_list)
    pyperclip.copy(password)
    password_text.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    site = website_text.get()
    email = email_text.get()
    password = password_text.get()
    new_data = {
        site: {
            "email": email,
            "password": password
        }
    }
    # is_ok = tkinter.messagebox.askokcancel(title=site, message=f"Email:{email}\nPassword:{password}\n Proceed?")
    if site == "" or email == "" or password == "":
        tkinter.messagebox.showinfo(title="Empty fields", message="Please don't left fields empty")
    else:
        try:
            with open("data.json", 'r') as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)
        finally:
            website_text.delete(0, END)
            password_text.delete(0, END)
            tkinter.messagebox.showinfo(message="Password was successfully added to DB")


# ---------------------------- SEARCH in DB ------------------------------- #
def search():
    try:
        with open("data.json", 'r') as file:
            data = json.load(file)
            website = website_text.get()
            tkinter.messagebox.showinfo(message=f"Data for '{website}' website:\n"
                                                f"Email: {data[website]['email']}\n"
                                                f"Password: {data[website]['password']}")

    except FileNotFoundError:
        tkinter.messagebox.showinfo(message="No data in Database yet")
    except KeyError as key_error:
        tkinter.messagebox.showinfo(message=f"There is no {key_error} website in Database")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_text = Entry(width=21)
website_text.focus()
website_text.grid(row=1, column=1, columnspan=1)
sch_button = Button(text="Search", width=13, command=search)
sch_button.grid(row=1, column=2)

email_text = Entry(width=38)
email_text.insert(0, "user@mail.ru")
email_text.grid(row=2, column=1, columnspan=2)

password_text = Entry(width=21)
password_text.grid(row=3, column=1)
gen_pass_button = Button(text="Generate Password", width=13, command=gen_password)
gen_pass_button.grid(row=3, column=2)

add_button = Button(width=36, text="Add", command=save_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
