from character import Character, Higherup
from items import Weapon, weapon, potion, Potion
import random
import os
from map import castle

def clear():
    os.system("cls" if os.name == "nt" else "clear")

twilight = Higherup(name="Twilight", health=100, power=5, color="green")
enemy = Character(name="enemy", health=100, power=10, color="red")


def before_battle():
    twilight.display_stats()
    print(potion.name, weapon.name)
    heh = input("> do u wanna pick up the weapon and potion? ")
    if heh == "yes":
        twilight.pick_up(weapon)
        twilight.pick_up(potion)
        twilight.display_inventory()
    print("----------")
    twilight.using_item(weapon)
    twilight.display_stats()
    twilight.display_inventory()

def rounds():
    battling = True
    while battling:
        battling = battle()

def battle():
    clear()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.display_stats()
    enemy.display_stats()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.attack(enemy)
    enemy.attack(twilight)

    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.health_bar.draw()
    enemy.health_bar.draw()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")

    if twilight.alive() and enemy.alive():
        input("attack ah?")
        return True
    else:
        if twilight.alive():
            clear()
            print("yipee u won !!!")
        
        else:
            clear()
            print("oh u died")
        return False

def continueing():
    if twilight.alive():
            print("you can continue to move around the map!!!!!!!!!!!!")
            castle.move_location()
            castle.show_current_location()
    else:
        print("game over loser")
        quit() 