from random import choice
import os
logo = '''                                                                                                                                                            
                                                                                          
 ▄▄▄▄▄▄    ▄▄▄▄                          ▄▄           ▄▄▄▄▄                      ▄▄       
 ██▀▀▀▀██  ▀▀██                          ██           ▀▀▀██                      ██       
 ██    ██    ██       ▄█████▄   ▄█████▄  ██ ▄██▀         ██   ▄█████▄   ▄█████▄  ██ ▄██▀  
 ███████     ██       ▀ ▄▄▄██  ██▀    ▀  ██▄██           ██   ▀ ▄▄▄██  ██▀    ▀  ██▄██    
 ██    ██    ██      ▄██▀▀▀██  ██        ██▀██▄          ██  ▄██▀▀▀██  ██        ██▀██▄   
 ██▄▄▄▄██    ██▄▄▄   ██▄▄▄███  ▀██▄▄▄▄█  ██  ▀█▄   █▄▄▄▄▄██  ██▄▄▄███  ▀██▄▄▄▄█  ██  ▀█▄  
 ▀▀▀▀▀▀▀      ▀▀▀▀    ▀▀▀▀ ▀▀    ▀▀▀▀▀   ▀▀   ▀▀▀   ▀▀▀▀▀     ▀▀▀▀ ▀▀    ▀▀▀▀▀   ▀▀   ▀▀▀ 

'''
# currently we aren't dealing with probabilty stuff and removing cards from deck, we're gonna assume the deck to be infinite
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]    # 11 is the Ace

def deal_card(card_list = cards):
    """
    Returns a random card from deck
    """
    return choice(card_list)

def calculate_score(score_list):
    """
    Takes a list of cards and returns the score calculated
    """
    if sum(score_list) == 2 and len(score_list) == 2:
        return 0

    if 11 in score_list and sum(score_list) > 21:
        score_list.remove(11)
        score_list.append(1)

    return sum(score_list)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Its a Draw"
    elif computer_score == 0:
        return "You LOSE !!\nOpponent has Blackjack"
    elif user_score == 0:
        return "You WIN with a Blackjack"
    elif user_score > 21:
        return "You went over\nYou LOSE"
    elif computer_score > 21:
        return "Opponent went over\nYou WIN"
    elif user_score > computer_score:
        return "You WIN"
    else:
        return "You LOSE"

def play_game():
    user_cards = [deal_card() for _ in range(2)]
    computer_cards = [deal_card() for _ in range(2)]
    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer\'s first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            if  input("Type \'y\' to get another card, type \'n\' to pass: ").lower() == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand is {user_cards}, final score: {user_score}")
    print(f"Computer\'s final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type \'y\' or \'n\': ").lower() == "y":
    os.system('cls')
    print(logo)
    play_game()