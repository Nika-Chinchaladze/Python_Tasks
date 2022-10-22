class WorkTxt:
    def __init__(self):
        self.hello = "hello, world"

    def write_txt(self, highest_score):
        with open("highest_score.txt", "w") as file:
            file.write(f"{highest_score}")
            file.close()
            pass

    def read_txt(self):
        with open("highest_score.txt", "r") as file:
            number = file.read()
            file.close()
            pass
        return number
