import art

print(art.logo)

should_continue = True

bidders = {}

def print_highest_bid_amount():
    max_amount = 0
    bidder_name = ""
    for name in bidders:
        bid_amount = bidders[name]
        if bid_amount > max_amount:
            max_amount = bid_amount
            bidder_name = name

    print(f"The Winner is {bidder_name} with a bid of {max_amount}")


while should_continue:
    name = input("What is your name?")
    bid_amount = int(input("What is your bid: $"))
    choice = input('''Are there any bidders? Type 'yes' or 'no'.\n''').lower()
    bidders[name] = bid_amount
    if choice != "yes":
        should_continue = False
    else:
        print("\n" * 20)

print_highest_bid_amount()
