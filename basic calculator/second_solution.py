from replit import clear
from logo import logo

def Calculate(first_number, second_number, operation):
    if operation == "+":
        return first_number + second_number
    elif operation == "-":
        return first_number - second_number
    elif operation == "*":
        return first_number * second_number
    elif operation == "/":
        return first_number / second_number


operations = ['+', '-', '*', '/']

def magic():
    print(logo)
    first = float(input("Enter first number: "))
    for symbol in operations:
        print(symbol)
    
    same = True
    while same:
        oper = input("Choose operation: ")
        second = float(input("Enter second number: "))
        answer = Calculate(first, second, oper)
        print(f"Answer: {first} {oper} {second} = {answer}")
        choice = input("Continue from old or new page? old / new \n")
        if choice == "old":
            first = answer
            for symbol in operations:
                print(symbol)
        else:
            same = False
            clear()
            magic()

magic()