import os
def highest_bidder(record):
    highest_bid = 0
    winner = ""
    for bidder in record:
        if record[bidder] > highest_bid:
            highest_bid = record[bidder]
            winner = bidder
    print(f"The winner is {winner} with a bid of ₹{highest_bid}.")

logo = '''
                         ___________
                         \\         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
'''
print(logo)
print("~~~Welcome to the Secret Auction~~~") # using dictionaries
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Enter your name: ")
    price = float(input("Enter bid amount: ₹"))
    bids[name] = price
    choice = input("Are there any other bidders? type \"yes\" or \"no\": ").lower()
    if choice == "no":
        bidding_finished = True
        highest_bidder(bids)
    elif choice == "yes":
        os.system('cls')
    else:
        print("Please enter a valid choice!!!\nEnding Auction")
        highest_bidder(bids)
        bidding_finished = True