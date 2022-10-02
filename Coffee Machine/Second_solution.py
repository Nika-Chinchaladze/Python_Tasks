from info import MENU, resources


def stock_amount(ordered):
    for item in ordered["ingredients"].keys():
        if ordered["ingredients"][item] > resources[item]:
            print(f"Sorry, there is not enough {item}!")
            return False
    return True


def deal_coins():
    print("Print insert coins!")
    paid = int(input("How many Quarters? ")) * 0.25
    paid += int(input("How many Dimes? ")) * 0.1
    paid += int(input("How many Nickles? ")) * 0.05
    paid += int(input("How many Pennies? ")) * 0.01
    return paid


def good_transaction(received_money, real_cost):
    if received_money >= real_cost:
        refund = round(received_money - real_cost, 2)
        if refund > 0:
            print(f"Here is ${refund} in change!")
        resources["money"] += real_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded!")
        return False


def make_order(name, composition):
    for item in composition["ingredients"].keys():
        resources[item] -= composition["ingredients"][item]
    print(f"Here is you {name}. Enjoy!")


turn_on = True
while turn_on:
    guess = input("What would you like? (espresso/latte/cappuccino): ")
    if guess == "off":
        turn_on = False
    elif guess == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${resources['money']}")
    elif guess in ("espresso", "latte", "cappuccino"):
        glass = MENU[guess]
        if stock_amount(glass):
            payment = deal_coins()
            if good_transaction(payment, glass["cost"]):
                make_order(guess, glass)
