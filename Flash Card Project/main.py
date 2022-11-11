from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
from random import choice

DATA_LOCATION = "./used_data/unknown_words.csv"
LEARNT_LOCATION = "./used_data/learnt_words.csv"
FRONT_IMAGE = "./used_images/front.png"
BACK_IMAGE = "./used_images/back.png"
WRONG_IMAGE = "./used_images/wrong.png"
RIGHT_IMAGE = "./used_images/right.png"
TITLE_FONT = ("Arial", 20, "italic")
WORD_FONT = ("Arial", 25, "bold")
TIMER_FONT = ("Courier", 20, "bold")
BUTTON_FONT = ("Courier", 15, "normal")


class FlashCard:
    def __init__(self, window):
        self.window = window
        self.window.title("FlashCard")
        self.window.config(bg="#B1DDC6", width=600, height=420)
        # extra variables:
        self.df = pd.read_csv(DATA_LOCATION)
        self.learn = self.df.to_dict(orient="records")
        self.random_word = None
        self.second = 3
        self.timer = None
        self.french_word = ""
        self.english_word = ""
        self.known_words = []
        self.forgot_words = []
        self.answered_words = []
        self.unknown_list = []

        # timer label:
        self.timer_label = Label(self.window, text="", font=TIMER_FONT, justify="center", bg="#B1DDC6")
        self.timer_label.place(x=560, y=10, width=30, height=50)

        # center frame:
        self.center_frame = Frame(self.window, bg="#B1DDC6")
        self.center_frame.place(x=50, y=20, width=500, height=310)

        # image preparation:
        self.used_image = Image.open(FRONT_IMAGE)
        self.used_photo = ImageTk.PhotoImage(self.used_image)

        self.ground_label = Label(self.center_frame, image=self.used_photo, bg="#B1DDC6")
        self.ground_label.image = self.used_photo
        self.ground_label.pack()

        # Words:
        self.title_label = Label(self.center_frame, text="", justify="center", font=TITLE_FONT, bg="#D9D9D9")
        self.title_label.place(x=150, y=50, width=200, height=50)

        self.word_label = Label(self.center_frame, text="", justify="center", font=WORD_FONT, bg="#D9D9D9")
        self.word_label.place(x=125, y=130, width=250, height=50)

        self.display_with_wrong()

        # Buttons:
        self.wrong_image = Image.open(WRONG_IMAGE)
        wrong_photo = ImageTk.PhotoImage(self.wrong_image)

        self.wrong_button = Button(self.window, image=wrong_photo, bd=0, bg="#B1DDC6", command=self.display_with_wrong)
        self.wrong_button.image = wrong_photo
        self.wrong_button.place(x=100, y=330)

        self.right_image = Image.open(RIGHT_IMAGE)
        right_photo = ImageTk.PhotoImage(self.right_image)

        self.right_button = Button(self.window, image=right_photo, bd=0, bg="#B1DDC6", command=self.display_with_right)
        self.right_button.image = right_photo
        self.right_button.place(x=420, y=330)

        self.save_progress = Button(self.window, text="save progress", font=BUTTON_FONT, bd=2, bg="#B1DDC6",
                                    relief=RIDGE, cursor="hand2", command=self.save_learning_progress)
        self.save_progress.place(x=210, y=345)

        self.start_method()

    # ================================ FUNCTIONALITY =================================== #
    def change_images_back(self):
        self.used_image = Image.open(BACK_IMAGE)
        self.used_photo = ImageTk.PhotoImage(self.used_image)

        self.ground_label.config(image=self.used_photo)
        self.ground_label.image = self.used_photo

        self.title_label.config(bg="#A9D18E")
        self.word_label.config(bg="#A9D18E")

    def change_images_front(self):
        self.used_image = Image.open(FRONT_IMAGE)
        self.used_photo = ImageTk.PhotoImage(self.used_image)

        self.ground_label.config(image=self.used_photo)
        self.ground_label.image = self.used_photo

        self.title_label.config(bg="#D9D9D9")
        self.word_label.config(bg="#D9D9D9")

    def display_with_wrong(self):
        self.change_images_front()
        self.title_label.config(text="French", fg="green")
        self.random_word = choice(self.learn)
        self.word_label.config(text=self.random_word["French"], fg="green")
        self.french_word = self.random_word["French"]
        self.english_word = self.random_word["English"]
        self.track_time(self.second)

    def display_with_right(self):
        self.display_with_wrong()
        self.known_words.append(self.random_word)
        self.learn.remove(self.random_word)

    def display_english_translation(self):
        self.title_label.config(text="English", fg="maroon")
        self.word_label.config(text=self.english_word, fg="maroon")
        self.change_images_back()
        self.timer_label.config(text="")

    def track_time(self, number):
        if number < 4:
            self.timer_label.config(text=f"{number}")
        if number > 0:
            self.timer = self.window.after(1000, self.track_time, number - 1)
        else:
            self.window.after_cancel(self.timer)
            self.display_english_translation()

    def start_method(self):
        self.track_time(self.second)

    def save_learning_progress(self):
        # refreshed data structure:
        self.answered_words = []
        self.unknown_list = []
        # save learnt words:
        old_result = pd.read_csv(LEARNT_LOCATION)
        self.answered_words = [list(dictionary.values()) for dictionary in self.known_words]
        current_result = pd.DataFrame(self.answered_words, columns=["French", "English"])
        new_result = pd.concat([old_result, current_result])
        new_result.to_csv(LEARNT_LOCATION, index=False)
        # keep only unknown words:
        self.unknown_list = [list(item.values()) for item in self.learn]
        unknown_result = pd.DataFrame(self.unknown_list, columns=["French", "English"])
        unknown_result.to_csv(DATA_LOCATION, index=False)
        messagebox.showinfo(title="progress", message="Progress has been saved!")


def launch_program():
    app = Tk()
    FlashCard(app)
    app.mainloop()


if __name__ == "__main__":
    launch_program()
