import random

print("Welcome to the PyPassword Generator!")
nu_letters = int(input("How many letters would you like in your password?\n"))
nu_symbols = int(input("How many symbols would you like?\n"))
nu_numbers = int(input("How many numbers would you like?\n"))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = ["!", "$", "%", "&", "*", "(", ")", "_", "-", ":", ";", "<", ",", ">", ".", "?"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

n = nu_letters
rnd_letters = []
for i in range(n):
  rnd_letters.append(random.choice(letters))

n = nu_symbols
rnd_symbols = []
for i in range(n):
  rnd_symbols.append(random.choice(symbols))

n = nu_numbers
rnd_numbers = []
for i in range(n):
  rnd_numbers.append(random.choice(numbers))

final_rnd = rnd_letters + rnd_symbols + rnd_numbers

random.shuffle(final_rnd)

final_password = "".join(final_rnd)

print("Here is your final password: " + final_password)