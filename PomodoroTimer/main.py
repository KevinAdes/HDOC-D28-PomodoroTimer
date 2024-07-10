import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
CHECK_MARK = "✔"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = NONE

# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    check_label.config(text="")
    state_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    reps += 1
    length = 0
    if reps % 8 == 0:
        length = LONG_BREAK_MIN
        state_label.config(text="Break", fg=RED)
        reps = 0
    elif reps % 2 == 0:
        state_label.config(text="Break", fg=PINK)
        length = SHORT_BREAK_MIN
    else:
        state_label.config(text="Work", fg=GREEN)
        length = WORK_MIN
    count_down(length * 60)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    global timer
    minutes_remaining = math.floor(count/60)
    if minutes_remaining <= 9:
        minutes_remaining = f"0{minutes_remaining}"

    seconds_remaining = count % 60
    if seconds_remaining <= 9:
        seconds_remaining = f"0{seconds_remaining}"
    formatted_count = f"{minutes_remaining}:{seconds_remaining}"

    canvas.itemconfig(timer_text, text=formatted_count)
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        window.attributes('-topmost', True)
        window.attributes('-topmost', False)
        marks = ""
        work_sessions = math.floor((reps + 1)/2)
        for _ in range(work_sessions):
            marks += CHECK_MARK
        check_label.config(text=marks)
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

state_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))

tomato_image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", command=start_timer)
reset_button = Button(text="Reset", command=reset_timer)

check_label = Label(text="", bg=YELLOW, fg=GREEN)

state_label.grid(column=1, row=0)
canvas.grid(column=1, row=1)
start_button.grid(column=0, row=2)
reset_button.grid(column=2, row=2)
check_label.grid(column=1, row=3)

window.mainloop()
