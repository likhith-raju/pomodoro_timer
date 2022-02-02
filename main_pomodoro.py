from tkinter import *
import math
from playsound import playsound


PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

def reset():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    subcaption.config(text="Timer")
    check_marks.config(text="")


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If 1st/3rd/5th/7th rep

    # if it's the 8th rep
    if reps % 8 == 0:
        subcaption.config(text="Long Break", fg=RED)
        countdown(long_break_sec)
        playsound('pomodoro_timer/beep-07a.mp3')
    # if it 2nd /4th/6th rep
    if reps % 2 == 0:
        subcaption.config(text="Short Break", fg=PINK)
        countdown(short_break_sec)
        playsound('pomodoro_timer/beep-07a.mp3')
        print()
    else:

        subcaption.config(text="Work Session")
        countdown(work_sec)
        playsound('pomodoro_timer/beep-07a.mp3')



def countdown(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        window.after(1000, countdown, count - 1)

    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
        check_marks.config(text=mark)



window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


def say_something(a, b, c):
    print(a)
    print(b)
    print(c)


subcaption = Label(text="Work Time", fg=GREEN, bg=YELLOW, font=("Arial", 14, "bold"))
subcaption.grid(column=1, row=1)

heading = Label(text="Pomodoro Timer", fg=GREEN, bg=YELLOW, font=("Arial", 24, "bold"))
heading.grid(column=1, row=0)
fg = GREEN
canvas = Canvas(width="200", height="224", bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset)
reset_button.grid(column=2, row=2)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

author_label = Label(text="Likhith Raju")
author_label.grid(column=1, row=5)

window.mainloop()

  
