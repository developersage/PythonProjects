from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menus = Menu()
coffee = CoffeeMaker()
money = MoneyMachine()

user_input = ""
while user_input.lower() != "off":
    user_input = input(f'\nWhat would you like? {menus.get_items()}Report/Off :').lower()
    if user_input in menus.get_items():
        if money.make_payment(menus.find_drink(user_input).cost):
            if coffee.is_resource_sufficient(menus.find_drink(user_input)):
                coffee.make_coffee(menus.find_drink(user_input))
    elif user_input == "report":
        coffee.report()
        money.report()
print("Coffee Machine turning off...")
