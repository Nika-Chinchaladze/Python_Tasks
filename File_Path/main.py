# read invited names from file:
with open("./Input/Names/Invited_Names.txt", "r") as name_file:
    names = name_file.readlines()
    name_file.close()
    pass
good_names = [name.strip() for name in names]

# read invitation letter form:
with open("./Input/Letters/Starting_Letter.txt", "r") as letter_form:
    text_format = letter_form.read()
    letter_form.close()
    pass

# prepare invitation letters for everyone:
for invited in good_names:
    new_letter = text_format.replace("Name", f"{invited}")
    with open(f"./Output/Ready_To_Send/letter for {invited}.txt", "w") as letters:
        letters.write(f"{new_letter}")
        letters.close()
        pass
