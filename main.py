
# THE EDGE OF OBSIDIAN
# Function based version

import random

# character classes
character_classes = {
    "diplomat": {
        "charisma": 14,
        "wisdom": 12,
        "dexterity": 10,
        "strength": 8,
        "intelligence": 12,
        "constitution": 10,
    },
    "investigator": {
        "charisma": 10,
        "wisdom": 12,
        "dexterity": 12,
        "strength": 8,
        "intelligence": 14,
        "constitution": 10,
    },
    "survivor": {
        "charisma": 10,
        "wisdom": 10,
        "dexterity": 12,
        "strength": 14,
        "intelligence": 8,
        "constitution": 12,
    }
}

# -------------------------
# CHARACTER CREATION
# ------------------------- 

def create_character():
    print("Choose a class: diplomat, investigator, or survivor.")

    chosen_class = input("> ").strip().lower()

    while chosen_class not in character_classes:
        print("Please enter diplomat, investigator, or survivor.")
        chosen_class = input("> ").strip().lower()

    player = {
        "name": "Miles Carter",
        "class": chosen_class,
        "stats": character_classes[chosen_class].copy(),
        "inventory": [],
        "clues": [],
        "location": "funeral",
        "saved_woman": False,
        "checked_casket": False,
        "questioned_mourner": False,
        "rerolls": 3,
    }

    print(f"\nYou are {player['name']}.")
    print(f"Your class is the {player['class']}.")

    for stat, value in player["stats"].items():
        print(f"{stat.capitalize()}: {value}")

    return player

# ------------------------
# INVENTORY SYSTEM
# ------------------------

def show_inventory(player):

    if not player["inventory"]:
        print("\nYour inventory is empty.")

    else:
        print("\nInventory:")

        for item in player["inventory"]:
            print(f"-{item}")


# ------------------------
# CLUE SYSTEM
# ------------------------

def show_clues(player):
    if not player["clues"]:
        print("\nYou haven't discovered any clues.")

    else:
        print("\nDiscovered clues:")

        for clue in player["clues"]:
            print(f"-{clue}")

# -------------------------
# DICE / STATE CHECK SYSTEM
# ------------------------

def stat_check(player, stat, difficulty):

    modifier = (player["stats"][stat] - 10) // 2

    while True:
        roll = random.randint(1, 20)
        total = roll + modifier

        print(f"\nD20 Roll: {roll}")
        print(f"{stat.capitalize()} modifier: {modifier:+}")
        print(f"Total: {total}")
        print(f"Difficulty: {difficulty}")

        if total >= difficulty:
            print("\nCheck successful!")
            return True

        
        print("\nCheck failed!")

        if player["rerolls"] <= 0:
                  print("You have no rerolls remaining.")
                  return False

        print(f"\nRerolls remaining: {player['rerolls']}")
        print("1. Reroll")
        print("2. Accept failure")

        choice = input("> ").strip()

        while choice not in("1", "2"):
             choice = input("Please enter 1 or 2: ")
             
        if choice == "2":
             return False

        player["rerolls"] -= 1
        print(f"\nRerolls remaining: {player['rerolls']}")



    
#-------------------------
#OPEN NARRATION
#-------------------------

def introduction():
    input("\nPress Enter to begin...")
    
    print("\nIn the beginning, there was nothing.")
    input("\nPress enter to continue...")
    
    print("\nThen came the Ivory Light.")
    input("\nPress enter to continue...")
    
    print("\nAnd with that light, a blackness darker than the end itself.")
    input("\nPress enter to continue...")

    print("\nChapter One")

# -----------------------
# FUNERAL SCENE
# -----------------------

def funeral_scene(player):
    print("\nYou stand before the casket of your deceased best friend.")

    while True:
        print("\nWhat do you do?")
        print("1. Examine the casket.")
        print("2. Speak to a nearby mourner.")
        print("3. Look around the room.")
        print("4. Leave the funeral.")
        print("5. Check inventory.")
        print("6. Check clues.")

        choice = input("> ").strip()

        if choice == "1":
            print("\nYou approach the casket.")
            print(" Your friend's hands lie folded.")

            if not player["checked_casket"]:

                print("\n1. Examine his body more closely. [Wisdom - DC 13]")
                print("2. Step away from the casket")

                examine_choice = input("> ").strip()

                while examine_choice not in ("1", "2"):
                    examine_choice = input("Please enter 1 or 2: ").strip()

                if examine_choice == "1":

                    player["checked_casket"] = True

                    success = stat_check(player, "wisdom", 13)

                    if success:
                        print("\nYou notice a strange symbol on his wrist.")
                        player["clues"].append("strange symbol")
                        print("\nNew clue discovered!")

                    else:
                        print("\nYou examine his body carefully.")
                        print("Nothing unusual catches your attention.")

                else:
                    print("\nYou step away from the casket.")

            elif "strange symbol" in player["clues"]:
                print("\nYou remember the symbol on his wrist.")

            else:
                print("\nYou've already examined his body.")


        elif choice == "2":
            print("\nA mourner turns toward you.")
            print('"We worked together. He wasn\'t himself during those last few weeks."')

            if not player["questioned_mourner"]:

                print("\n1. Press them for more information. [Charisma - DC 12]")
                print("2. Return to the room.")

                conversation_choice = input("> ").strip()

                while conversation_choice not in ("1", "2"):
                    conversation_choice = input("Please enter 1 or 2: ").strip()

                if conversation_choice == "1":

                    player["questioned_mourner"] = True

                    success = stat_check(player, "charisma", 12)

                    if success:
                        print("\nThe mourner hesitates.")
                        print('"He was meeting someone in secret."')
                        print('"I don\'t know who, but he seemed frightened."')

                        player["clues"].append("secret meeting")
                        print("\nNew clue discovered!")

                    else:
                        print("\nThe mourner looks uncomfortable.")
                        print('"I really don\'t want to talk about it."')

                else:
                    print("\nYou return to the room.")

            elif "secret meeting" in player["clues"]:
                print("\nThe mourner has nothing more to tell you.")

            else:
                print("\nThe mourner avoids further questions.")

        elif choice == "3":
            print("\nSomeone stands alone near the exit, watching the room.")

            if "brass key" not in player["inventory"]:
                
                print("\nYou notice something beneath an empty chair.")
                print("It's a small brass key.")

                print("\n1. Pick up the key.")
                print("2. Leave it where it is.")

                item_choice = input("> ").strip()

                while item_choice not in ("1", "2"):
                    item_choice = input("Please enter 1 or 2: ").strip()

                if item_choice == "1":
                    player["inventory"].append("brass key")
                    print("\nBrass key added to inventory!")

                else:
                    print("\nYou leave the key where it is.")

            else:
                print("\nYou remember finding the brass key beneath the chair.")

        elif choice == "4":
            print("\nYou step outside.")
            return "street"

        elif choice == "5":
            show_inventory(player)

        elif choice == "6":
            show_clues(player)

        else:
            print("\nPlease enter 1, 2, 3, 4, 5, or 6.")

        

