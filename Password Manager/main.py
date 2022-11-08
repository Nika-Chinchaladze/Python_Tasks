from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from file import WorkFile
from password import PasswordCreator
import pyperclip

LABEL_FONT = ("Arial", 10, "normal")


class Password:
    def __init__(self, window):
        self.window = window
        self.window.title("Password Manager")
        self.window.geometry("500x500")
        self.window.config(bg="white")
        # extra variables:
        self.website_name = StringVar()
        self.email_name = StringVar()
        self.pass_name = StringVar()

        # add main Frame:
        self.main_frame = Frame(self.window, bg="white")
        self.main_frame.place(x=100, y=30, width=300, height=260)

        # add security image:
        security_image = Image.open("security.png")
        used_image = ImageTk.PhotoImage(security_image)
        self.security_label = Label(self.main_frame, image=used_image, bd=0)
        self.security_label.image = used_image
        self.security_label.pack()

        # labels Frame:
        self.below_frame = Frame(self.window, bg="white")
        self.below_frame.place(x=25, y=300, width=480, height=150)
        # labels:
        self.website_label = Label(self.below_frame, text="Website:", font=LABEL_FONT, bg="white")
        self.website_label.grid(row=0, column=0)

        self.email_label = Label(self.below_frame, text="Email/Username:", font=LABEL_FONT, bg="white")
        self.email_label.grid(row=1, column=0)

        self.password_label = Label(self.below_frame, text="Password:", font=LABEL_FONT, bg="white")
        self.password_label.grid(row=2, column=0)
        # Entries:
        self.website_entry = Entry(self.below_frame, font=LABEL_FONT, width=46, justify="center", bd=2,
                                   textvariable=self.website_name)
        self.website_entry.grid(row=0, column=1, columnspan=2, pady=5)
        self.website_entry.focus()

        self.email_entry = Entry(self.below_frame, font=LABEL_FONT, width=46, justify="center", bd=2,
                                 textvariable=self.email_name)
        self.email_entry.grid(row=1, column=1, columnspan=2, pady=5)
        self.email_entry.insert(END, "chincho@gmail.com")

        self.password_entry = Entry(self.below_frame, font=LABEL_FONT, width=26, justify="center", bd=2,
                                    textvariable=self.pass_name)
        self.password_entry.grid(row=2, column=1, pady=5)

        # Buttons:
        self.generate_button = Button(self.below_frame, text="Generate Password", font=LABEL_FONT, width=16,
                                      bg="light gray", command=self.generate_password)
        self.generate_button.grid(row=2, column=2, pady=5)

        self.add_button = Button(self.below_frame, text="Add", font=LABEL_FONT, width=40, bg="dark sea green",
                                 command=self.save_info)
        self.add_button.grid(row=3, column=1, columnspan=2, pady=5)

        # =============================== FUNCTIONALITY ================================= #
    def save_info(self):
        hand = WorkFile()
        if hand.check_empty(self.website_name.get(), self.email_name.get(), self.pass_name.get()):
            confirm = messagebox.askokcancel(title="Confirmation", message=f"These are entered details: "
                                                                           f"\nWebsite: {self.website_name.get()} "
                                                                           f"\nEmail: {self.email_name.get()} "
                                                                           f"\nPassword: {self.pass_name.get()} "
                                                                           f"\nAre you sure to save?")
            if confirm:
                hand.append_text(self.website_name.get(), self.email_name.get(), self.pass_name.get())
                self.website_entry.delete(0, END)
                self.email_entry.delete(0, END)
                self.password_entry.delete(0, END)
                messagebox.showinfo(title="About Save", message="Information Has Been Added, Successfully!")
            else:
                pass
        else:
            messagebox.showwarning(title="Oops", message="All fields must be filled!")

    def generate_password(self):
        need = PasswordCreator()
        new_password = need.create_password()
        self.password_entry.delete(0, END)
        self.password_entry.insert(END, new_password)
        pyperclip.copy(new_password)


def launch_program():
    app = Tk()
    Password(app)
    app.mainloop()


if __name__ == "__main__":
    launch_program()
