place = input("Choose a place: forest or cave? ")


if place == "forest":
    action = input("climb a tree or cross a river? ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You light your torch and enter the cave!")
    elif action == "proceed in the dark":
        print("You enter the deep dark cave without lighting your torch!")
    else:
        pass
else:
    pass