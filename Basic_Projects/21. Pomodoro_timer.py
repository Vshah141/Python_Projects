import tkinter
import time
import math
WORK_MIN = 25
SHORT_BREAK = 5
reps = 0
LONG_BREAK_MIN = 20
timer = None


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Timer")


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        label.config(text="Break", fg="RED")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        label.config(text="Break", fg="PINK")
    else:
        countdown(work_sec)
        label.config(text="Work", fg="GREEN")


def countdown(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if (count_sec < 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count-1)
    else:
        start_timer()


def breaktime(count):

    count_min = math.floor(count/60)
    count_sec = count % 60
    if (count_sec < 10):
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, countdown, count-1)


window = tkinter.Tk()
window.title("POMODORO")
window.config(padx=100, pady=50, bg="#f7f5dd")

label = tkinter.Label(text="Timer", font=("Arial", 35, "bold"), fg="green")
label.grid(column=1, row=0)

canvas = tkinter.Canvas(width=512, height=512,
                        bg="yellow", highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="C:\Dummy folder\pomodoro.png")
canvas.create_image(256, 256, image=tomato_img)
timer_text = canvas.create_text(
    250, 250, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.grid(column=1, row=1)


b1 = tkinter.Button(text="Start", font=(
    "Arial", 35, "bold"), command=start_timer)
b1.grid(column=0, row=2)
b1 = tkinter.Button(text="Reset", font=(
    "Arial", 35, "bold"), command=reset_timer)
b1.grid(column=2, row=2)


window.mainloop()
