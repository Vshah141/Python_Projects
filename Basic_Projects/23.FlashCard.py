from tkinter import *
import pandas as pd
import random

BACKGROUNDCOLOR = "#B1DDC6"
current_card = {}

df = pd.read_csv("C:/Users/vyoms/Downloads/french.csv")
to_learn = df.to_dict(orient="records")
# print(df)

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French",fill="black")
    canvas.itemconfig(card_word, text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front)
    flip_timer=window.after(3000,func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word,text=current_card["Hindi"],fill="white")
    canvas.itemconfig(card_background, image=card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUNDCOLOR)
window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

canvas.grid(row=0, column=0, columnspan=2)
card_front = PhotoImage(file="C:/vs code/ezgif.com-gif-maker (1).gif")
card_back = PhotoImage(file="C:/vs code/back_card.gif")
canvas.create_image(400, 263, image=card_front)
card_background = canvas.config(bg=BACKGROUNDCOLOR, highlightthickness=0)
card_title = canvas.create_text(
    400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 36, "bold"))

tick_image = PhotoImage(file="tick.gif")
b1 = Button(image=tick_image, height=125, width=125,
            highlightthickness=0, command=next_card)
b1.grid(row=1, column=0)

cross_image = PhotoImage(file="C:/vs code/PYTHON/cross.gif")
b2 = Button(image=cross_image, height=150, width=150,
            highlightthickness=0, command=next_card)
b2.grid(row=1, column=1)


flip_card()


window.mainloop()

