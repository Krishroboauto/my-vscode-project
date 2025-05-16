from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker


myMenu = Menu()
#MyMenuItem = MenuItem()
CM = CoffeeMaker()
Money = MoneyMachine()

mac_status = True

while mac_status:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "report":
        CM.report()
        Money.report()
    elif user_choice == "off":
        mac_status = False  #switch off machine
    else:
        drink = myMenu.find_drink(user_choice)
        if CM.is_resource_sufficient(drink):
            #payment = Money.process_coins()
            if Money.make_payment(drink.cost):
                CM.make_coffee(drink)
            
        else:
            mac_status = False


