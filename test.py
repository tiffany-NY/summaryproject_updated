# import mud
# import menu
# import map
# import main
from items import Weapon, Potion
from inventory import Inventory
# import desc
# import character
# import battle_stuff


def run_inventory_tests():
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
    assert inventory.count == 3, "❌ Add item failed"

    # Test using an item
    equipped = inventory.use_item(sword)
    assert equipped == sword, "❌ Use item did not return correct object"
    assert inventory.count == 2, "❌ Count not updated after use"

    # Test dropping an item
    dropped = inventory.drop_item(spell)
    assert dropped is True, "❌ Drop item failed"
    assert inventory.count == 1, "❌ Count not updated after drop"

    # Final check: only potion should remain
    assert inventory.head.item == potion, "❌ Wrong item left in inventory"
    assert inventory.head.next is None, "❌ Extra items left in inventory"

    print("✅ All inventory tests passed!")

run_inventory_tests()