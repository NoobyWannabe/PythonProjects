from data import MENU
from data import resources

is_on = True
income = 0


def greeting():
    greeting_result = input("What would you like? (espresso/latte/cappuccino): ")
    return greeting_result


def report():
    print(f"Water: {resources['water']}")
    print(f"milk: {resources['milk']}")
    print(f"coffee: {resources['coffee']}")
    print(f"Money: {resources['money']} ")


def resources_check(drink):
    available_water = resources['water']
    if MENU[drink]['ingredients']['water'] > available_water:
        print("Not enough water. Please choose another option, or have the machine refilled. ")
        return False
    available_milk = resources['milk']
    if MENU[drink]['ingredients']['milk'] > available_milk:
        print("Not enough milk. Please choose another option, or have the machine refilled. ")
        return False
    available_coffee = resources['coffee']
    if MENU[drink]['ingredients']['coffee'] > available_coffee:
        print("Not enough coffee Please choose another option, or have the machine refilled. ")
        return False
    else:
        return True


def transaction(drink):
    """takes water, milk, coffee cost and deducts from inventory"""
    resources['water'] -= MENU[drink]['ingredients']['water']
    resources['milk'] -= MENU[drink]['ingredients']['milk']
    resources['coffee'] -= MENU[drink]['ingredients']['coffee']
    resources['money'] += MENU[drink]['cost']
    return


def insert_coins():
    quarters = int(input("How many quarters are you putting in? "))
    dimes = int(input("How many dimes are you putting in? "))
    nickels = int(input("How many nickels are you putting in? "))
    pennies = int(input("How many pennies are you putting in? "))
    value = (quarters * .25) + (dimes * .1) + (nickels * .05) + (pennies * .01)
    return value


while is_on:
    user_choice = greeting()
    if user_choice == 'report':
        report()
    elif user_choice == 'off':
        is_on = False
    else:
        if resources_check(user_choice):
            item_cost = float(MENU[user_choice]['cost'])
            inserted_coins = insert_coins()
            if inserted_coins < MENU[user_choice]['cost']:
                print("Sorry, that's not enough money. Money Refunded.")
            else:
                transaction(user_choice)
                change = round((inserted_coins - MENU[user_choice]['cost']), 2)
                print(f"Here is your change: {change} ")
                print(f"Here is your {user_choice}. Enjoy! ")
