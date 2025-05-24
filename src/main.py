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

def simulation(trials, answer):   

    prizes = ["goat", "car", "goat"]

    doors = []

    while len(prizes) > 0:

        prize_number = random.randrange(len(prizes))

        doors.append(prizes.pop(prize_number))
    
    print("\n             Monty Hall Simulation                   ")
    print("=======================================================")

    print("Now that you know how the game works, give it a try!\n")

    user_chosen_door = int(input("Pick a door from (1-3)? ")) - 1

    print("You choose door:", user_chosen_door + 1, '\n')

    idx = 0

    while True:

        if doors[idx] == 'goat' and idx != (user_chosen_door):
            print("Let's open up door number", idx + 1)
            print("...Woah, it's a goat!\n")
            break

        idx+=1
    
    print("So, here's your options, you can stay with your door or you can switch to the other door.")
    
    user_decision = input("Stay/Switch Doors: ").lower()
    
    while True:

        if user_decision == "stay":
            print("\n Interesting.. you choose to stay.")
            break

        elif user_decision == "switch":
            print("\n")
            
            for door_number in range(len(doors)-1):

                if door_number != idx and door_number != user_chosen_door:
                    user_chosen_door = door_number



                    print("You choose to switch to door number: ", user_chosen_door+1)
                    break
            break

        else:
            user_decision = input("Stay/Switch Doors: ").lower()

    print("Now, let's open door number", user_chosen_door+1)
    
    if doors[user_chosen_door] == "car":

        "Jeez, Congrats on your brand new car!!"
    else:

        "Aww man, better luck next time"

        

    





# Function call,
simulation(1000, 1)




    







