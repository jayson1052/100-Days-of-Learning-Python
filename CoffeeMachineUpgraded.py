from coffee_maker import *
from menu import *
from money_machine import *
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

# correct input
    if order in menu.get_items():
        drink = menu.find_drink(order)
        print(f"Your order is: {drink.name}.") #confirm order

      # check if machine has enough ingredients
        if coffee_maker.is_resource_sufficient(drink):
            print(f"You need to insert ${drink.cost}") #display price
            pay_accept = money_machine.make_payment(drink.cost)
            if pay_accept:
                coffee_maker.make_coffee(drink)



      # insufficient ingredients:
        else:
            print("Not enough ingredients to make your order!")
            print("Try another drink, or type 'off' to quit!")
            continue

# user type in 'off'
    elif order == 'off':
        print("Machine shutting down in 3, 2, 1...")
        print("...")
        print("Machine has been turned off!")
        break


# user type 'report'
    elif order == 'report':
        coffee_maker.report()
        money_machine.report()
# Invalid syntax or unavailable drink
    else:
        print("Please choose from the available drinks only!")
        print("Rebooting...")
        continue
