'''
Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. Now, do you want to pick door No. 2? What is the probability to win the car if you switch?
'''

'''
Before the show the Host chooses 1 of 3 doors to put the car behind Car

When the show start the User is prompted to choose a door

Host opens a door with a Goat behind it and then allows the user to keep or switch doors

User chooses to switch doors, since this yield the better expectation, but is this the correct choice?
'''

import random


def simulation():

    prizes = ["goat", "car", "goat"]

    random.shuffle(prizes)

    print("\n             Monty Hall Game                   ")
    print("=======================================================")
    print("Now that you know how the game works, give it a try!\n")

    users_door = int(input("Pick a door (1-3): ")) - 1 # Asking the user to pick a door

    print("You chose door:", users_door + 1) # Showing the user the door that they picked

    # Getting all avaliable doors, that the user didn't choose and have a goat behind them
    avaliable_doors = [door for door in range(len(prizes)) if door != users_door and prizes[door] == "goat"] 

    host_opened_door = random.choice(avaliable_doors)

    print("\nLet's open door number", host_opened_door + 1)
    print("(Behind the door is a goat!)")

    print("\nSo, here's a question for you.\n")
    users_decision = input("Would you like to Stay or Switch doors. (Stay/Switch): ").lower()
    
    while True:

        if users_decision == "stay":
            print("\nInteresting.. you're sticking with this door.")
            final_choice = users_door
            break
        
        elif users_decision == "switch":
            final_choice = [final_door for final_door in range(len(prizes)) if final_door not in [users_door, host_opened_door]][0]
            print("\nWoah, you choose to switch door number", final_choice, ".")
            break
        else:
            print("\nYour input is invaild.")
            users_decision = input("Would you like to Stay or Switch doors. (Stay/Switch): ").lower()

    print("\n======================================\n")
    print("Final Results:")
    if prizes[final_choice] == "car": 
        print("Congrats, you won a brand new car!!!")

    else:
        print("Oh no, better luck next time.")
def main(): 
    simulation()

main()
