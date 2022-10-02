from info import MENU, resources


def check_ability(outcome):
    if outcome == "espresso":
        basic = [
            resources["water"] >= MENU[outcome]["ingredients"]["water"],
            resources["coffee"] >= MENU[outcome]["ingredients"]["coffee"]
        ]
    else:
        basic = [
            resources["water"] >= MENU[outcome]["ingredients"]["water"],
            resources["coffee"] >= MENU[outcome]["ingredients"]["coffee"],
            resources["milk"] >= MENU[outcome]["ingredients"]["milk"]
        ]
    if outcome == "espresso":
        if (basic[0] is False) and (basic[1] is False):
            return "Sorry there is not enough water and coffee!"
        elif (basic[0] is False) and (basic[1] is True):
            return "Sorry there is not enough water!"
        elif (basic[0] is True) and (basic[1] is False):
            return "Sorry there is not enough coffee!"
        else:
            return "Please, insert coins!"
    else:
        if (basic[0] is False) and (basic[1] is False) and (basic[2] is False):
            return "Sorry there is not enough water, coffee and milk!"
        elif (basic[0] is False) and (basic[1] is False) and (basic[2] is True):
            return "Sorry there is not enough water and coffee!"
        elif (basic[0] is False) and (basic[1] is True) and (basic[2] is False):
            return "Sorry there is not enough water and milk!"
        elif (basic[0] is False) and (basic[1] is True) and (basic[2] is True):
            return "Sorry there is not enough water!"
        elif (basic[0] is True) and (basic[1] is False) and (basic[2] is False):
            return "Sorry there is not enough coffee and milk!"
        elif (basic[0] is True) and (basic[1] is False) and (basic[2] is True):
            return "Sorry there is not enough coffee!"
        elif (basic[0] is True) and (basic[1] is True) and (basic[2] is False):
            return "Sorry there is not enough milk!"
        else:
            return "Please, insert coins!"


def reduce_bit(ans):
    resources["water"] -= MENU[ans]["ingredients"]["water"]
    resources["coffee"] -= MENU[ans]["ingredients"]["coffee"]
    if ans != "espresso":
        resources["milk"] -= MENU[ans]["ingredients"]["milk"]


def process_coin(chosen, q, d, n, p):
    price = MENU[chosen]["cost"]
    inserted = (q*0.25) + (d*0.1) + (n*0.05) + (p*0.01)
    if inserted == price:
        resources["money"] += price
        reduce_bit(chosen)
        return f"Here is your {chosen}, Enjoy!"
    elif inserted > price:
        resources["money"] += price
        reduce_bit(chosen)
        refund = round(inserted - price, 2)
        return f"Here is ${refund} dollars in change and your {chosen}, Enjoy!"
    else:
        return "Sorry that's not enough money. Money refunded!"


turn = "on"
while turn == "on":
    guess = input("What would you like? (espresso/latte/cappuccino) ")
    if guess == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${resources['money']}")
    elif guess in ("espresso", "latte", "cappuccino"):
        ability = check_ability(guess)
        if ability == "Please, insert coins!":
            print("Please, insert coins!")
            quarter = int(input("Insert Quarters! "))
            dime = int(input("Insert Dimes! "))
            nickle = int(input("Insert Nickles! "))
            penny = int(input("Insert Pennies! "))
            print(process_coin(guess, quarter, dime, nickle, penny))
        else:
            print(f"{ability}!")
    else:
        turn = "off"
