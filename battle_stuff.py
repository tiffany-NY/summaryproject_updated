from character import Character, twilight
import items
import map
import menu
import text


def before_battle():
    """
    Displays the stats and inventory of Twilight and
    Prompts user to equip weapons or drink potions
    """
    print(text.DIVIDER)
    twilight.display_stats()
    print(text.DIVIDER)
    if twilight.inventory.count > 0:
        twilight.display_inventory()
        print(text.DIVIDER)
        choices = input("> would you like to equip a weapon or drink a potion before starting your battle? (yes/no) ")
        menu.clear_screen()
        while choices == "yes":
            menu.clear_screen()
            twilight.display_inventory()
            print(text.DIVIDER)
            thing = input("> what would you like to use? or type 'cancel' to exit: ") 
            if thing == 'cancel':
                print('Equip operation cancelled.')
                print(text.DIVIDER)
                choices = -1
            else:
                twilight.use_item(int(thing)-1)
            menu.clear_screen()
            twilight.display_stats()
            print(text.DIVIDER)
        twilight.display_inventory()


def battle(enemy):
    """
    Displays and updates stats and health of Twilight before the battle starts and after each attack and 
    Prompts user to attack
    """
    menu.clear_screen()
    print(text.DIVIDER)
    twilight.display_stats()
    enemy.display_stats()
    print(text.DIVIDER)
    twilight.attack(enemy)
    enemy.attack(twilight)

    print(text.DIVIDER)
    twilight.health_bar.draw()
    enemy.health_bar.draw()
    print(text.DIVIDER)

    if twilight.is_alive() and enemy.alive():
        input("> click enter to attack ")
        return True
    else:
        if twilight.is_alive():
            menu.clear_screen()
            print("yipee you won!")
        
        else:
            menu.clear_screen()
            print("oh no you died")
        return False


def continueing(enemy):
    """
    Prompts user to pick up items (potions, elements and weapons) dropped by the enemy after a battle
    If input == 'yes', updates and displays inventory, if input == 'no', continue the game
    """
    if twilight.is_alive():
        current = map.castle.current_location
        if None not in list(map.details[current]["item"]):
            print(text.DIVIDER)
            print(f"oh look! {enemy.name} dropped an item!")
            input("> click enter to see what it is! ")

            for item_name in map.details[current]["item"]:
                try:
                    weapon = items.create_weapon(item_name)
                    print(text.DIVIDER)
                    print(weapon.display_weapon_stats())
                    option = input("> do u wanna pick up the weapon? (yes/no) ")
                    if option == "yes":
                        twilight.pick_up(weapon)
                except ValueError:
                    try:
                        potion = items.create_potion(item_name)
                        print(text.DIVIDER)
                        print(potion.display_potion_stats())
                        option = input("> do u wanna pick up the potion? (yes/no) ")
                        if option == "yes":
                            twilight.pick_up(potion)
                    except ValueError:
                        element = items.create_element(item_name)
                        print(text.DIVIDER)
                        print(f"congratulations! u found the {element.name}")
                        option = input("> do u wanna pick up the element? (hint: u need it to win!!!!) (yes/no) ")
                        if option == "yes":
                            twilight.pick_up(element)
                            map.details[current]["item"].remove(item_name)
                            game_over()

            print(text.DIVIDER)
            twilight.unequip(twilight.weapon)
            twilight.display_inventory()
            print(text.DIVIDER)
        else:
            print(f"awh man {enemy.name} did not drop anything :(")

        input("> click enter to continue! ")
        menu.clear_screen()
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
    if twilight.inventory.element_count == 6:
        print(text.DIVIDER)
        print(text.VICTORY)
        quit()