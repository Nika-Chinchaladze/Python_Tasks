import pandas as pd


df = pd.read_csv("50_states.csv")
df["state"] = df["state"].apply(lambda row: row.lower())


def check_if_exists(guessed_answer):
    if len(df[df["state"] == guessed_answer]) > 0:
        return True


def return_location(guessed_word):
    x_location = df[df["state"] == guessed_word]["x"]
    y_location = df[df["state"] == guessed_word]["y"]
    coordinates = [x_location, y_location]
    return coordinates


def save_into_csv(guessed_list):
    # define data:
    not_answered_list = []
    whole_list = df["state"].to_list()
    for state_name in whole_list:
        if state_name not in guessed_list:
            not_answered_list.append(state_name)
    # save into csv:
    new_df = pd.DataFrame(data=not_answered_list, columns=["Not Answered States"])
    new_df.to_csv("Not_Answered.csv", index=False)
