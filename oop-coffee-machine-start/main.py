from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_money_machine = MoneyMachine()
my_coffee = CoffeeMaker()
menu = Menu()

machine_is_on = True

while machine_is_on:
    options = menu.get_items()
    order_item = input(f"What would you like to order?\nWe have {options}: ").lower()
    if order_item == "off":
        machine_is_on = False
    elif order_item == "report":
        my_coffee.report()
        my_money_machine.report()
    else:
        drink = menu.find_drink(order_item)
        if my_coffee.is_resource_sufficient(drink) and my_money_machine.make_payment(drink.cost):
            my_coffee.make_coffee(drink)
        else:
            print("we dont have it")

