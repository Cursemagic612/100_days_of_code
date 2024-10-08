import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letter_req = 0
symbol_req = 0
number_req = 0
gen_password = []

for letter_req in range(0,nr_letters):
    temp_letter = random.choice(letters)
    gen_password.extend(temp_letter)

for symbol_req in range(0,nr_symbols):
    temp_symbol = random.choice(symbols)
    gen_password.extend(temp_symbol)

for number_req in range(0,nr_numbers):
    temp_number = random.choice(numbers)
    gen_password.extend(temp_number)

random.shuffle(gen_password)

print(''.join(str(i) for i in gen_password))
