import random

print("Welcome to the PyPassword Generator!")
nu_letters = int(input("How many letters would you like in your password?\n"))
nu_symbols = int(input("How many symbols would you like?\n"))
nu_numbers = int(input("How many numbers would you like?\n"))

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

symbols = ["~", "`", "!", "@", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", ":", ";", "<", ",", ">", ".", "?"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

n = nu_letters
passwd_letters = []
for i in range(n):
  passwd_letters.append(random.choice(letters))
p_letters = "".join(passwd_letters)


n = nu_symbols
passwd_symbols = []
for i in range(n):
  passwd_symbols.append(random.choice(symbols))
p_symbols = "".join(passwd_symbols)

n = nu_numbers
passwd_numbers = []
for i in range(n):
  passwd_numbers.append(random.choice(numbers))
p_numbers = "".join(passwd_numbers)


final_passwd_lst = []
final_passwd_lst.append(p_letters) 
final_passwd_lst.append(p_symbols)
final_passwd_lst.append(p_numbers)


random.shuffle(final_passwd_lst)

final_passwd = "".join(final_passwd_lst)

print("Here is your final password: " + final_passwd)