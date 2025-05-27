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

    doors = []

    while len(prizes) > 0:

        prize_number = random.randrange(len(prizes))

        doors.append(prizes.pop(prize_number))
    
    print("\n             Monty Hall Simulation                   ")
    print("=======================================================")

    print("Now that you know how the game works, give it a try!\n")

    user_chosen_door = int(input("Pick a door from (1-3)? ")) # Aligns with the indexing of the doors

    print("You chose door:", user_chosen_door, '\n') # Aligns with the users perspective of the door they selected

    door_index = 0 # The door position in the array, changed_door_index.e Door 1 would be at position 0 in the array

    user_door_list = user_chosen_door - 1

    while True:

        if doors[door_index] == 'goat' and door_index != (user_door_list): # Checks for a goat behind the door and check that's it's not the same door the User chose
            user_door_index = door_index + 1
            print("Let's open up door number", user_door_index) # Aligns with the users perspective of a door that
            print("...Woah, it's a goat!\n")
            break
        
        door_index+=1
    
    print("So, here's your options, you can stay with your door or you can switch to the other door.")
    
    user_decision = input("Stay/Switch Doors: ").lower()

    def final_result(chosen_door):
        print("\n====================================\n")
        print("Final Results:")
        if doors[chosen_door] == "car":
            
            print("Jeez, Congrats on your brand new car!!\n\n")
        else:
            
            print("Aww man, better luck next time\n\n")

        return 0 
    
    while True:

        if user_decision == "stay":
            print("\nInteresting.. you choose to stay.")
            final_result(user_door_list)
            break

        elif user_decision == "switch":

            print("\nOuuu, choosing to switch..")
              
            for changed_door_index in range(len(doors)-1):
                    
                if doors[changed_door_index] != user_door_list and doors[changed_door_index] != door_index:

                    final_result(changed_door_index)
                    return
        else:
            user_decision = input("Stay/Switch Doors: ").lower()

        
def main():

    simulation()

    return 0
    

# Function call,
main()
