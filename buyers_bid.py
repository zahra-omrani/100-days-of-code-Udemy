from IPython.display import clear_output
offer_dic = {}


def find_highest_bidder(offer_dic):
    highest_bid = 0
    winner = ""

    for name in offer_dic:  
        if offer_dic[name] > highest_bid:
            highest_bid = offer_dic[name]
            winner = name
    
    print(f"The winner is {winner} with a bid of {highest_bid}")


new_user = "Yes"


while new_user.lower() == "yes":
    clear_output(wait=True)
    
    
    name = input("What is your name: ")
    bid_price = int(input("What is your bid price: "))
    offer_dic[name] = bid_price
    
   
    new_user = input("Are there any users left? (Yes/No): ").strip()


if offer_dic:
    find_highest_bidder(offer_dic)
else:
    print("No bids were entered.")

print(offer_dic)
