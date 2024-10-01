

logo = '''

 __    __  __ __   ____  ______  __   _____     ______  __ __   ____  ______      ____   __ __  ___ ___  ____     ___  ____   _____ 
|  |__|  ||  |  | /    ||      ||  | / ___/    |      ||  |  | /    ||      |    |    \ |  |  ||   |   ||    \   /  _]|    \ /     |
|  |  |  ||  |  ||  o  ||      ||_ |(   \_     |      ||  |  ||  o  ||      |    |  _  ||  |  || _   _ ||  o  ) /  [_ |  D  )|  Y  |
|  |  |  ||  _  ||     ||_|  |_|  \| \__  |    |_|  |_||  _  ||     ||_|  |_|    |  |  ||  |  ||  \_/  ||     ||    _]|    / |__|  |
|  `  '  ||  |  ||  _  |  |  |       /  \ |      |  |  |  |  ||  _  |  |  |      |  |  ||  :  ||   |   ||  O  ||   [_ |    \    |__|
 \      / |  |  ||  |  |  |  |       \    |      |  |  |  |  ||  |  |  |  |      |  |  ||     ||   |   ||     ||     ||  .  \    __ 
  \_/\_/  |__|__||__|__|  |__|        \___|      |__|  |__|__||__|__|  |__|      |__|__| \__,_||___|___||_____||_____||__|\_|   |__|
                                                                                                                                    
                                                                                                                                                                     
'''
import random


def compare(a,b):
    if a > b:
        return "Too high, please guess again!"
    elif a < b:
        return "Too low, please guess again!"
    else:
        return "Congrats you found the mysterious number!"
def guessing_game():
    print(logo)
    print("I'm thinking of a number between 1 and 100.")
    hidden_number = random.randint(1,100)

    attempt_count = 0

    difficulty = input("Please choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == 'easy':
        attempt_count = 10
    elif difficulty == 'hard':
        attempt_count = 5
    while attempt_count > 0:
        print(f"You have {attempt_count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        result = compare(guess, hidden_number)
        if result != "Congrats you found the mysterious number!":
            print(result)
            attempt_count -= 1
            if attempt_count == 0:
                print("You've run out of guess, you lose!")
        else:
            print(result)
            break
    print("The number is", hidden_number)

def main():
    while True:
        play = input("Do you want to play a game of Number Guessing? Type 'y' or 'n': ").lower()
        if play == 'y':
            guessing_game()
            continue
        else:
            break
main()
