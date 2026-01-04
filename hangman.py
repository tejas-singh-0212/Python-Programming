import random
hangman_logo = '''
 .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |
| | |_   ||   _| | || |     /  \\     | || ||_   \\|_   _| | || |  .' ___  |   | || ||_   \\  /   _|| || |     /  \\     | || ||_   \\|_   _| | |
| |   | |__| |   | || |    / /\\ \\    | || |  |   \\ | |   | || | / .'   \\_|   | || |  |   \\/   |  | || |    / /\\ \\    | || |  |   \\ | |   | |
| |   |  __  |   | || |   / ____ \\   | || |  | |\\ \\| |   | || | | |    ____  | || |  | |\\  /| |  | || |   / ____ \\   | || |  | |\\ \\| |   | |
| |  _| |  | |_  | || | _/ /    \\ \\_ | || | _| |_\\   |_  | || | \\ `.___]  _| | || | _| |_\\/_| |_ | || | _/ /    \\ \\_ | || | _| |_\\   |_  | |
| | |____||____| | || ||____|  |____|| || ||_____|\\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\\____| | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''
win = '''
 __     ______  _    _  __          ______  _   _ _ 
 \\ \\   / / __ \\| |  | | \\ \\        / / __ \\| \\ | | |
  \\ \\_/ / |  | | |  | |  \\ \\  /\\  / / |  | |  \\| | |
   \\   /| |  | | |  | |   \\ \\/  \\/ /| |  | | . ` | |
    | | | |__| | |__| |    \\  /\\  / | |__| | |\\  |_|
    |_|  \\____/ \\____/      \\/  \\/   \\____/|_| \\_(_)
'''
lose = '''
 __     ______  _    _   _      ____   _____ ______ _ 
 \\ \\   / / __ \\| |  | | | |    / __ \\ / ____|  ____| |
  \\ \\_/ / |  | | |  | | | |   | |  | | (___ | |__  | |
   \\   /| |  | | |  | | | |   | |  | |\\___ \\|  __| | |
    | | | |__| | |__| | | |___| |__| |____) | |____|_|
    |_|  \\____/ \\____/  |______\\____/|_____/|______(_)
'''
stages = [''' 
    +---+
    |   |
    0   |
   /|\\  |
   / \\  |
        |
===========
''',
''' 
    +---+
    |   |
    0   |
   /|\\  |
   /    |
        |
===========
''',
''' 
    +---+
    |   |
    0   |
   /|\\  |
        |
        |
===========
''',
''' 
    +---+
    |   |
    0   |
   /|   |
        |
        |
===========
''',
''' 
    +---+
    |   |
    0   |
    |   |
        |
        |
===========
''',
''' 
    +---+
    |   |
    0   |
        |
        |
        |
===========
''',
''' 
    +---+
    |   |
        |
        |
        |
        |
===========
'''
]
print(hangman_logo)
word_list = [
    "apple", "banana", "orange", "grape", "mango", "peach", "cherry", "lemon", "melon", "berry",
    "tiger", "lion", "zebra", "giraffe", "monkey", "rabbit", "dolphin", "whale", "eagle", "falcon",
    "laptop", "keyboard", "mouse", "screen", "printer", "camera", "speaker", "router", "charger", "battery",
    "python", "java", "ruby", "swift", "kotlin", "script", "function", "variable", "loop", "object",
    "river", "mountain", "forest", "desert", "island", "valley", "ocean", "beach", "canyon", "glacier",
    "football", "cricket", "tennis", "hockey", "boxing", "racing", "skating", "surfing", "cycling", "archery",
    "doctor", "teacher", "engineer", "artist", "writer", "singer", "dancer", "farmer", "pilot", "baker",
    "window", "mirror", "pillow", "blanket", "carpet", "curtain", "ladder", "hammer", "bucket", "bottle",
    "rocket", "planet", "galaxy", "comet", "asteroid", "satellite", "orbit", "eclipse", "nebula", "meteor",
    "puzzle", "mystery", "fortune", "adventure", "fantasy", "legend", "hero", "villain", "kingdom", "treasure"
]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
blank_word = ["_" for i in range(word_length)]
end_of_game = False
lives = 6
while not end_of_game:
    guessed_letter = input("Guess a letter: ").lower()
    for i in range(word_length):
        if guessed_letter == chosen_word[i]:
            blank_word[i]=guessed_letter
            
    if guessed_letter not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(lose)

    print(f"{' '.join(blank_word)}")
    if "_" not in blank_word:
        end_of_game = True
        print(win)
    
    print(stages[lives])