from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_menu = Menu()
my_machine = CoffeeMaker()
money_mac = MoneyMachine()

is_working = True;
while is_working:
    print("What would you like? (espresso/latte/cappuccino/)")
    order = input()
    if order == "report":
        my_machine.report()
        my_machine.report()
    elif order == "off":
        is_working = False
        print("Thank you. Good Bye!")
    else:
        desired_drink = my_menu.find_drink(order)
        if desired_drink:
            if my_machine.is_resource_sufficient(desired_drink):
                if money_mac.make_payment(desired_drink.cost):
                    my_machine.make_coffee(desired_drink)


