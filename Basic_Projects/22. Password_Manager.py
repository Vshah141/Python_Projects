from tkinter import *
from tkinter import messagebox
import random


windows = Tk()

windows.title("Password Manager")

windows.config(padx=50, pady=50)
canvas = Canvas(height=200, width=200)
# logo_img=PhotoImage(file="WEBDEVELOPMENT\1645004636794.jpg")
# canvas.create_image(100,100,image=logo_img)
# canvas.grid(row=0,column=1)

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X",
           "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "@", "#", "$", "^", "&", "*", "(", ")"]


def genpass():
    l = random.randint(1, 3)
    n = random.randint(2, 3)
    s = random.randint(2, 3)
    password_list = []
    for x in range(0, l):
        password_list.append(random.choice(letters))

    for x1 in range(0, n):
        password_list.append(random.choice(numbers))

    for x2 in range(0, s):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = "".join(password_list)

    l3_entry.insert(0, password)


def save():
    website = l1_entry.get()
    email = l2_entry.get()
    password = l3_entry.get()

    if (len(website) == 0 or len(email) == 0 or len(password) == 0):
        messagebox.askretrycancel(
            title="Oops", message="Please dont leave any empty fields!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"These are the details entered: \n NAME:{website} \n EMAIL:{email}\n Password:{password}\n Is it Ok? ")

        if is_ok:

            with open("passmanagerdata.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                l1_entry.delete(0, END)
                l2_entry.delete(0, END)
                l3_entry.delete(0, END)


l1 = Label(text="Title")
l1.grid(row=1, column=0)
l2 = Label(text="Email/Username")
l2.grid(row=2, column=0)
l3 = Label(text="Password: ")
l3.grid(row=3, column=0)

l1_entry = Entry(width=35)
l1_entry.grid(row=1, column=1, columnspan=2)
l2_entry = Entry(width=35)
l2_entry.grid(row=2, column=1, columnspan=2)
l3_entry = Entry(width=21)
l3_entry.grid(row=3, column=1)

b1 = Button(text="Generate Password", width=14, command=genpass)
b1.grid(row=3, column=2, columnspan=2)
b2 = Button(text="Add", width=36, command=save)
b2.grid(row=4, column=1, columnspan=2)

windows.mainloop()
