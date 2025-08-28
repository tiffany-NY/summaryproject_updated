from map import castle, Map, map
from character import Character, Higherup, twilight
from items import Weapon
from inventory import Inventory

twilight = Higherup("Twilight", 100, 20, 10)
castle.move_location()
castle.move_location()
castle.move_location()
castle.show_current_location()
sword = Weapon("Sword", 15, 100)  
twilight.pick_up(sword)
twilight.own_inventory.show_inventory()
