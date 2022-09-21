from replit import clear
from logo import logo

def add(a, b):
  return a + b

def sub(a, b):
  return a - b

def mul(a, b):
  return a * b

def div(a, b):
  return a / b

basic = {'+':add, '-':sub, '*':mul, '/':div}


def Calculation():
  print(logo)
  first = float(input("What's the first number? "))
  for key in basic.keys():
    print(key)

  cont = "yes"
  while cont == "yes":
    operation = input("Pick an operation! ")
    second = float(input("What's the second number? "))
    function = basic[f"{operation}"]
    answer = function(first, second)
    print(f"{first} {operation} {second} = {answer}")
    choise = input("Type 'y' to continue with previous number or type 'n' to start with blank page! \n")
  
    if choise == "y":
      for key in basic.keys():
        print(key)
      first = answer
    else:
      cont == "no"
      clear()
      Calculation()

Calculation()