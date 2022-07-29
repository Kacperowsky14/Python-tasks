import time
import random

equipment = []
treasures = ("gold bar", "small purse", "rubbish", "strange stone", "underpants", "sword", "dagger")

print("You are a lonely seeker, we'll see what you find!\n")
time.sleep(1)
start_game = (input("Enter the 'start' to go!\n"))
if (start_game.upper()) == "START":
    print("A great trip is ahead of you, at the very beginning you can see that something is lying near the tree, let's see what it is!")
    x = random.choice(treasures)
    time.sleep(2)
    print("Great, you found ", x ,)
    time.sleep(2)
    found_item = int(input("Press 1 to add to inventory or press 0 to continue without adding\n"))
    if found_item == 1:
        equipment.append(x)
        time.sleep(1)
        print("Added! let's go.\n")
        print("Equipment- ", equipment ,)
        time.sleep(2)
    else:
        time.sleep(1)
        print("Let's go.")
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print(".")
    time.sleep(1)
    print("Another treasure! A mystery bag in front of you, let's see what it is!")
    time.sleep(2)
    a = random.choice(treasures)
    b = random.choice(treasures)
    print("After opening the bag, it turned out that ",a,", and ", b)
    time.sleep(3)
    print("Save: ",a," press 1 \n"
    "Save: ",b," press 2  \n"
    "Keep both of these - press 3\n"
    "Keep going, take nothing - 0 \n")
    found_item = int(input("Choose wisely!\n"))
    if found_item == 1:
        equipment.append(a)
        print("Added ",a," to inventory!")
        time.sleep(2)
    if found_item == 2:
        equipment.append(b)
        print("Added " ,b, " to inventory!")
        time.sleep(2)
    if found_item == 3:
        equipment.append(a)
        equipment.append(b)
        time.sleep(2)
        print("Added ",a," and ",b," to inventory!\n")
        print("Your inventory: ",equipment,)
    time.sleep(3)
    print("You want to go, but you hear some strange noises in the distance ...")
    time.sleep(2)
    print("You come closer, the noise you heard is a growl")
    time.sleep(2)
    print("It's a wolf!\n")
    wolf = int(input("1- escape, 2- state to fight the wolf.\n"))
    if wolf == 1:
        print("You run away as fast as you can")
    if wolf == 2:
        if "underpants" in equipment:
            print("Underpants are a premium item. The wolf runs away. You win")
        if "underpants" not in equipment:
            if "dagger" in equipment:
                print("You kill a wolf with a dagger!")
            if "dagger" not in equipment:
                if "sword" in equipment:
                    print("You cut your opponent open with your sword!")
                if "sword" not in equipment:
                    print("You have no weapon, you were tasty for the wolf [*]")
input("Press enter to end the game")

                   
