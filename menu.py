import os
from desc import backstory, rules, item_info

HP = 100
power = 5
name = ""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def save():
    """
    saves the file in the txt
    """
    try:
        with open("load.txt", "w") as file:
            file.write(f"{name}\n{HP}\n{power}\n")
    except Exception as e:
        print(f"Error saving game: {e}")

def load():
    """
    load the game data from the txt
    """
    global name, HP, power
    try:
        with open("load.txt", "r") as file:
            loaded = file.readlines()
            name = loaded[0].strip()
            HP = int(loaded[1].strip())
            power = int(loaded[2].strip())
        return True
    except FileNotFoundError:
        print("No saved game found.")
        return False
    except Exception as e:
        print(f"Error loading game: {e}")
        return False

def start():
    """
    introduction of game
    """
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    print("\t𐙚⋆˚✿˖° Castle of the Two Sisters 𐙚⋆˚✿˖°")
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    print(backstory)
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    input("> click enter to move on ")


def menu():
    """
    the menu panel in which player can choose to create a new game, load previous game, read th rules or quit the game
    """
    flag = True
    while flag:
        clear()
        print("1: New Game")
        print("2: Load Previous Game")
        print("3: Rules")
        print("4: Quit")
        choice = input("> ")
        
        if choice == "1":
            clear()
            name = input("> what's your name: ")
            print(f"Welcome, {name}!")
            flag = False
            return True
        
        elif choice == "2":
            if load():
                clear()
                print(f"Welcome back, {name}!!")
                flag = False
                return True
            else:
                input("> click enter to return to menu...")

        elif choice == "3":
            clear()
            print(rules)
            input("\n> click enter to return to menu...")
            flag = False

        elif choice == "4":
            quit()