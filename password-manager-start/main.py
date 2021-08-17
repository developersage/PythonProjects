from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
from pyperclip import copy
import json
import string
import pandas as pd

# try:
#     df = pd.read_csv("data.csv")
# except FileNotFoundError:
#     df = pd.DataFrame(columns=["Website", "Email/Username", "Password"])
#     df.to_csv("data.csv", index=False)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation


def pw_gen():
    password_list = [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    copy(password)
    entry_pw.delete(0, END)
    entry_pw.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_web.get()
    email = entry_user.get()
    password = entry_pw.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website and email and password:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password} \nIs it okay to save?")
        if is_ok:
            # a_list = [website, email, password]
            # a_series = pd.Series(a_list, index=df.columns)
            # df.loc[len(df.index)] = a_series
            # df.to_csv("data.csv", index=False)
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)
            finally:
                entry_web.delete(0, END)
                entry_pw.delete(0, END)
    else:
        messagebox.showwarning(title="Password Manager", message="Please fill in all of the entries.")


# ---------------------------- SEARCH DATA ------------------------------- #
def search():
    website = entry_web.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
        email = data[website]["email"]
        password = data[website]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found.")
    except KeyError:
        messagebox.showerror(title="Error", message="No details for the website exists.")
    else:
        messagebox.showinfo(title=website, message=f"Email: {email} \nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

label_web = Label(text="Website: ")
label_user = Label(text="Email/Username: ")
label_pw = Label(text="Password: ")

entry_web = Entry(width=21)
entry_web.insert(0, "Google")
entry_user = Entry(width=35)
entry_user.insert(0, "sangdo719@gmail.com")
entry_pw = Entry(width=21)

button_search = Button(text="Search", width=10, command=search)
button_gen = Button(text="Generate Password", width=14, command=pw_gen)
button_add = Button(text="Add", width=35, command=save)

label_web.grid(row=1, column=0)
label_user.grid(row=2, column=0)
label_pw.grid(row=3, column=0)
entry_web.grid(row=1, column=1)
entry_user.grid(row=2, column=1, columnspan=2)
entry_pw.grid(row=3, column=1)
button_search.grid(row=1, column=2)
button_gen.grid(row=3, column=2)
button_add.grid(row=4, column=1, columnspan=2)



window.mainloop()