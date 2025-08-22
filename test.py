# import mud
# import menu
import map
# import main
from items import Weapon, Potion
from inventory import Inventory
# import desc
# import character
# import battle_stuff


def run_inventory_tests():
    """
    test the inventory class in inventory.py
    """
    print("Running Inventory tests...")

    inventory = Inventory()

    # Create some test objects
    sword = Weapon("sword", 10, 0)
    spell = Weapon("kaboom spell", 10, -5)
    potion = Potion("Wiggenweld juice", "+10", "0", "0")


    # Test adding items
    inventory.add_item(sword)
    inventory.add_item(spell)
    inventory.add_item(potion)
    assert inventory.count == 3, "Add item failed"

    # Test using an item
    equipped = inventory.use_item(sword)
    assert equipped == sword, "Use item did not return correct object"
    assert inventory.count == 2, "Count not updated after use"

    # Test dropping an item
    dropped = inventory.drop_item(spell)
    assert dropped is True, "Drop item failed"
    assert inventory.count == 1, "Count not updated after drop"

    # Final check: only potion should remain
    assert inventory.head.item == potion, "Wrong item left in inventory"
    assert inventory.head.next is None, "Extra items left in inventory"

    print("All inventory tests passed!")

run_inventory_tests()

def run_map_tests():
    """
    tests the map.py
    """
    # initializes the map
    try:
        map_dungeon = Map(map, 0, 0)
    except:
        print('An error occured while initializing the map.')
        raise AssertionError
    assert map_dungeon.show_current_location() == f'Your current location is (0, 0).', 'An error occured when printing the starting location.'
    map_dungeon.move_location()
    assert map_dungeon.display_map() == map, "An error occured when displaying the map"
    # Test the normal case of this
    game_map = Map(map, 1, 1)  # start at room5
    game_map.ycoord -= 1       # simulate north move
    game_map.current_location = map[game_map.ycoord][game_map.xcoord]
    assert game_map.current_location == "room2"

    game_map = Map(map, 1, 1)  # start at room5
    game_map.ycoord += 1       # simulate south move
    game_map.current_location = map[game_map.ycoord][game_map.xcoord]
    assert game_map.current_location == "room8"

    game_map = Map(map, 1, 1)  # start at room5
    game_map.xcoord += 1       # simulate east move
    game_map.current_location = map[game_map.ycoord][game_map.xcoord]
    assert game_map.current_location == "room6"

    game_map = Map(map, 1, 1)  # start at room5
    game_map.xcoord -= 1       # simulate west move
    game_map.current_location = map[game_map.ycoord][game_map.xcoord]
    assert game_map.current_location == "room4"

    