from bidding_art import logo
print(logo)
bidding_dic = {}
bidding_finished = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winnder is {winner} with a bid of ${highest_bid}")
        
while not bidding_finished:
    name = input("What is your name? ")
    bidding_price = int(input("What is your bidding price? $"))
    bidding_dic[name] = bidding_price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no' .")
    if should_continue == "no": 
        bidding_finished = True
    elif should_continue == "yes": 
        bidding_finished = False
        
 




