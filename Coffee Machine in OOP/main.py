from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine = True
while machine:
    guess = input(f"What would you like? {menu.get_items()}: ").lower()
    if guess == "off":
        machine = False
    elif guess == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        if menu.find_drink(guess):
            drink = menu.find_drink(guess)
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
