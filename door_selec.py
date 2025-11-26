print(''' 
 _                                     
| |                                    
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
| __| '__/ _ \/ _` / __| | | | '__/ _ |
| |_| | |  __/ (_| \__ \ |_| | | |  __/
 \__|_|  \___|\__,_|___/\__,_|_|  \___| HUNT.
''')

print("\nWelcome to Treasure Island ")
print("Your mission is to find the treasure.")

choice1 = input("Enter the direction of ship ('left' or 'right'):")

if choice1 == "left" or "Left":
    choice2 = input("You want to go on island by ('ship' or 'wait'):")
    if choice2 == "wait".lower():
        choice3 = input("you have to choose the door ('red', 'yellow' and 'blue'):")
        if choice3 == "red".lower():
            print("You're burned by fire. Game Over.")
        elif choice3 == "yellow".lower():
            print("You win!,  congratulation you get your treasure.")
        elif choice3 == "blue".lower():
            print("You're eaten by beasts. Game Over.")
        else:
            print("You choose a door that doesn't exit. Game Over.")
    else:
        print("Your're attacked by trout. Game Over.")
else:
    print("You're going to fall into a hole. Game over.")
                                       









 