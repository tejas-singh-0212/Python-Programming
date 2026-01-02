rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
def print_choice(a):
    if a == "rock":
        print(rock)
    elif a == "paper":
        print(paper)
    elif a == "scissor":
        print(scissor)

import random
print("Welcome to Rock-Paper-Scissors")
user_choice = input("What do you choose? (Rock / Paper / Scissor): ").lower()
comp_choice = random.choice(["rock","paper","scissor"])

if user_choice == comp_choice:
    print(f"You chose: {user_choice}")
    print_choice(user_choice)
    print(f"Computer chose: {comp_choice}")
    print_choice(comp_choice)
    print("Its a tie")
elif ((user_choice == "rock" and comp_choice == "scissor") or (user_choice == "paper" and comp_choice == "rock") or (user_choice == "scissor" and comp_choice == "paper")):
    print(f"You chose: {user_choice}")
    print_choice(user_choice)
    print(f"Computer chose: {comp_choice}")
    print_choice(comp_choice)
    print("Congratulation!!\nYou WON!!!")
elif ((comp_choice == "rock" and user_choice == "scissor") or (comp_choice == "paper" and user_choice == "rock") or (comp_choice == "scissor" and user_choice == "paper")):
    print(f"You chose: {user_choice}")
    print_choice(user_choice)
    print(f"Computer chose: {comp_choice}")
    print_choice(comp_choice)
    print("Computer won")
else:
    print("Invalid choice!!\nYou LOSE!!")