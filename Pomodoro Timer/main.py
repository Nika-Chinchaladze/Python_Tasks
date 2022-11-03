from tkinter import *
from math import floor


# ---------------------------- CONSTANTS ------------------------------- #
GREEN = "green"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SECOND = 20
SHORT_BREAK_SECOND = 5
LONG_BREAK_MIN = 10
STEP = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfigure(canvas_item, text="00:00")
    check_label.config(text="")
    global STEP
    STEP = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def timer_mechanism():
    global STEP
    STEP += 1
    if STEP % 2 == 1:
        count_time(WORK_SECOND)
        timer_label.config(text="WORK", fg="green")
    elif STEP % 8 == 0:
        count_time(LONG_BREAK_MIN)
        timer_label.config(text="Break", fg="red")
    else:
        count_time(SHORT_BREAK_SECOND)
        timer_label.config(text="Break", fg="blue")


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_time(number):
    minute = floor(number / 60)
    second = number % 60
    if second < 10:
        second = f"0{second}"
    canvas.itemconfigure(canvas_item, text=f"0{minute}:{second}")
    if number > 0:
        global timer
        timer = window.after(1000, count_time, number - 1)
    else:
        timer_mechanism()
        sighs = ""
        for i in range(floor(STEP/2)):
            sighs += "✔"
        check_label.config(text=sighs)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
canvas_item = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "normal"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

check_label = Label(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(row=3, column=1)

start_button = Button(text="Start", font=(FONT_NAME, 15, "normal"), bg=YELLOW, highlightthickness=0,
                      command=timer_mechanism)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", font=(FONT_NAME, 15, "normal"), bg=YELLOW, highlightthickness=0,
                      command=reset_timer)
reset_button.grid(row=2, column=2)


window.mainloop()
