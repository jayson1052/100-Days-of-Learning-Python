import random
from hangman_words import word_list
from hangman_art import *
def main():
    print(logo)
    lives = 6


    chosen_word = random.choice(word_list)
    # print(chosen_word)

    placeholder = ""
    word_length = len(chosen_word)
    for position in range(word_length):
        placeholder += "_"
    print("Word to guess: " + placeholder)

    correct_letters = []
    display = []
    for i in range(word_length):
        display.append("_")
    while lives >0 and "_" in display:
        guess = input("Guess a word: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a valid single letter.")
            continue

        if guess in display or guess in correct_letters:
            print(f"You already guessed {guess}. Try another letter!")
            continue

        if guess in chosen_word:
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess
                    correct_letters.append(guess)
            print(''.join(display))
        else:
            lives -= 1
            print(f"You guess {guess}, it's not in the word!")
        print(stages[lives])

        if "_" not in display:
            print("You win!")
            break
    if lives == 0:
        print("You lost!")
        print("The word was:", chosen_word)
    proceed = input("Do you want another round? Yes or No\n").lower()
    if proceed == 'yes':
        main()
    else:
        print("Bye, have a good day!")
main()
