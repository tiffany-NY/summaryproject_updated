from character import Character, Higherup
from items import Weapon, Potion
import random
import os
from map import castle, details
from menu import clear

twilight = Higherup(name="Twilight", health=100, power=5, color="green")
weapon3 = Weapon("sword", 10, 0)
twilight.pick_up(weapon3)

def before_battle():
    """
    Displays the stats and inventory of Twilight and
    Prompts user to equip weapons or drink potions
    """
    print("-------------------")
    twilight.display_stats()
    print("-------------------")
    twilight.display_inventory()
    print("-------------------")
    choices = input("> would you like to equip a weapon or drink a potion before starting your battle? ")
    if choices == "yes":
        thing = input("> what would you like to use? or type 'cancel' to exit: ")  #add validation for str input
        # while int(thing) > twilight.own_inventory.count:
        #     thing = input("> what would you like to use? or type 'cancel' to exit: ")
        #     if thing == 'cancel':
        #         print("Equip operation cancelled.")
        #         break
        twilight.using_item(int(thing)-1)
        twilight.display_stats()
    twilight.display_inventory()


def battle(enemy):
    """
    Displays and updates stats and health of Twilight before the battle starts and after each attack and 
    Prompts user to attack
    """
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

def continueing(enemy):
    """
    Prompts user to pick up items (potions, elements and weapons) dropped by the enemy after a battle
    If input == 'yes', updates and displays inventory, if input == 'no', continue the game
    """
    if twilight.alive():
            print(f"oh look! {enemy.name} dropped an item!")
            input("> click enter to see what it is! ")
            current = castle.current_location
            
            if list(details[current]["item"].keys()) == ['weapon']:
                weapon = Weapon(details[current]["item"]["weapon"]["name"], details[current]["item"]["weapon"]["damage"], details[current]["item"]["weapon"]["health"])
                print(weapon.display_weapon_stats())
                item = weapon
            elif list(details[current]["item"].keys()) == ['potion']:
                potion = Potion(details[current]["item"]["potion"]["name"], details[current]["item"]["potion"]["health"], details[current]["item"]["potion"]["max_health"], details[current]["item"]["potion"]["default_power"])
                print(potion.display_potion_stats())
                item = potion
            elif list(details[current]["item"].keys()) == ['elements']:
                item = details[current]["item"]["elements"]
                print(f"congratulations! u found the {item}")

            heh = input("> do u wanna pick up the item? ")
            if heh == "yes":
                twilight.pick_up(item)
                twilight.display_inventory()
            
            input("> click enter to continue! ")
            clear()
            print("you can continue to move around the map!!!!!!!!!!!!")
            castle.move_location()
            castle.show_current_location()
    else:
        print("game over loser")
        quit() 

def at_each_place():
    """
    Displays current location
    Define stats of enemy
    Conducts battle
    """
    castle.show_current_location()

    current = castle.current_location
    enemy = Character(name=details[current]["enemy"][0], health=details[current]["enemy"][1], power=details[current]["enemy"][2], color="red")
    print(f"oh no {enemy.name} has appeared")
    before_battle()
    input("> press enter to start your battle ")
    battling = True
    while battling:
        battling = battle(enemy)
    continueing(enemy)