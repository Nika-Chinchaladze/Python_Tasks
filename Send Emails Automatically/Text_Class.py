from random import choice


class PrepareText:
    def __init__(self):
        self.letter_form = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

    def return_text(self, name):
        file_name = choice(self.letter_form)
        with open(f"./Letters/{file_name}", "r") as msg_form:
            old_content = msg_form.read()
            msg_form.close()
        new_content = old_content.replace("[NAME]", name)
        return new_content
