from tkinter import Tk, Label, Button, Entry, StringVar, ttk

UNITS = ["Mile", "Kilometer", "Meter"]
FONT = ("Arial", 12, "bold")


# functions:
def calculate():
    from_unit = from_box.get()
    to_unit = to_box.get()
    quantity = number_entry.get()
    if from_unit == "Mile" and to_unit == "Mile":
        answer = float(quantity)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Mile" and to_unit == "Kilometer":
        answer = round(float(quantity) * 1.60934, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Mile" and to_unit == "Meter":
        answer = round(float(quantity) * 1609.34, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Kilometer" and to_unit == "Mile":
        answer = round(float(quantity) * 0.621371, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Kilometer" and to_unit == "Kilometer":
        answer = float(quantity)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Kilometer" and to_unit == "Meter":
        answer = round(float(quantity) * 1000, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Meter" and to_unit == "Mile":
        answer = round(float(quantity) * 0.000621371, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Meter" and to_unit == "Kilometer":
        answer = round(float(quantity) / 1000, 2)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")
    elif from_unit == "Meter" and to_unit == "Meter":
        answer = float(quantity)
        answer_label.config(text=f"{quantity} {from_unit} is {answer} {to_unit}")


# prepare window:
window = Tk()
window.title("Unit Converter")
window.minsize(width=250, height=250)
window.config(padx=30, pady=30)
window.configure(bg="silver")

# prepare labels:
hello_label = Label(text="Welcome To Unit Converter App", font=("Arial", 14, "bold"))
hello_label.grid(row=0, column=1)
hello_label.config(padx=10, pady=10)
hello_label.configure(bg="light gray")

from_label = Label(text="From", font=FONT)
from_label.grid(row=1, column=0)
from_label.config(padx=10, pady=10)
from_label.configure(bg="silver")

quantity_label = Label(text="Quantity", font=FONT)
quantity_label.grid(row=1, column=1)
quantity_label.config(padx=10, pady=10)
quantity_label.configure(bg="silver")

to_label = Label(text="To", font=FONT)
to_label.grid(row=1, column=2)
to_label.config(padx=10, pady=10)
to_label.configure(bg="silver")

answer_label = Label(text="", font=("Arial", 15, "bold"), justify="center")
answer_label.grid(row=4, column=1)
answer_label.config(padx=20, pady=20)
answer_label.grid(row=5, column=1)
answer_label.configure(bg="silver")

space_label = Label()
space_label.grid(row=3, column=1)
space_label.configure(bg="silver")

# prepare buttons, entry and combobox:
calculate_button = Button(text="Calculate", command=calculate, font=FONT, justify="center")
calculate_button.grid(row=4, column=1)
calculate_button.configure(bg="forest green")

number_entry = Entry(justify="center", font=FONT)
number_entry.grid(row=2, column=1)

selected_from_unit = StringVar()
selected_to_unit = StringVar()
from_box = ttk.Combobox(window, textvariable=selected_from_unit, font=FONT, justify="center")
to_box = ttk.Combobox(window, textvariable=selected_to_unit, font=FONT, justify="center")
from_box.grid(row=2, column=0)
to_box.grid(row=2, column=2)
from_box["values"] = [item for item in UNITS]
to_box["values"] = [item for item in UNITS]


window.mainloop()
