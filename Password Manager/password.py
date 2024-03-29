from random import randint, choice, shuffle


class PasswordCreator:
    def __init__(self):
        self.letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                        's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                        'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        self.nr_letters = randint(8, 10)
        self.nr_symbols = randint(2, 4)
        self.nr_numbers = randint(2, 4)

    def create_password(self):
        first = [choice(self.letters) for char_1 in range(self.nr_letters)]
        second = [choice(self.symbols) for char_2 in range(self.nr_symbols)]
        third = [choice(self.numbers) for char in range(self.nr_numbers)]
        result = first + second + third
        shuffle(result)
        password = "".join(result)
        return password
