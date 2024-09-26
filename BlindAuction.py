# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo
def auction():
    print(logo)
    print("Welcome to today Blind Auction!")
    num_participants = int(input("How many people are joining this auction?\n"))
    auction_data = {}
    print("Let's begin")
    for i in range(num_participants):
        name = input("What is your name?\n").title()
        price = int(input("How much would you pay?\n$"))
        auction_data[name] = price
        print("\n"*20)
        print(logo)
    maximum = 0
    winner = ""
    for name in auction_data:
        if auction_data[name] > maximum:
            maximum = auction_data[name]
            winner = name
    print(f"The winner is {winner} with the bid of ${maximum}")
def main():
    while True:
        auction()
        again = input("Do you want to have another auction? Y or N\n").lower()
        if again == "y" or again == "yes":
            continue
        elif again == "n" or again == "no":
            print("Have a good day!")
            break
        else:
            raise Exception("Please type in the correct input!")
main()
