from character import Character, Higherup, twilight
from items import Weapon, Potion, Element
import random
import os
from map import castle, details
from menu import clear
from desc import winner


def before_battle():
    """
    Displays the stats and inventory of Twilight and
    Prompts user to equip weapons or drink potions
    """
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.display_stats()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    if twilight.own_inventory.count > 0:
        twilight.display_inventory()
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        choices = input("> would you like to equip a weapon or drink a potion before starting your battle? (yes/no) ")
        clear()
        while choices == "yes":
            clear()
            twilight.display_inventory()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            thing = input("> what would you like to use? or type 'cancel' to exit: ") 
            if thing == 'cancel':
                print('Equip operation cancelled.')
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                choices = -1
            else:
                twilight.using_item(int(thing)-1)
            clear()
            twilight.display_stats()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
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
        input("> click enter to attack ")
        return True
    else:
        if twilight.alive():
            clear()
            print("yipee you won!")
        
        else:
            clear()
            print("oh no you died")
        return False


def continueing(enemy):
    """
    Prompts user to pick up items (potions, elements and weapons) dropped by the enemy after a battle
    If input == 'yes', updates and displays inventory, if input == 'no', continue the game
    """
    if twilight.alive():
        current = castle.current_location
        if None not in list(details[current]["item"].values()):
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            print(f"oh look! {enemy.name} dropped an item!")
            input("> click enter to see what it is! ")
            
            if 'weapon' in list(details[current]["item"].keys()):
                weapon = Weapon(details[current]["item"]["weapon"]["name"], details[current]["item"]["weapon"]["damage"], details[current]["item"]["weapon"]["health"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(weapon.display_weapon_stats())
                option = input("> do u wanna pick up the weapon? (yes/no) ")
                if option == "yes":
                    twilight.pick_up(weapon)

            if 'potion' in list(details[current]["item"].keys()):
                potion = Potion(details[current]["item"]["potion"]["name"], details[current]["item"]["potion"]["health"], details[current]["item"]["potion"]["max_health"], details[current]["item"]["potion"]["default_power"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(potion.display_potion_stats())
                option = input("> do u wanna pick up the potion? (yes/no) ")
                if option == "yes":
                    twilight.pick_up(potion)
                
            
            if 'elements' in list(details[current]["item"].keys()):
                elements = Element(details[current]["item"]["elements"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(f"congratulations! u found the {elements.name}")
                option = input("> do u wanna pick up the element? (hint: u need it to win!!!!) (yes/no) ")
                if option == "yes":
                    twilight.pick_up(elements)
                    details[current]["item"]["elements"] = None
                    game_over()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            twilight.putting_back(twilight.weapon)
            twilight.display_inventory()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        else:
            print(f"awh man {enemy.name} did not drop anything :(")

        input("> click enter to continue! ")
        clear()
        print("you can continue to move around the map!")
        return True

    else:
        print("game over...thanks for playing tho!")
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


def game_over():
    """checks if all elements have been collected, if all 6 collected, game is won and over"""
    if twilight.own_inventory.element_count == 6:
        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        print(winner)
        quit()