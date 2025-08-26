from character import Character, Higherup
from items import Weapon, Potion, Element
import random
import os
from map import castle, details
from menu import clear

twilight = Higherup(name="Twilight", health=100, power=5, color="green")

def before_battle():
    """
    Displays the stats and inventory of Twilight and
    Prompts user to equip weapons or drink potions
    """
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.display_stats()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    twilight.display_inventory()
    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
    choices = input("> would you like to equip a weapon or drink a potion before starting your battle? ")
    while choices == "yes":
        thing = input("> what would you like to use? or type 'cancel' to exit: ") 
        if thing == 'cancel':
            print('Equip operation cancelled.')
        else:
            try:
                thing = int(thing)
            except:
                print('Please enter a valid input.')
                before_battle() #check
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
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            print(f"oh look! {enemy.name} dropped an item!")
            input("> click enter to see what it is! ")
            current = castle.current_location
            
            if 'weapon' in list(details[current]["item"].keys()):
                weapon = Weapon(details[current]["item"]["weapon"]["name"], details[current]["item"]["weapon"]["damage"], details[current]["item"]["weapon"]["health"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(weapon.display_weapon_stats())
                option = input("> do u wanna pick up the weapon? ")
                if option == "yes":
                    twilight.pick_up(weapon)

            if 'potion' in list(details[current]["item"].keys()):
                potion = Potion(details[current]["item"]["potion"]["name"], details[current]["item"]["potion"]["health"], details[current]["item"]["potion"]["max_health"], details[current]["item"]["potion"]["default_power"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(potion.display_potion_stats())
                option = input("> do u wanna pick up the potion? ")
                if option == "yes":
                    twilight.pick_up(potion)
            
            if 'elements' in list(details[current]["item"].keys()):
                elements = Element(details[current]["item"]["elements"])
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                print(f"congratulations! u found the {elements}")
                option = input("> do u wanna pick up the element? (hint: u need it to win!!!!) ")
                if option == "yes":
                    twilight.pick_up(elements)
            
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            twilight.putting_back(twilight.weapon)
            twilight.display_inventory()
            
            input("> click enter to continue! ")
            clear()
            print("you can continue to move around the map!!!!!!!!!!!!")
            return True

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


before_battle()
