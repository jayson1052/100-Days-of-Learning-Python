logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
calc_function = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(logo)
    print("!!! Please make sure you put in numbers only in order for this to function correctly !!!")
    num1 = float(input("What is the first number?: "))
    while True:
        print("+\n-\n*\n/")
        operation = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        if operation in "+-*/":
            result = calc_function[operation](num1, num2)
            print(f"{num1} {operation} {num2} = {result}")
        else:
            print("Please follow the given operations only!")
            break

        again = input(f"Type 'y' to continue calculating with {result}, and type 'n' to start a new calculation: ").lower()
        if again == "y":
            num1 = result
            continue
        elif again == "n":
            print("\n"*17)
            calculator()
        else:
            print("You typed in a wrong key, the program will stop now!")
            break
calculator()
