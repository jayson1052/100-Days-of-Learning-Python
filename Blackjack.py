from art import logo
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def display_score(deck):
    print(f"    Your cards: {deck}, current score: {sum(deck)}")

def deal_card(deck):
    return deck.append(random.choice(cards))

def calculate_score(deck):
    if 11 in deck and 10 in deck and len(deck) == 2:
        return 0
    elif 11 in deck and len(deck) > 2:
        if sum(deck) > 21:
            deck.remove(11)
            deck.append(1)
    return sum(deck)

def compare(a, b):
    if a == b:
        print("It's a draw!")
    if a == 0:
        print("Player has a Blackjack and wins the game!")
    elif b == 0:
        print("Computer has a Blackjack, player loses!")
    elif b > 21:
        print("Computer busted, player won!")
    elif a > 21:
        print("Player busted, player lost!")
    elif a > 21 and b > 21:
        print("Both busted, draw!")
    else:
        if a > b:
            print("Player wins!")
        elif a < b:
            print("Player loses!")

def blackjack():
    user_cards = []
    computer_cards = []
    for i in range(2):
        deal_card(user_cards)
        deal_card(computer_cards)
    player_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    display_score(user_cards)
    print("    Computer's first card:", computer_cards[0])

    keep_drawing = True
    while keep_drawing:
        ask_to_draw = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if ask_to_draw == 'y':
            deal_card(user_cards)
            player_score = calculate_score(user_cards)
            display_score(user_cards)
            print("    Computer's first card:", computer_cards[0])
            if calculate_score(user_cards) > 21:
                keep_drawing = False
        elif ask_to_draw == 'n':
            keep_drawing = False

    while computer_score < 17:
        deal_card(computer_cards)
        computer_score = calculate_score(computer_cards)
    print(f"    Your final hand: {user_cards}, final score: {player_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    compare(player_score, computer_score)
def main():
    game_on = True
    while game_on:
        play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if play == 'y':
            print(logo)
            blackjack()
        elif play == 'n':
            print("Have a good day!")
            game_on = False

main()
