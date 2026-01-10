import string
import random
letter = list(string.ascii_lowercase)
logo = '''
$$$$$$$$\\                                     $$\\                             $$$$$$$\\                                      $$\\                     
$$  _____|                                    $$ |                            $$  __$$\\                                     $$ |                    
$$ |      $$$$$$$\\   $$$$$$$\\  $$$$$$\\   $$$$$$$ | $$$$$$\\   $$$$$$\\          $$ |  $$ | $$$$$$\\   $$$$$$$\\  $$$$$$\\   $$$$$$$ | $$$$$$\\   $$$$$$\\  
$$$$$\\    $$  __$$\\ $$  _____|$$  __$$\\ $$  __$$ |$$  __$$\\ $$  __$$\\ $$$$$$\\ $$ |  $$ |$$  __$$\\ $$  _____|$$  __$$\\ $$  __$$ |$$  __$$\\ $$  __$$\\ 
$$  __|   $$ |  $$ |$$ /      $$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \\__|\\______|$$ |  $$ |$$$$$$$$ |$$ /      $$ /  $$ |$$ /  $$ |$$$$$$$$ |$$ |  \\__|
$$ |      $$ |  $$ |$$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |              $$ |  $$ |$$   ____|$$ |      $$ |  $$ |$$ |  $$ |$$   ____|$$ |      
$$$$$$$$\\ $$ |  $$ |\\$$$$$$$\\ \\$$$$$$  |\\$$$$$$$ |\\$$$$$$$\\ $$ |              $$$$$$$  |\\$$$$$$$\\ \\$$$$$$$\\ \\$$$$$$  |\\$$$$$$$ |\\$$$$$$$\\ $$ |      
\\________|\\__|  \\__| \\_______| \\______/  \\_______| \\_______|\\__|              \\_______/  \\_______| \\_______| \\______/  \\_______| \\_______|\\__| 
'''
def encode(list_message):
    '''
    encoding a message on the basis of following rules:
    1. if the word has at least 3 characters, then move the first character to the last and then add three random characters at the start and end
    2. if the word has less than 3 characters, them reverse the word
    '''
    modified_message = []
    for item in list_message:
        if len(item) >= 3:
            first_char = item[0]
            item = item[1:] + first_char
            for i in range(3):
                item = random.choice(letter) + item
            for i in range(3):
                item += random.choice(letter)
        else:
            item = item[::-1]
        modified_message.append(item)
    return " ".join(modified_message)

def decode(list_message):
    '''
    decoding message on the basis of the reverse of the rules of encoding
    '''
    modified_message = []
    for item in list_message:
        if len(item) >= 9:
            item = item[3:-3]
            first_char = item[-1]
            print(item)
            item = first_char + item[:-1]
        else:
            item = item[::-1]
        modified_message.append(item)
    return " ".join(modified_message)

print(logo)
should_end = False
while not should_end:
    message = input("Enter message:\n>>> ")
    message_list = message.split(" ")
    choice = input("Type \"encode\" to start encoding, \"decode\" to start decoding: ").lower()
    if choice == "encode":
        print(f"\nEncoded message:\n>>> {encode(message_list)}")
    elif choice == "decode":
        print(f"\nDecoded message:\n>>> {decode(message_list)}")
    else:
        print("\nInvalid Input!!!")
        print("\nExiting Encoder-Decoder")
        break
    choice = input("\nWould you like to continue? type \"yes\" to continue and anything else to exit:\n>>> ").lower()
    if choice == "yes":
        should_end = False
    else:
        print("\nExiting Encoder-Decoder")
        should_end = True