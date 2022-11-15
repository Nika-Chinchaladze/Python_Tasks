from tkinter import *
from PIL import Image, ImageTk
from API_Class import ImportKanye


class KanyeWords:
    def __init__(self, window):
        self.window = window
        self.window.title("Kanye Words")
        self.window.geometry("400x580")

        cloud_image = Image.open("./kanye_img/background.png")
        cloud_photo = ImageTk.PhotoImage(cloud_image)
        self.cloud_label = Label(self.window, image=cloud_photo)
        self.cloud_label.image = cloud_photo
        self.cloud_label.place(x=50, y=0)

        self.phrase_label = Label(self.cloud_label, text="", font=("Arial", 16, "bold"), justify=LEFT, fg="chocolate",
                                  wraplength=250, bg="#FBD53A")
        self.phrase_label.place(x=20, y=50, width=260, height=270)

        actor_image = Image.open("./kanye_img/kanye.png")
        actor_photo = ImageTk.PhotoImage(actor_image)
        self.actor_button = Button(self.window, image=actor_photo, command=self.display_phrases)
        self.actor_button.image = actor_photo
        self.actor_button.place(x=150, y=430)

    # ====================== FUNCTIONALITY ================================= #
    def display_phrases(self):
        hand_tool = ImportKanye()
        phrase = hand_tool.get_phrases()
        self.phrase_label.config(text=phrase)


def launch_program():
    app = Tk()
    KanyeWords(app)
    app.mainloop()


if __name__ == "__main__":
    launch_program()
