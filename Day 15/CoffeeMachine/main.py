


import sys
import re

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

# TODO: Turn off the Coffee Machine by entering “ off​ ” to the prompt. 
def turn_off(user_input):
    if user_input == 'off':
        sys.exit("User asked to turn off the coffe mechine!")
    

# TODO: Print report. 
def print_report(user_input):
    if user_input == 'report':
        print(
            f"Water: {resources['water']}\n"
            f"Milk: {resources['milk']}\n"
            f"Coffee: {resources['coffee']}\n"
            f"Money: {resources['money']}\n"
        )
# TODO: Check resources sufficient? 
def resource_sufficient():
    if resources['water'] < 50 :
        return("Sorry there is not enough water!")
    if resources ["milk"] < 100: 
        return("Sorry there is not enough milk")
    if resources ["coffee"] < 18:
        return("Sorry there is not enough coffee")
# TODO: Process coins. 
import re

def process_coin(coins):
    def extract_coin_value(pattern, text):
        match = re.findall(pattern, text)
        return int(match[0]) if match else 0  # Convert to int or return 0 if not found

    quarter_coin = extract_coin_value(r"(\d+) quarter", coins)
    dimes_coin = extract_coin_value(r"(\d+) dime", coins)
    nickels_coin = extract_coin_value(r"(\d+) nickel", coins)
    pennies_coin = extract_coin_value(r"(\d+) penny", coins)

    total = 0.25 * quarter_coin + 0.1 * dimes_coin + 0.05 * nickels_coin + 0.01 * pennies_coin
    return total

# Example Usage:
print(process_coin("I have 3 quarters, 555555 dimes, 1 nickel, and 4 pennies."))  # Expected output: 1.04

# TODO: Check transaction succesreturn (sful? 
# Check if transaction was successful
def tran_succ(order, money_inserted):
    cost = MENU[order]['cost']

    if money_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        resources['money'] += cost
        change = money_inserted - cost
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        return True
# TODO: Make Coffee. 
def make_coffe(order):
    resources["coffee"] = resources["coffee"]- MENU[order]["ingredients"]["coffee"]
    resources ["milk"]  = resources["milk"] - MENU[order]["ingredients"]["milk"]
    resources["water"] = resources ["water"] - MENU [order]["ingredients"]["water"]
    resources["money"] = resources["money"] + MENU [order]["cost"]
    print("here is your"+order)

# TODO - todo note

# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):​ ” 
# order = input("What would you like? (espresso/latte/cappiccino): ")
# coins = input("Insert your coins:")

# money_inserted = process_coin(coins)


is_on = True
while is_on:
   order = input("What would you like? (espresso/latte/cappiccino): ")
   if order == "off":
       is_on = False
   else:
    coins = input("Insert your coins:") 
    money_inserted = process_coin(coins)
    if tran_succ(order, money_inserted):  # Check if transaction was successful
        resource_sufficient()
        make_coffe(order)


print( MENU["latte"]["ingredients"]["coffee"])