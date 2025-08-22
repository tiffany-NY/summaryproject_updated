import os
from character import Character, Higherup
from items import weapon, potion
import random
from battle_stuff import battle, twilight, enemy, before_battle
from desc import backstory, rules, item_info
from map import castle
from menu import clear, load, save, start, menu, rounds, continueing

run = True

HP = 100
power = 5
name = ""

while run:
    play = menu()

    while play:
        save()
        start()
        input("> click enter to move on ")
        clear()

        castle.show_current_location()
        input("> press enter to show stats and pick stuff up")
        before_battle()
        input("> press enter to start your battle ")
        rounds()
        
        continueing()