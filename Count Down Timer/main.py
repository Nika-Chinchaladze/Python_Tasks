from tkinter import *
from math import floor

TIMER_FONT = ("Courier", 30, "bold")
BIG_FONT = ("Courier", 50, "bold")
BUTTON_FONT = ("Arial", 20, "normal")
SMALL_FONT = ("Arial", 15, "bold")
WORKING_TIME = 70
SHORT_BREAK = 10
LONG_BREAK = 20
INFO = ["Working Time:\t\t 70 Seconds", "Short Break:\t\t 10 Seconds", "Long Break:\t\t 20 Seconds"]


class Timer:
    def __init__(self, window):
        self.window = window
        self.window.geometry("400x600")
        self.window.title("Timer App")
        self.window.configure(bg="dark slate gray")
        self.step = 0
        self.timer = ""
        self.minute = 0
        self.second = 0
        self.minute_holder = 0
        self.second_holder = 0

        self.timer_label = Label(self.window, text="", font=TIMER_FONT, bg="dark slate gray", fg="goldenrod")
        self.timer_label.place(x=50, y=25, width=300, height=40)

        # ======================================== TOP FRAME ========================================= #
        self.top_frame = LabelFrame(self.window, relief=RIDGE, bd=3, bg="dark slate gray")
        self.top_frame.place(x=10, y=80, width=380, height=130)

        self.running_time = Label(self.top_frame, text="", font=BIG_FONT, bg="dark slate gray", fg="white")
        self.running_time.place(x=25, y=20)

        # ======================================== BOTTOM FRAME ======================================= #
        self.bottom_frame = LabelFrame(self.window, relief=RIDGE, bd=3, bg="dark slate gray")
        self.bottom_frame.place(x=10, y=450, width=380, height=120)

        self.info_text = Text(self.bottom_frame, font=SMALL_FONT, width=30, height=3, bg="dark slate gray", bd=0,
                              fg="khaki")
        self.info_text.place(x=20, y=15)

        # ========================================= SMILE ========================================== #
        self.smile = Label(self.window, text="", font=("Courier", 40, "bold"), anchor=CENTER, bd=0,
                           bg="dark slate gray", fg="gold")
        self.smile.place(x=10, y=215, width=377, height=45)

        # ========================================= BUTTONS ========================================== #
        turn_button = Button(self.window, text="Turn On/Off", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                             bg="indian red", command=self.turn_on_off)
        turn_button.place(x=10, y=260)

        start_button = Button(self.window, text="Start", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                              bg="sea green", command=self.start_method)
        start_button.place(x=218, y=260)

        reset_button = Button(self.window, text="Reset", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                              bg="tomato", command=self.reset_method)
        reset_button.place(x=10, y=320)

        pause_button = Button(self.window, text="Pause", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                              bg="steel blue", command=self.pause_method)
        pause_button.place(x=218, y=320)

        end_button = Button(self.window, text="Close", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                            bg="pale violet red", command=self.close_window)
        end_button.place(x=10, y=380)

        continue_button = Button(self.window, text="Continue", font=BUTTON_FONT, relief=RIDGE, width=10, height=1,
                                 bg="dodger blue", command=self.continue_method)
        continue_button.place(x=218, y=380)

    # ====================================== FUNCTIONALITY ================================================= #
    def turn_on_off(self):
        if len(self.timer_label.cget("text")) > 0:
            self.running_time.config(text="")
            self.timer_label.config(text="")
            self.smile.config(text="")
            self.info_text.delete("1.0", END)
            self.step = 0
            self.window.after_cancel(self.timer)
        else:
            self.running_time.config(text="00:00:00")
            self.timer_label.config(text="Timer")
            self.fill_text()

    def fill_text(self):
        self.info_text.insert(END, INFO[0] + "\n")
        self.info_text.insert(END, INFO[1] + "\n")
        self.info_text.insert(END, INFO[2] + "\n")

    def close_window(self):
        self.window.destroy()

    def track_time(self, number):
        self.minute = floor(number / 60)
        self.second = number % 60
        if self.second < 10:
            self.running_time.config(text=f"00:0{self.minute}:0{self.second}")
        else:
            self.running_time.config(text=f"00:0{self.minute}:{self.second}")
        if number > 0:
            self.timer = self.window.after(1000, self.track_time, number - 1)
        else:
            self.start_method()
            sighs = ""
            for i in range(floor(self.step / 2)):
                sighs += "☻"
            self.smile.config(text=sighs)

    def start_method(self):
        self.step += 1
        if self.step % 4 == 0:
            self.track_time(LONG_BREAK)
            self.timer_label.config(text="Long Break", fg="red")
        elif self.step % 2 == 0:
            self.track_time(SHORT_BREAK)
            self.timer_label.config(text="Short Break", fg="orange red")
        else:
            self.track_time(WORKING_TIME)
            self.timer_label.config(text="Working Time", fg="chartreuse")

    def reset_method(self):
        self.step = 0
        self.running_time.config(text="00:00:00")
        self.timer_label.config(text="Timer")
        self.smile.config(text="")
        self.window.after_cancel(self.timer)

    def pause_method(self):
        self.minute_holder = self.minute
        self.second_holder = self.second
        self.window.after_cancel(self.timer)

    def continue_method(self):
        current_time = self.minute_holder * 60 + self.second_holder
        self.track_time(current_time)


app = Tk()
app_object = Timer(app)


app.mainloop()
