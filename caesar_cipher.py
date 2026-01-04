import string
logo= '''
  /$$$$$$   /$$$$$$  /$$$$$$$$  /$$$$$$   /$$$$$$  /$$$$$$$         /$$$$$$  /$$$$$$ /$$$$$$$  /$$   /$$ /$$$$$$$$ /$$$$$$$ 
 /$$__  $$ /$$__  $$| $$_____/ /$$__  $$ /$$__  $$| $$__  $$       /$$__  $$|_  $$_/| $$__  $$| $$  | $$| $$_____/| $$__  $$
| $$  \\__/| $$  \\ $$| $$      | $$  \\__/| $$  \\ $$| $$  \\ $$      | $$  \\__/  | $$  | $$  \\ $$| $$  | $$| $$      | $$  \\ $$
| $$      | $$$$$$$$| $$$$$   |  $$$$$$ | $$$$$$$$| $$$$$$$/      | $$        | $$  | $$$$$$$/| $$$$$$$$| $$$$$   | $$$$$$$/
| $$      | $$__  $$| $$__/    \\____  $$| $$__  $$| $$__  $$      | $$        | $$  | $$____/ | $$__  $$| $$__/   | $$__  $$
| $$    $$| $$  | $$| $$       /$$  \\ $$| $$  | $$| $$  \\ $$      | $$    $$  | $$  | $$      | $$  | $$| $$      | $$  \\ $$
|  $$$$$$/| $$  | $$| $$$$$$$$|  $$$$$$/| $$  | $$| $$  | $$      |  $$$$$$/ /$$$$$$| $$      | $$  | $$| $$$$$$$$| $$  | $$
 \\______/ |__/  |__/|________/ \\______/ |__/  |__/|__/  |__/       \\______/ |______/|__/      |__/  |__/|________/|__/  |__/
'''
print(logo)
def caesar(text, shift_amount, direction):
    modified_text =""
    if direction == "decode":
        shift_amount *= -1
    for char in text:
        if char in letters:
            index = letters.index(char)
            modified_text += letters[index + shift_amount]
        else:
            modified_text += char
    print(f"The {direction}d text is: {modified_text}")

letters = list(string.ascii_lowercase)
letters.extend(list(string.ascii_lowercase))

choice = "yes"
while choice=="yes":
    task = input("Type \"encode\" to encrypt, type \"decode\" to decrypt:\n>>> ").lower()
    if(task == "encode" or task == "decode"):
        message = input("Type your message:\n>>> ").lower()
        shift = int(input("Enter shift number:\n>>> ")) % 26
        caesar(text=message, shift_amount=shift, direction=task)
    else:
        print("Enter a Valid choice")
    choice = input("Would you like to continue type \"yes\" or \"no\":\n>>> ").lower()

print("Exiting Program")