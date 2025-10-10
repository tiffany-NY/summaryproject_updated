from character import Character, twilight
import items
import map
import menu
import desc


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
        menu.clear()
        while choices == "yes":
            menu.clear()
            twilight.display_inventory()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            thing = input("> what would you like to use? or type 'cancel' to exit: ") 
            if thing == 'cancel':
                print('Equip operation cancelled.')
                print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                choices = -1
            else:
                twilight.using_item(int(thing)-1)
            menu.clear()
            twilight.display_stats()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        twilight.display_inventory()


def battle(enemy):
    """
    Displays and updates stats and health of Twilight before the battle starts and after each attack and 
    Prompts user to attack
    """
    menu.clear()
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
            menu.clear()
            print("yipee you won!")
        
        else:
            menu.clear()
            print("oh no you died")
        return False


def continueing(enemy):
    """
    Prompts user to pick up items (potions, elements and weapons) dropped by the enemy after a battle
    If input == 'yes', updates and displays inventory, if input == 'no', continue the game
    """
    if twilight.alive():
        current = map.castle.current_location
        if None not in list(map.details[current]["item"]):
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            print(f"oh look! {enemy.name} dropped an item!")
            input("> click enter to see what it is! ")

            for item_name in map.details[current]["item"]:
                try:
                    weapon = items.create_weapon(item_name)
                    print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                    print(weapon.display_weapon_stats())
                    option = input("> do u wanna pick up the weapon? (yes/no) ")
                    if option == "yes":
                        twilight.pick_up(weapon)
                except ValueError:
                    try:
                        potion = items.create_potion(item_name)
                        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                        print(potion.display_potion_stats())
                        option = input("> do u wanna pick up the potion? (yes/no) ")
                        if option == "yes":
                            twilight.pick_up(potion)
                    except ValueError:
                        element = items.create_element(item_name)
                        print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
                        print(f"congratulations! u found the {element.name}")
                        option = input("> do u wanna pick up the element? (hint: u need it to win!!!!) (yes/no) ")
                        if option == "yes":
                            twilight.pick_up(element)
                            map.details[current]["item"].remove(item_name)
                            game_over()

            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
            twilight.putting_back(twilight.weapon)
            twilight.display_inventory()
            print("𐙚⋆˚✿˖°~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~𐙚⋆˚✿˖°")
        else:
            print(f"awh man {enemy.name} did not drop anything :(")

        input("> click enter to continue! ")
        menu.clear()
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
    map.castle.show_current_location()
    current = map.castle.current_location
    enemy = Character(name=map.details[current]["enemy"][0], health=map.details[current]["enemy"][1], power=map.details[current]["enemy"][2], color="red")
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
        print(desc.winner)
        quit()