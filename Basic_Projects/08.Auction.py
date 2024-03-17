import os

def find_highest_bidder(bid_record):
    highestbid = 0
    winner = ""
    for bidder in bid_record:
        bid_amount = int(bid_record[bidder])
        if bid_amount > highestbid:
            highestbid = bid_amount
            winner = bidder
    print(f"Winner is {winner}")

def clear():
    os.system('cls')
bids = {}
bidding_finished = False
while not bidding_finished:
    name = input("Enter your name")

    price = input("Whats bid")
    
    bids[name] = price
    should_continue = input("other bidders?")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue=="yes":
        clear()
