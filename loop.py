import os
from character import Character, Higherup
from items import Weapon, Potion 
import random
from battle_stuff import battle, twilight, before_battle, continueing, at_each_place
from desc import backstory, rules, item_info
from map import castle, details
from menu import clear, load, save, start, menu

run = True

HP = 100
power = 5
name = ""

while run:
    start()
    play = menu()

    while play:
        #save()
        input("> click enter to move on ")
        clear()
        at_each_place()
        #save()

