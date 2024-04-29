#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

generated_chars = []

new_password = ""

for char in range(0, nr_letters):
    generated_chars.append(letters[random.randint(0, len(letters) - 1)])

for char in range(0, nr_symbols):
    generated_chars.append(symbols[random.randint(0, len(symbols) - 1)])

for char in range(0, nr_numbers):
    generated_chars.append(numbers[random.randint(0, len(numbers) - 1)])


while len(generated_chars) > 0:
    ran_index = random.randint(0, len(generated_chars) - 1)
    new_password = new_password + generated_chars[ran_index]
    generated_chars.pop(ran_index)

print(new_password)