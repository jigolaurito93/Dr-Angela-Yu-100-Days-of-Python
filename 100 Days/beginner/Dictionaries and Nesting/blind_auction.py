#  Start
# Show logo
# Ask name for input
# Ask for bid price
# Add name and bid into a dictionary as key and value
# Ask if there are any other users who want to bid
    # if yes: Loop through
    # If no: Find the highest bid in the dictionary and declare them as winner
from art_auction import logo

print(logo)
print(f"Welcome to the secret auction program.")

run_bidding = True

bidders = {}

def add_bidder(name, price):
    bidders[name] = price

while run_bidding:
    name = input("What is your name? ").capitalize()
    price = int(input("What is your bid? $"))
    add_bidder(name, price)
    more_bidder = input(f"Are there any other bidders? Type y/n? ")
    if more_bidder == 'n':
        run_bidding = False

highest_bid = 0
highest_bidder = ''
for key, value in bidders.items():
    if value > highest_bid:
        highest_bid = value
        highest_bidder = key
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}!")

