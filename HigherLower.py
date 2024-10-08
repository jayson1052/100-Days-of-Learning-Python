'''
1. Create game logo - done, them import to main.py
2. Import data, random
2. Def game function:
    print: Logo 1
    print: compare A: name, description, from where
    print: Logo 2
    print: against B: name, description, from where
A and B took randomly from the data list of dictionaries, with name, description and where are equivalent keys
3. Def main:
    while True:
        execute game function
        input: Who has more followers? Type 'A' or 'B', input should be capitalized
        correct -> again with B, new A = old B, score += 1
        wrong -> end game immediately, print final score, break the loop
'''

from art import *
from game_data import *
import random
def random_data():
    randomized_data = random.choice(data)
    followerData = randomized_data['follower_count']
    return [f"{randomized_data['name']}, a {randomized_data['description']}, from {randomized_data['country']}", followerData]

def compare(a, b):
    if a > b:
        return "A"
    elif a < b:
        return "B"


def higher_lower():
    score = 0
    b = random_data()
    while True:
        print(logo)
        a = b
        print("Compare A:", a[0])
        print(vs)
        b = random_data()
        while b == a:
            b = random_data()
        print("Against B:", b[0])


        guess = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        while guess not in "AB":
            guess = input("Invalid input! Type 'A' or 'B': ").capitalize()
        if guess == compare(a[1], b[1]):
            score += 1
            print(f"Correct! Current score: {score}. Let's continue!")
            print("\n" * 20)
            continue
        else:
            print("You guessed wrong! Total score:", score)
            break
higher_lower()

