from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Pomodoro")
windows.config(padx=100, pady=50, bg=YELLOW)

def start():
    return

def reset():
    return

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

first_label = Label(text="Timer", font=("Arial", 40), fg=GREEN, bg=YELLOW)
first_label.grid(column=1, row=0)

image = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=image)

canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(column=1, row=1)

button = Button(text="Start", command=start)
button.grid(column=0, row=2)

button = Button(text="Reset", command=reset)
button.grid(column=2, row=2)

check_label = Label(text="✔", font=("Arial", 15), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

windows.mainloop()