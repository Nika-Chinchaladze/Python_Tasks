import pandas as pd


class PandaDealer:
    def __init__(self):
        self.df = pd.read_csv("./BirthDates/birthdays.csv")
        self.answer = None

    def return_wanted_raw(self, month, day):
        self.answer = self.df[(self.df['month'] == month) & (self.df['day'] == day)][['name', 'email']]
        self.answer = self.answer.values.tolist()
        return self.answer

    def return_name(self, now_month, now_day):
        try:
            name = self.return_wanted_raw(month=now_month, day=now_day)[0][0]
            return name
        except IndexError:
            return "not found"

    def return_mail(self, now_month, now_day):
        try:
            mail = self.return_wanted_raw(month=now_month, day=now_day)[0][1]
            return mail
        except IndexError:
            return "not found"
