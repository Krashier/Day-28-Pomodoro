from tkinter import *
import math


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 8
START_GAME = True
actual_check = ""
time = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
    global actual_check, REPS
    windows.after_cancel(time)
    canvas.itemconfig(time_text, text=f"{0:02d}:{0:02d}")
    first_label.config(text="Timer", fg=GREEN)
    actual_check = ""
    REPS = 8


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start():
    global REPS, actual_check
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60

    if REPS > 0:
        if REPS == 1:
            actual_check += "✔"
            count_down(long_break_time)
            first_label.config(text="Break",fg=RED)
            check_label.config(text=actual_check)
        elif REPS % 2 == 0:
            count_down(work_time)
            first_label.config(text="Work",fg=GREEN)
        else:
            actual_check += "✔"
            count_down(short_break_time)
            check_label.config(text=actual_check)
            first_label.config(text="Break",fg=PINK)
        REPS -= 1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    canvas.itemconfig(time_text, text=f"{minutes:02d}:{seconds:02d}")
    if count > 0:
        global time
        time = windows.after(1000, count_down, count - 1)
    else:
        start()

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

first_label = Label(text="Timer", font=("Arial", 40), fg=GREEN, bg=YELLOW)
first_label.grid(column=1, row=0)

image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=image)

time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_label = Label(text=actual_check, font=("Arial", 15), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

windows.mainloop()