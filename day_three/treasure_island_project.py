"""This is a treasure island project"""
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome To Treasure Island!")
print("Your mission is to find the treasure")
direction_1 = input('You are at a cross road. where do you want to go? Type "left" or "right":').lower()
if direction_1 == "left":
    user_input_1 = input("You have come to a lake, There is an island in the middle of the lake. Type 'wait' to wait "
                         "for a boat. "
                         "Type 'swim' to swim across:").lower()
    if user_input_1 == "wait":
        user_input_2 = input(
            "You arrived at the island unharmed. There is a house with 3 doors. One is red, One is yellow and the "
            "last is blue:")
        if user_input_2 == "yellow":
            print("You found the treasure, You win!")
        elif user_input_2 == "red":
            print("Its a room full of fire, Game over, you loose!")
        elif user_input_2 == "blue":
            print("You entered a room full of beast. Game Over!")
        else:
            print("You entered a door that doesnt exist")
    else:
        print("You got attacked by an angry trout. Game over")
else:
    print("You fell into a hole. Game Over")

