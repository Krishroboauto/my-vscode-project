from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine  import MoneyMachine

CM = CoffeeMaker()
MN = Menu()
Money = MoneyMachine()



on = True
while on:
    choice = input("What would you like? Type 'espresso', 'latte', 'cappuccino': ")
    if choice == 'report':
        CM.report()
        Money.report()
    elif choice == 'off':
        print('Turning off')
        on = False
    else:
        drink = MN.find_drink(choice)
        check_resource = CM.is_resource_sufficient(drink)
        if check_resource:                     
            price = drink.cost
            amt_paid = Money.make_payment(price)
            if amt_paid:
                CM.make_coffee(drink)
            else:
                print("focus on your career!")






