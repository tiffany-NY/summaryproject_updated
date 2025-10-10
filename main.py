import os
import random

from battle_stuff import at_each_place

from . import map, menu

run = True

HP = 100
power = 5
name = ""


while run:
    menu.start()
    play = menu.menu()

    while play:
        menu.save()
        input("> click enter to move on ")
        menu.clear()
        at_each_place()
        map.castle.move_location()
        map.castle.show_current_location()

#left: data validation for all inputs and actually implement save feature properly
