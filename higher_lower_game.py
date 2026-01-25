import os
from random import choice

logo = """ _   _ _       _                      _                            
| | | (_)     | |                    | |                           
| |_| |_  __ _| |__   ___ _ __ ______| |     _____      _____ _ __ 
|  _  | |/ _` | '_ \\ / _ \\ '__|______| |    / _ \\ \\ /\\ / / _ \\ '__|
| | | | | (_| | | | |  __/ |         | |___| (_) \\ V  V /  __/ |   
\\_| |_/_|\\__, |_| |_|\\___|_|         \\_____/\\___/ \\_/\\_/ \\___|_|   
          __/ |                                                    
         |___/                                                     
"""
print(logo)
data_set = [
    {
        'name': 'Instagram',
        'follower_count': 698000000,
        'description': 'Social media platform',
        'country': 'United States'
    },
    {
        'name': 'Cristiano Ronaldo',
        'follower_count': 670000000,
        'description': 'Footballer',
        'country': 'Portugal'
    },
    {
        'name': 'Lionel Messi',
        'follower_count': 511000000,
        'description': 'Footballer',
        'country': 'Argentina'
    },
    {
        'name': 'Selena Gomez',
        'follower_count': 416000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kylie Jenner',
        'follower_count': 391000000,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Dwayne Johnson',
        'follower_count': 390000000,
        'description': 'Actor and professional wrestler',
        'country': 'United States'
    },
    {
        'name': 'Ariana Grande',
        'follower_count': 372000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Kim Kardashian',
        'follower_count': 354000000,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Beyoncé',
        'follower_count': 308000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Khloé Kardashian',
        'follower_count': 300000000,
        'description': 'Reality TV star and businesswoman',
        'country': 'United States'
    },
    {
        'name': 'Nike',
        'follower_count': 298000000,
        'description': 'Sportswear multinational',
        'country': 'United States'
    },
    {
        'name': 'Justin Bieber',
        'follower_count': 292000000,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Kendall Jenner',
        'follower_count': 285000000,
        'description': 'Model and Reality TV star',
        'country': 'United States'
    },
    {
        'name': 'Taylor Swift',
        'follower_count': 281000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'National Geographic',
        'follower_count': 275000000,
        'description': 'Magazine and media brand',
        'country': 'United States'
    },
    {
        'name': 'Virat Kohli',
        'follower_count': 274000000,
        'description': 'Cricketer',
        'country': 'India'
    },
    {
        'name': 'Jennifer Lopez',
        'follower_count': 246000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Neymar',
        'follower_count': 231000000,
        'description': 'Footballer',
        'country': 'Brazil'
    },
    {
        'name': 'Kourtney Kardashian',
        'follower_count': 216000000,
        'description': 'Reality TV star',
        'country': 'United States'
    },
    {
        'name': 'Miley Cyrus',
        'follower_count': 211000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Katy Perry',
        'follower_count': 201000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Real Madrid CF',
        'follower_count': 180000000,
        'description': 'Football Club',
        'country': 'Spain'
    },
    {
        'name': 'Kevin Hart',
        'follower_count': 176000000,
        'description': 'Comedian and actor',
        'country': 'United States'
    },
    {
        'name': 'Zendaya',
        'follower_count': 176000000,
        'description': 'Actress and singer',
        'country': 'United States'
    },
    {
        'name': 'Cardi B',
        'follower_count': 164000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'LeBron James',
        'follower_count': 157000000,
        'description': 'Basketball player',
        'country': 'United States'
    },
    {
        'name': 'Demi Lovato',
        'follower_count': 152000000,
        'description': 'Musician and actress',
        'country': 'United States'
    },
    {
        'name': 'Rihanna',
        'follower_count': 149000000,
        'description': 'Musician and businesswoman',
        'country': 'Barbados'
    },
    {
        'name': 'FC Barcelona',
        'follower_count': 145000000,
        'description': 'Football Club',
        'country': 'Spain'
    },
    {
        'name': 'Chris Brown',
        'follower_count': 143000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Drake',
        'follower_count': 142000000,
        'description': 'Musician',
        'country': 'Canada'
    },
    {
        'name': 'Ellen DeGeneres',
        'follower_count': 134000000,
        'description': 'Comedian and TV host',
        'country': 'United States'
    },
    {
        'name': 'Kylian Mbappé',
        'follower_count': 129000000,
        'description': 'Footballer',
        'country': 'France'
    },
    {
        'name': 'Billie Eilish',
        'follower_count': 124000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'UEFA Champions League',
        'follower_count': 121000000,
        'description': 'Club football competition',
        'country': 'Europe'
    },
    {
        'name': 'Lisa',
        'follower_count': 106000000,
        'description': 'Musician',
        'country': 'Thailand'
    },
    {
        'name': 'Gal Gadot',
        'follower_count': 106000000,
        'description': 'Actress',
        'country': 'Israel'
    },
    {
        'name': 'Vin Diesel',
        'follower_count': 104000000,
        'description': 'Actor',
        'country': 'United States'
    },
    {
        'name': 'Narendra Modi',
        'follower_count': 99000000,
        'description': 'Prime Minister',
        'country': 'India'
    },
    {
        'name': 'NASA',
        'follower_count': 97000000,
        'description': 'Space agency',
        'country': 'United States'
    },
    {
        'name': 'Shakira',
        'follower_count': 95000000,
        'description': 'Musician',
        'country': 'Colombia'
    },
    {
        'name': 'Shraddha Kapoor',
        'follower_count': 94000000,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Priyanka Chopra',
        'follower_count': 93000000,
        'description': 'Actress and musician',
        'country': 'India'
    },
    {
        'name': 'NBA',
        'follower_count': 90000000,
        'description': 'Basketball league',
        'country': 'United States'
    },
    {
        'name': 'Snoop Dogg',
        'follower_count': 88000000,
        'description': 'Musician',
        'country': 'United States'
    },
    {
        'name': 'Dua Lipa',
        'follower_count': 88000000,
        'description': 'Musician',
        'country': 'United Kingdom'
    },
    {
        'name': 'David Beckham',
        'follower_count': 88000000,
        'description': 'Footballer',
        'country': 'United Kingdom'
    },
    {
        'name': 'Jennie',
        'follower_count': 88000000,
        'description': 'Musician',
        'country': 'South Korea'
    },
    {
        'name': 'Alia Bhatt',
        'follower_count': 86000000,
        'description': 'Actress',
        'country': 'India'
    },
    {
        'name': 'Rosé',
        'follower_count': 84000000,
        'description': 'Musician',
        'country': 'New Zealand'
    }
]

