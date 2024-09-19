print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Let's begin your journey!\nThere is no turning back from this point!!!")
direction = input("First, choose which direction to proceed: Left or Right\n").lower()
if direction == "left":
    print("There's a river in front of you.")
    action = input("Swim or Wait\n").lower()
    if action == "wait":
        print("The water slowly disappears as you wait, the journey continues")
        print("After walking for a while you face 3 mysterious doors, Red, Yellow, and Blue...")
        door = input("Which one will you enter?\n").lower()
        if door == "yellow":
            print("You found the treasure and won the game! Congrats!!!")
        elif door == "blue":
            print("A hungry lion awaits as you enter the room, now you've become its feast!\nGame over!")
        elif door == "red":
            print("As you open the door, engulfing flame surrounds you and burns you to ashes!\n Game over!")
        else:
            print("You did not follow the rule, you die immediately.\nGame over!")
    else:
        print("You are attacked by a lurking crocodile.\nGame over!")
else:
    print("You fell into a hole.\nGame over!")
