from coffee_machine_data import MENU, resources, measurement_units, value_of_coin


# def print_resource_report():
#     resource_keys = (list(resources.keys()))
#
#     for key in resource_keys:
#         measurement_units = key[key.rfind("_") + 1:]
#         resource_type = key[:key.find("_")]
#         print(f"{resource_type.capitalize()}: {resources[key]}{measurement_units}")


def print_resource_report():
    resource_keys = (list(resources.keys()))
    for key in resource_keys:
        print(f"{key.capitalize()}: {resources[key]}{measurement_units[key]}")


def check_ingredients_sufficient(option):
    ingredients = MENU[option]['ingredients']

    for key in ingredients:
        if ingredients[key] >= resources[key]:
            print(f"Sorry there is not enough {key}.")
            return False

    return process_coins(option)


def process_coins(option):
    entered_coins = {
        'quarters': float(input("How many quarters?")),
        'dimes': float(input("How many dimes?")),
        'nickles': float(input("How many nickles?")),
        'pennies': float(input("How many pennies?")),
    }

    price = MENU[option]['cost']
    money_arrived = 0
    change_amount = None

    for coin in entered_coins:
        money_arrived += entered_coins[coin] * value_of_coin[coin]
    print(f"Money arrived: {money_arrived:.2f}$")

    if money_arrived > price:
        change_amount = money_arrived - price
        money_arrived = price
        print(f"Here is {change_amount:.2f}$ dollars in change.")
        resources['money'] += money_arrived
    elif money_arrived == price:
        resources['money'] += money_arrived
    else:
        print("Sorry that's not enough money. Money refunded.")
        money_arrived = 0
        return False

    return make_coffee(option)


def make_coffee(option):
    """Deducting resources"""
    resource_list = MENU[option]['ingredients']

    for key in resource_list:
        resources[key] -= MENU[option]['ingredients'][key]

    print(f"Here is your {option}. Enjoy!")


power_on = True

while power_on:
    option = input("What would you like? (espresso/latte/cappuccino): ")

    if option == "espresso" or option == "latte" or option == "cappuccino":
        check_ingredients_sufficient(option)
    elif option == "report":
        print_resource_report()
    elif option == "off":
        print("Thank you for using Coffee Machine.......shut down.")
        power_on = False
    else:
        print("Sorry, that's not a valid option. Please try again.")
