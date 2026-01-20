from random import randint
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5
def check_answer(guess, answer,turns):
    """
    Checks answer against guess and returns the number of turns remaining
    """
    if guess > answer:
        print("Too High")
        return turns - 1
    elif guess < answer:
        print("Too Low")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")

def set_difficulty():
    if input("Choose a difficulty. Type \'easy\' or \'hard\':\n>>> ").lower() == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

logo = """
                                                                                                          
   ____                                              ___      ___                         ___                       
  6MMMMb/                                            `MM\\     `M'                          MM                       
 8P    YM                                             MMM\\     M                           MM                       
6M      Y ___   ___   ____     ____     ____          M\\MM\\    M ___   ___ ___  __    __   MM____     ____  ___  __ 
MM        `MM    MM  6MMMMb   6MMMMb\\  6MMMMb\\        M \\MM\\   M `MM    MM `MM 6MMb  6MMb  MMMMMMb   6MMMMb `MM 6MM 
MM         MM    MM 6M'  `Mb MM'    ` MM'    `        M  \\MM\\  M  MM    MM  MM69 `MM69 `Mb MM'  `Mb 6M'  `Mb MM69 " 
MM     ___ MM    MM MM    MM YM.      YM.             M   \\MM\\ M  MM    MM  MM'   MM'   MM MM    MM MM    MM MM'    
MM     `M' MM    MM MMMMMMMM  YMMMMb   YMMMMb         M    \\MM\\M  MM    MM  MM    MM    MM MM    MM MMMMMMMM MM     
YM      M  MM    MM MM            `Mb      `Mb        M     \\MMM  MM    MM  MM    MM    MM MM    MM MM       MM     
 8b    d9  YM.   MM YM    d9 L    ,MM L    ,MM        M      \\MM  YM.   MM  MM    MM    MM MM.  ,M9 YM    d9 MM     
  YMMMM9    YMMM9MM_ YMMMM9  MYMMMM9  MYMMMM9        _M_      \\M   YMMM9MM__MM_  _MM_  _MM_MYMMMM9   YMMMM9 _MM_    
                                                                                                                    
                                                                                                                    
                                                                                                                    """
print(logo)
print("Welcome to Number Guessing Game!!")

def game():
    print("I\'m thinking of a number between 1 and 100.")
    # Choosing a number between 1 and 100
    answer = randint(1,100)
    turns = set_difficulty()
    guess = ""
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess:\n>>> "))
        turns = check_answer(guess, answer,turns)
        if turns == 0:
            print("You have run out of guesses, You LOSE")
            print(f"The answer was {answer}")
            return
        elif guess!=answer:
            print("Guess again")

game()