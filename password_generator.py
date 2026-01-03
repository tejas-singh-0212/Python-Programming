import random
import string
letters = list(string.ascii_letters)
symbols = ['!','@','#','$','%','^','&','*','(',')',';',':','<','>','/','\\','|','[',']','{','}','?','=','+','-','_']
numbers = [str(i) for i in range(10)]
print("Welcome to PyPassword Generator!!")
number_letters = int(input("How many letters would you like in your password: "))
number_numbers = int(input("How many numbers would you like in your password: "))
number_symbols = int(input("How many symbols would you like in your password: "))

# Generator starts
password_list = []
# fetching random characters, symbols, number
for char in range(number_letters):
    password_list.append(random.choice(letters))
for n in range(number_numbers):
    password_list.append(random.choice(numbers))
for sym in range(number_symbols):
    password_list.append(random.choice(symbols))
# shuffling the order of password
random.shuffle(password_list)
# joining it as a string
password = "".join(password_list)
print(f"Your password is: {password}")