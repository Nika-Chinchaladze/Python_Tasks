import random as rd

letters = []
for i in range(65,91):
  letters.append(chr(i))

for j in range(97,123):
  letters.append(chr(j))

numbers = []
for k in range(0,10):
  numbers.append(str(k))

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


print("Welcome to the PyPassword Generator!")
first = int(input("How many letters would you like in your password? \n"))
second = int(input("How many symbols would you like? \n"))
third = int(input("How many numbers would you like? \n"))

result = []
for i in range(first):
  result.append(rd.choice(letters))
  
for i in range(second):
  result.append(rd.choice(symbols))
  
for i in range(third):
  result.append(rd.choice(numbers))
  
# for second way of solution:
result_2 = result.copy()

# generate first password:
length = len(result)
password_1 = ''
for i in range(length):
  control = rd.choice(result)
  password_1 += control
  result.remove(control)

# generate second password:
rd.shuffle(result_2)
password_2 = ''
for i in result_2:
  password_2 += i

# print our possible passwords:
print(f"Here are your Passwords:\n{password_1} \n{password_2}")



