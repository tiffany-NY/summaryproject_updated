import os
from character import Character, Higherup, twilight
from items import Weapon, Potion 
import random
from battle_stuff import battle, before_battle, continueing, at_each_place, game_over
from desc import backstory, rules, item_info
from map import castle, details, unlock
from menu import clear, load, save, start, menu

run = True

HP = 100
power = 5
name = ""

while run:
    start()
    play = menu()

    while play:
        save()
        input("> click enter to move on ")
        clear()
        at_each_place()
        castle.move_location()
        castle.show_current_location()

#left: data validation for all inputs and actually implement save feature properly