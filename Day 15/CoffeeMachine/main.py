import sys
import re

# --- MENU CONFIGURATION ---
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

# --- INITIAL RESOURCE STATE ---
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0
}

# --- PRINT REPORT ---
def print_report():
    print(
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${resources['money']:.2f}\n"
    )

# --- CHECK IF RESOURCES ARE SUFFICIENT FOR THE ORDER ---
def resource_sufficient(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        if resources.get(item, 0) < ingredients[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

# --- PROCESS COIN INPUT ---
def process_coin(coins_input):
    """This function returns the total amount that the user entered"""
    def extract_coin_value(pattern, text):
        match = re.findall(pattern, text)
        return int(match[0]) if match else 0

    quarter = extract_coin_value(r"(\d+)\s*quarter", coins_input)
    dime = extract_coin_value(r"(\d+)\s*dime", coins_input)
    nickel = extract_coin_value(r"(\d+)\s*nickel", coins_input)
    penny = extract_coin_value(r"(\d+)\s*penny", coins_input)

    total = 0.25 * quarter + 0.10 * dime + 0.05 * nickel + 0.01 * penny
    return round(total, 2)

# --- CHECK TRANSACTION SUCCESS ---
def tran_succ(order, money_inserted):
    cost = MENU[order]['cost']

    if money_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_inserted - cost, 2)
        if change > 0:
            print(f"Here is ${change:.2f} in change.")
        resources['money'] += cost
        return True

# --- MAKE COFFEE AND DEDUCT INGREDIENTS ---
def make_coffee(order):
    ingredients = MENU[order]["ingredients"]
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f"Here is your {order}. Enjoy! ☕️")

# --- MAIN PROGRAM LOOP ---
def coffee_machine():
    is_on = True
    while is_on:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            print("Turning off... Bye! 👋")
            is_on = False

        elif order == "report":
            print_report()

        elif order in MENU:
            if resource_sufficient(order):
                coins_input = input("Insert your coins (e.g., '1 quarter, 2 dimes, 1 nickel, 4 pennies'): ")
                money_inserted = process_coin(coins_input)
                if tran_succ(order, money_inserted):
                    make_coffee(order)

        else:
            print("Invalid input. Please choose espresso, latte, or cappuccino.")

# --- RUN THE COFFEE MACHINE ---
coffee_machine()
