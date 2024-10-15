import art

print(art.logo)

other_bidder = True
auction_info = {}

while other_bidder:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    auction_info[name] = bid
    bidder = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if bidder == "no":
        other_bidder = False
    else:
        print("\n" * 20)

highest_bid = 0
highest_bidder = ""

for user in auction_info:
    if auction_info[user] > highest_bid:
        highest_bid = auction_info[user]
        highest_bidder = user

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")
