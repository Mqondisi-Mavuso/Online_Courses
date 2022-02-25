# Day 15 of 100 python bootcamp
# Coffee machine
# from art import logo
from data import MENU, resources
# TODO 1: Take user's coffee order and compare it against the resources and the money they have
machine_resources = resources
machine_resources["money"] = 0
money = 0


def report():
    global money
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    money += resources["money"]

    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# TODO 2: Check if the money the user has will be enough for the order or not

# TODO 3: Check if the resources are enough for the order or not


def get_order(customer_order):
    """
    Takes string of the customer's oder
    :param customer_order: string
    :return: dictionary containing the customer's order
    """
    if customer_order == '1':
        order_ingredients = MENU["espresso"]
        return order_ingredients
    elif customer_order == '2':
        order_ingredients = MENU["latte"]
        return order_ingredients
    elif customer_order == '3':
        order_ingredients = MENU["cappuccino"]
        return order_ingredients
    else:
        return "Wrong order, Please check your option again"


total_cash = 0


def get_money():
    """
    Takes input from the user and increment the global variable "total_cash" to give
    the total cash the customer has input into the coffee machine
    """
    global total_cash
    quarter = int(input("How many quarters? "))*0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? "))*0.01
    total_cash += quarter + dimes + nickels + pennies
    return total_cash


def enough_resources(customer_order, customer_cash):
    """Takes dictionary with the customer order and cash, returns string integer which
     signals if the resources are enough or not
    """
    # checking for water
    global order
    if customer_order["ingredients"]["water"] > resources["water"]:
        return '1'

    elif customer_order["ingredients"]["coffee"] > resources["coffee"]:
        return '3'

    elif customer_cash < customer_order["cost"]:
        return '4'

    elif customer_order["ingredients"]["milk"] > resources["milk"]:
        return '2'

    else:
        return '0'


should_continue = True
while should_continue:
    order = input("What would you like to have? 1. Espresso, 2. Latte, 3. Cappuccino? ")
    # turn off the machine if the user typed off
    if order == "off":
        should_continue = False
        break
    elif order == "report":
        report()
        continue
    total_cash = get_money()
    the_order = get_order(order)
    # TODO 4: If both todo 2 and 3 are met, their coffee will be made using the machine resources
    enough_r = enough_resources(the_order, total_cash)

    if enough_r == '0':
        # Make the coffee, reduce the resource, and calculate change
        resources["water"] -= the_order["ingredients"]["water"]
        resources["milk"] -= the_order["ingredients"]["milk"]
        resources["coffee"] -= the_order["ingredients"]["coffee"]
        resources["money"] = the_order["cost"]
        change = round(total_cash - the_order["cost"], 2)
        if order == '1':
            print("Here is your Espresso!")
        elif order == '2':
            print("Here is your Latte!")
        elif order == '3':
            print("Here is your Cappuccino!")
        print(f"Here is your change of ${change}")
    else:
        if enough_r == '1':
            print("Sorry, there is not enough water")
        elif enough_r == '2':
            print("Sorry, there is not enough milk")
        elif enough_r == '3':
            print("Sorry, there is not enough coffee")
        elif enough_r == '4':
            print("Sorry, not enough cash")
        should_continue = False
