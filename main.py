from battle_stuff import at_each_place

from . import map, menu, text

run = True

HP = 100
power = 5
name = ""


while run:
    menu.show_intro()
    play = menu.main_menu_prompt()

    while play:
        menu.save_game()
        input("> click enter to move on ")
        text.clear_screen()
        at_each_place()
        map.castle.move_location()
        map.castle.show_current_location()

#left: data validation for all inputs and actually implement save feature properly
