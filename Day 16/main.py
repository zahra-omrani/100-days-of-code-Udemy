from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_coffe_maker = CoffeeMaker()
my_money_machine = MoneyMachine()

user_order = input("What would you like? (espresso/latte/cappuccino/):")
recieved_money = my_money_machine.process_coins()
print(recieved_money)
if user_order == 'report':
   my_coffe_maker.report()
elif my_coffe_maker.is_resource_sufficient(user_order):
   my_coffe_maker.make_coffee()
