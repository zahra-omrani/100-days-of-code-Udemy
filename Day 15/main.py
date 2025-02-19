


import sys


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
            "Money: 000"
        )


# TODO: Prompt user by asking “ What would you like? (espresso/latte/cappuccino):​ ” 
order = input("What would you like? (espresso/latte/cappiccino): ")

print_report(order)
turn_off(order)
# TODO: Check resources sufficient? 
def resource_sufficient():
    if resources['water'] < 50 :
        print("Sorry there is not enough water!")
    if resources ["milk"] < 100: 
        print("Sorry there is not enough milk")
    if resources ["coffee"] < 18:
        print("Sorry there is not enough coffee")
# TODO: Process coins. 
def process_coin():
  
# TODO: Check transaction successful? 

# TODO: Make Coffee. 

# TODO - todo note