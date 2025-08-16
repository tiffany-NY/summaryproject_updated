from character import Character, Higherup
from items import weapon
import random
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")

twilight = Higherup(name="Twilight", health=100, power=5, weapon=weapon)
enemy = Character(name="enemy", health=100, power=10)

twilight.display_stats()

round = True
while round:
    clear()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.display_stats()
    enemy.display_stats()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.attack(enemy)
    enemy.attack(twilight)
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    print(f"\t\thealth of {twilight.name}: {twilight.health}")
    print(f"\t\thealth of {enemy.name}: {enemy.health}")
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")

    if twilight.alive() and enemy.alive():
        input("attack ah?")
    else:
        if twilight.alive():
            print("yipee u won")
        else:
            print("oh u died")
        quit()