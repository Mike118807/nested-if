# Task 2: Setting the Scene

# Based on your corrected code from Task 1, expand the game. If the user chooses "cave", 
# ask them if they want to "light a torch" or "proceed in the dark", 
# and provide outcomes for each decision.


place = input("Choose a place: forest or cave? ")

if place == "forest":
    
    action = input("climb a tree or cross a river?")
    
    if action == "climb a tree":
        print("You found a bird's nest!")
    
    else: action == "cross a river"
    print("You found a boat!")

elif place == "cave":
    action = input("light a torch or proceed in the dark?")

    if action == "light a torch":
        print("Continue with a bright view")

    elif action == input("proceed in the dark"):
            print("Continue into the dark hole blind")