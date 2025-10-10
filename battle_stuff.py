from character import Character, twilight
import items
import map
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
        choice = text.prompt_inline_choice(
            prompt="Would you like to equip a weapon or drink a potion before starting your battle?",
            options=["yes", "no"],
            prefix="> "
        )
        while choice != "cancel":
            text.clear_screen()
            twilight.display_inventory()
            print(text.DIVIDER)
            options = twilight.inventory.list_items()
            options.append("cancel")
            choice = text.prompt_numbered_choice(
                preamble="What would you like to use?",
                options=options,
            )
            if choice != 'cancel':
                twilight.use_item(choice)
            text.clear_screen()
            twilight.display_stats()
            print(text.DIVIDER)
        twilight.display_inventory()


def battle(enemy: Character) -> bool:
    """Displays and updates stats and health of Twilight before the battle starts and after each attack and 
    Prompts user to attack
    """
    text.clear_screen()
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

    if twilight.is_alive() and enemy.is_alive():
        input(text.ATTACK_PROMPT)
        return True
    else:
        if twilight.is_alive():
            text.clear_screen()
            print(text.FIGHT_WON)
        
        else:
            text.clear_screen()
            print(text.FIGHT_LOST)
        return False


def post_battle(enemy: Character) -> bool:
    """
    Prompts user to pick up items (potions, elements and weapons) dropped by the enemy after a battle
    If input == 'yes', updates and displays inventory, if input == 'no', continue the game
    """
    if twilight.is_alive():
        current = map.castle.current_location
        if None not in list(map.details[current]["item"]):
            text.prompt_loot(enemy.name)
            for item_name in map.details[current]["item"]:
                if item_name in items.weapon_data:
                    weapon = items.create_weapon(item_name)
                    print(text.DIVIDER)
                    weapon.display_weapon_stats()
                    choice = text.prompt_inline_choice(
                        prompt="do u wanna pick up the weapon?",
                        options=["yes", "no"],
                        prefix="> "
                    )
                    if choice == "yes":
                        twilight.pick_up(weapon)
                elif item_name in items.potion_data:
                    potion = items.create_potion(item_name)
                    print(text.DIVIDER)
                    potion.display_potion_stats()
                    choice = text.prompt_inline_choice(
                        prompt="do u wanna pick up the potion?",
                        options=["yes", "no"],
                        prefix="> "
                    )
                    if choice == "yes":
                        twilight.pick_up(potion)
                elif item_name in items.element_data:
                    element = items.create_element(item_name)
                    print(text.DIVIDER)
                    print(text.alert_element_found(element.name))
                    choice = text.prompt_inline_choice(
                        prompt="do u wanna pick up the element? (hint: u need it to win!!!!)",
                        options=["yes", "no"],
                        prefix="> "
                    )
                    if choice == "yes":
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
        text.clear_screen()
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
    post_battle(enemy)


def game_over():
    """checks if all elements have been collected, if all 6 collected, game is won and over"""
    if twilight.inventory.element_count == 6:
        print(text.DIVIDER)
        print(text.VICTORY)
        quit()