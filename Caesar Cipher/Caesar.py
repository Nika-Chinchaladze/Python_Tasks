from art import logo

print(logo)
alphabet = []
for i in range(97,123):
  alphabet.append(chr(i))
alphabet.extend(alphabet)

def Caesar(message, number, direct):
  if number > 26:
    number = number % 26
  answer = ''
  if direct == "decode":
    number *= -1
  for i in message:
    if i in alphabet:
      place = alphabet.index(i)
      new_place = place + number
      answer += alphabet[new_place]
    else:
      answer += i
  print(f"The {direct}d text is: {answer}")

will = "yes"
while will != "no":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
  text = input("Type your message: \n").lower()
  shift = int(input("Type the shift number! \n"))
  
  Caesar(text, shift, direction)
  
  will = input("if you want to try again - type 'yes', otherwise type 'no'! \n").lower()

if will == "no":
  print("GoodBye")