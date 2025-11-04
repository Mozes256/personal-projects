import os
from art import logo

print(logo)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


bids = {}
bidding_finished = False

highest_bid = 0
winner = ""

while not bidding_finished:
    name = input("What is your name?: ").lower()
    bid_price = int(input("What is your bid?: $"))
    bids[name] = bid_price

    new_bider = input("Are there any other bidders? (yes/no): ").lower()
    if new_bider == "no":
        bidding_finished = True
        clear_screen()
    else:
        clear_screen()

for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
        highest_bid = bid_amount
        winner = bidder

print(f"\nThe winner is {winner} with a bid of ${bids[winner]}")
