from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()

coffee_maker = CoffeeMaker()

money_machine = MoneyMachine()

is_power_on = True

while is_power_on:
    option = input(f"What would you like? ({menu.get_items()})").lower()
    if option == 'report':
        coffee_maker.report()
        money_machine.report()
    elif option == 'off':
        print("Shutting down...")
        is_power_on = False
    elif menu.find_drink(option):
        order = menu.find_drink(option)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)

