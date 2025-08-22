import os
from character import Character, Higherup
from items import weapon, potion
import random
from battle_stuff import battle, twilight, enemy, before_battle

run = True
menu = True
play = False

HP = 100
power = 5
name = ""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def save():
    try:
        with open("load.txt", "w") as file:
            file.write(f"{name}\n{HP}\n{power}\n")
    except Exception as e:
        print(f"Error saving game: {e}")

def load():
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
    print("intro stuff teehee")
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")

def rounds():
    battling = True
    while battling:
        battling = battle()

while run:
    while menu:
        clear()
        print("1: New Game")
        print("2: Load Previous Game")
        print("3: Backstory")
        print("4: Quit")
        
        choice = input("> ")
        
        if choice == "1":
            clear()
            name = input("> What's your name: ")
            print(f"Welcome, {name}!")
            menu = False
            play = True
        
        elif choice == "2":
            if load():
                clear()
                print(f"Welcome back, {name}!!")
                menu = False
                play = True
            else:
                input("Press Enter to return to menu...")

        elif choice == "3":
            clear()
            print("lalala place name backstory stuff")
            input("\nPress Enter to return to menu")
            menu = True

        elif choice == "4":
            quit()

    while play:
        save()
        start()

        destination = input("> where u wanna go: ").strip().lower()
        if destination == "menu":
            play = False
            menu = True
        else:
            clear()
            print("imagine ur in a kitchen ahh .. things appear ahhhh")
            input("> press enter to show stats and pick stuff up")
            before_battle()
            input("> press enter to start your battle ")
            rounds()
            if twilight.alive():
                print("you can continue to move around the map!!!!!!!!!!!!")
                destination = input("> where u wanna go: ").strip().lower()
                if destination == "menu":
                    play = False
                    menu = True
                else:
                    rounds()
            else:
                print("game over loser")
                quit()