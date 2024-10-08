MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 30000,
    "milk": 20000,
    "coffee": 10000,
    "money": 0,
}
def report_resources():
    print("Remaining resources:")
    print("  Water:", resources['water'])
    print("  Milk:", resources['milk'])
    print("  Coffee:", resources['coffee'])
    print("Money:", resources['money'])
def pay_prompt():
    print("Please insert your money to continue:")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total_money = quarter * 0.25 + dime * 0.1 + nickel * 0.05 + penny * 0.01
    return total_money

while True:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if order == 'off':
        print("Turning off coffee machine...")
        print("...\n" * 3)
        print("Machine has been shut down!")
        break
    elif order == 'report':
        report_resources()
        continue
    elif order in ["espresso", "latte", "cappuccino"]:
        order_ingredients = MENU[order]["ingredients"]
        order_cost = MENU[order]["cost"]

        for ingredient in order_ingredients:
            if order_ingredients[ingredient] > resources[ingredient]:
                print(f"Sorry, there is not enough {ingredient}")
                break
        else:
            total_pay = pay_prompt()

            if total_pay < order_cost:
                print("Sorry, that's not enough money. Money refunded...")
                continue
            elif total_pay >= order_cost:
                change = total_pay - order_cost
                if change > 0:
                    print(f"Here's your change: ${change}")
                resources['money'] += order_cost
                for ingredient in order_ingredients:
                    resources[ingredient] -= order_ingredients[ingredient]
                print(f"Here is your {order}. Enjoy!")
                continue
    else:
        print("Invalid input! Please only choose an available drink!")
        continue