# ----------------------
# STREET SCENE
# ----------------------

def street_scene(player):

    input("\nPress enter to continue...")
    print("\nThe sun is bright...") 
    input("\nFocus...")
    print("\nYou stand in place for a short moment until your eyes adjust to the space around you.")

    while True:
        print("1. Look left.")
        print("2. Look right.")
        print("3. Look down.")
        print("4. Look ahead.")
        print("5. Check inventory.")
        print("6. Check clues.")

        choice = input("> ").strip()

        if choice == "1":
            print("\nYou see a crowd holding up signs and shouting.")

            print("1. Look closer.")
            print("2. Ignore.")

            engagement_choice = input("> ").strip()

            while engagement_choice not in ("1", "2"):
                engagement_choice = input("Please enter 1 or 2: ").strip()

            if engagement_choice == "1":
                print("\nYou notice they're holding up political signs condemning the president.")
        
        elif choice == "2":
            print("\nYou see cops in riot gear standing in the road.")
        
        elif choice == "3":
            print("\nA flyer with your friends face lie at your feet.")

            print("1. Pick it up.")
            print("2. Leave it to rot on the ground.")

            pick_up = input("> ").strip()

            while pick_up not in ("1", "2"):
                pick_up = input("Please enter 1 or 2: ").strip()

            if pick_up == "1":

                if "funeral flyer" not in player["inventory"]:
                    player["inventory"].append("funeral flyer")
                    print("\nFuneral flyer added to inventory.")

                else:
                    print("\nYou already collected the flyer.")
                    
        
        elif choice == "4":
            print("\nYou see a woman getting ready to cross the street.")
            
            input("\n...")
            input("\n...")
            input("\n...")
            
            print("\nYou see a car speeding toward her. "
                "She doesn't notice."
            )
                  

            print("1. Save her.")
            print("2. Stand in place.")

            save_her = input("> ").strip()

            while save_her not in ("1", "2"):
                save_her = input(
                    "Please enter 1 or 2: "
                ).strip()

            if save_her == "1":
                player["saved_woman"] = True


                print("\nYou rush toward the woman.")
                print("You push her out of the car's path.")
                print("The car speeds past you.") 

            else:
                player["saved_woman"] = False

                print("\nYou remain frozen in place.")
                print("At the last possible moment, the car swerves.")
                print("The woman stumbles and drops her belongings.")
                print("You approach and help her gather them.")

            print("\nThe woman looks toward you.")
            print("After a brief conversation, you offer to walk her home.")

            return "walk_home"
           
        elif choice == "5":
            show_inventory(player)

        elif choice == "6":
            show_clues(player)    

        else:
            print("\nPlease enter 1, 2, 3, 4, 5, or 6.")           


# -------------------
# WALK GOME SCENE
# -------------------               

def walk_home_scene(player):

    print("\nYou begin walking alongside the woman.")

    if player["saved_woman"]:
        print("\nShe looks at you.")
        print('"You could have been killed back there."')

    else:
        print("\nShe looks toward the street behind you.")
        print('"I thought that car was going to hit me."')

    print("\nThe two of you continue walking.")

    print('\n"Who was the funeral for?" she asks.')

    print('\n"My best friend," you reply.')

    print('\n"What did he look like?"')

    if "funeral flyer" in player["inventory"]:

        print("\nYou reach into your pocket.")
        print("You unfold the funeral flyer and show her his photograph.")

        print("\nShe studies the photograph for a moment.")
        print("Something about her expression changes.")

        player["clues"].append("woman recognized photograph")

        print("\nNew clue discovered!")

    else:

        print("\nYou describe your friend as best you can.")
        print("She listens quietly.")

        print('\n"I see," she says.')

    input("\nPress Enter to continue...")

    return "end"
# -------------------
# MAIN GAME LOOP
# -------------------

def main():
    player = create_character()

    introduction()

    current_scene = player["location"]

    while current_scene != "end":

        if current_scene == "funeral":
            current_scene = funeral_scene(player)

        elif current_scene == "street":
            current_scene = street_scene(player)

        elif current_scene == "walk_home":
            current_scene = walk_home_scene(player)

        else:
            print("Unknown scene.")
            break

        player["location"] = current_scene

    print("\nEnd of playable chapter")

# ------------------
# START PROGRAM
# ------------------
 
if __name__ == "__main__":
    main()    
            