vs = """
____   ____         
\\   \\ /   /_____    
 \\   Y   /  ___/    
  \\     /\\___ \\     
   \\___//____  > 
             \\/ 
"""

# format the account data into printable format
def format_data(acc):
    """
    Format the account data into printable format
    """
    acc_name = acc['name']
    acc_des = acc['description']
    acc_country = acc['country']
    return f"{acc_name}, a {acc_des}, from {acc_country}"

def check_answer(guess, a_followers, b_followers):
    """
    Take the user guess and follower counts and returns if they got it right
    """
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
# generate a random account from game data
score = 0
should_continue = True
acc_B = choice(data_set)

# make the game repeatable
while should_continue:

    # making the current B, the next A, if user guesses correct
    acc_A = acc_B
    acc_B = choice(data_set)
    while acc_A == acc_B:
        acc_B = choice(data_set)

    print(f"Compare A: {format_data(acc_A)}")
    print(vs)
    print(f"Against B: {format_data(acc_B)}")
    # taking user guess input
    guess = input("Who has more followers? Type \'A\' or \'B\': ").lower()
    # get follower count of each account
    a_follower_count = acc_A['follower_count']
    b_follower_count = acc_B['follower_count']
    # use if statement to check if user if correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # give user feedback on their guess
    os.system('cls')
    print(logo)
    if is_correct:
    # score keeping
        score += 1
        print(f"You\'re right\nCurrent score: {score}")
    else:
        should_continue = False
        print(f"Sorry, that\'s wrong.\nFinal score: {score}")


    # clear screen after each round