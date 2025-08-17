from character import Character, Higherup
from items import weapon, potion
import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

twilight = Higherup(name="Twilight", health=100, power=5, weapon=weapon, potion=None)
enemy = Character(name="enemy", health=100, power=10)

def round():
    active = True
    while active:
        clear()
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        twilight.display_stats()
        enemy.display_stats()
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        twilight.attack(enemy)
        enemy.attack(twilight)
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        print(f"\t\thealth of {twilight.name}: {twilight.health} / {twilight.health_max}")
        print(f"\t\thealth of {enemy.name}: {enemy.health} / {enemy.health_max}")
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")

        if twilight.alive() and enemy.alive():
            input("attack ah?")
        else:
            if twilight.alive():
                print("yipee u won")
            else:
                print("oh u died")
            active = False

round()