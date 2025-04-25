from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()
my_menue = Menu()

is_on = True

while is_on:
    options = my_menue.get_items()
    choice = input(f'what do you like ({options})')

    if choice == "off":
        is_on = False
    if choice == 'report':
        my_coffe_maker.report()
    else:
      drink = my_menue.find_drink(choice)
      if my_coffe_maker.is_resource_sufficient(drink) == True and my_money_machine.make_payment(drink.cost):
         my_coffe_maker.make_coffee(drink)
