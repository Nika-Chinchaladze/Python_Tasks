import pandas as pd


df = pd.read_csv("NATO.csv")

# dictionary = {df.iloc[index]['letter']: df.iloc[index]['code'] for (index, row) in df.iterrows()}
dictionary = {row['letter']: row['code'] for (index, row) in df.iterrows()}

again = True
while again:
    word = input("Enter Your Name: ").upper()
    if word == "EXIT":
        again = False
    else:
        # letter_list = [character for character in word]
        # answer_list = [value for character in letter_list for (key, value) in dictionary.items() if character == key]
        answer_list = [dictionary[letter] for letter in word]
        print(answer_list)
