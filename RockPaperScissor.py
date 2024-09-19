rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
import random
print("Welcome to Rock-Paper-Scissors")
print("You will play against the computer...")
print("Here's the rule\nChoose 0 for Rock, 1 for Paper, and 2 for Scissors")
choices = [rock, paper, scissors]
player_action = int(input("Your choice:\n"))
computer_action = random.randint(0,2)
if player_action <0 or player_action>2:
    print("Please type a valid input!")
    exit()
else:
    print(f"You choose\n{choices[player_action]}")
    print(f"Computer chooses\n{choices[computer_action]}")
    if player_action == computer_action:
        print("It was a draw!")
    else:
        if player_action == 0 and computer_action == 2:
            print("You win!")
        elif player_action == 2 and computer_action == 0:
            print("You loose!")
        elif player_action == 1:
            if computer_action > player_action:
                print("You loose!")
            else:
                print("You win!")
        elif player_action == 0:
            if computer_action == 1:
                print("You loose!")
