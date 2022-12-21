from flask import Flask
from random import randint
app = Flask(__name__)

computer_number = randint(0, 9)


@app.route("/")
def start_game():
    return """
        <body style="background-color: Azure; padding-top: 10px;">
        <div style="width: 50%; height=auto; margin: auto; text-align: center;">
        <h1 style="color: green;">Guess The Number Between 0 and 9</h1>
        <img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp" alt="start gif">
        </div>
        </body>
        """


@app.route("/<int:number>")
def player_answer(number):
    if number == computer_number:
        return """
        <body style="background-color: Azure; padding-top: 10px;">
        <div style="width: 50%; height=auto; margin: auto; text-align: center;">
        <h1 style="color: green;">You Find Me</h1>
        <img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp" alt="start gif">
        </div>
        </body>
        """
    elif number > computer_number:
        return """
        <body style="background-color: Azure; padding-top: 10px;">
        <div style="width: 50%; height=auto; margin: auto; text-align: center;">
        <h1 style="color: green;">Too High, Try Again</h1>
        <img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp" alt="start gif">
        </div>
        </body>
        """
    else:
        return """
        <body style="background-color: Azure; padding-top: 10px;">
        <div style="width: 50%; height=auto; margin: auto; text-align: center;">
        <h1 style="color: green;">Too Low, Try Again</h1>
        <img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp" alt="start gif">
        </div>
        </body>
        """


if __name__ == "__main__":
    app.run(debug=True)
