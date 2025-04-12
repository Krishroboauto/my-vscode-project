from hammer import logo
from os import system

print(logo)
print("Welcome to the secret auction Program")

bidders = {}

is_bidder = True
highest_bid = 0
winner = ""

while is_bidder == True:
    name = input("What is your name?")
    bid  = float(input("what is your bid?:$"))
    next_bid = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    bidders[name] = bid
    if next_bid == 'yes':
        system("clear")
    elif next_bid == 'no':
        system("clear")
        for name,bid in bidders.items():
            if bid > highest_bid:
                highest_bid = bid
                winner = name

        print(f"The winner is {winner} with a bid of {highest_bid}$")
        is_bidder = False

print(bidders)


