# Day 16 of 100, Object oriented programming
# Coffee machine using classes, methods and attributes

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# constructing the coffee machine object using the Coffee Maker class
machine = CoffeeMaker()
coffee_menu = Menu()
pos_terminal = MoneyMachine()

is_on = True
while is_on:
    order = input(f"What would you like to have? ({coffee_menu.get_items()}): ")    # str of the coffee
    drink = coffee_menu.find_drink(order)           # object containing the name, cost and ingredients of the drink
    if order == "off":
        is_on = False
        break
    elif order == "report":
        machine.report()
        pos_terminal.report()

    else:
        if machine.is_resource_sufficient(drink) and pos_terminal.make_payment(drink.cost):
            machine.make_coffee(drink)
