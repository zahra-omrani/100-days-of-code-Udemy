from IPython.display import clear_output

# Initialize an empty dictionary to store offers
offer_dic = {}

# Function to find the highest bidder
def find_highest_bidder(offer_dic):
    highest_bid = 0
    winner = ""

    for name, bid_amount in offer_dic.items():  # Use .items() to iterate over key-value pairs
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = name
    
    print(f"The winner is {winner} with a bid of {highest_bid}")

# Variable to control the loop
new_user = "Yes"

# Loop to get new offers
while new_user.lower() == "yes":
    clear_output(wait=True)
    
    # Collect new offer details
    name = input("What is your name: ")
    bid_price = int(input("What is your bid price: "))
    offer_dic[name] = bid_price
    
    # Ask if there are any users left
    new_user = input("Are there any users left? (Yes/No): ").strip()

# Find and print the highest bidder
if offer_dic:
    find_highest_bidder(offer_dic)
else:
    print("No bids were entered.")

# Print all offers
print(offer_dic)
