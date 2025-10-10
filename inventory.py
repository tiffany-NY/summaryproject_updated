import items


class Inventory:
    def __init__(self):
        self.items = {}  # Dictionary to store items with name as key and item as value
        self.item_counts = {}  # Dictionary to track the count of each item type

    def add_item(self, item: object) -> None:
        """
        Adds item to inventory and updates count.
        If inventory is full, prompts user to drop an item and only adds item if dropped successfully.
        """
        if self.is_full():
            raise ValueError("Inventory is full.")
        if item.name in self.items:
            self.item_counts[item.name] += 1
        else:
            self.items[item.name] = item
            self.item_counts[item.name] = 1

        if isinstance(item, items.Element):
            self.element_count += 1
        print(f"{item.name} added to inventory.")

    def count_elements(self) -> int:
        """ Returns the total number of elements in the inventory """
        return sum(
            1 for item in self.items.values()
            if isinstance(item, items.Element)
        )

    def count_items(self) -> int:
        """ Returns the total number of items in the inventory """
        return sum(self.item_counts.values())

    def drop_item(self, item_name: str) -> None:
        """Drop item from the inventory."""
        if not self.has_item(item_name):
            raise ValueError(f"Item {item_name!r} not found in inventory.")
        self.item_counts[item_name] -= 1
        if self.item_counts[item_name] == 0:
            del self.items[item_name]
            del self.item_counts[item_name]

    def has_item(self, item_name: str) -> bool:
        """ Check if the inventory contains a specific item """
        return item_name in self.items
    
    def is_empty(self) -> bool:
        """ Check if the inventory is empty """
        return bool(self.items)
    
    def is_full(self) -> bool:
        """ Check if the inventory is full """
        return self.count_items() >= 15

    def list_items(self) -> list:
        """ Returns a list of items in the inventory """
        return list(self.items.values())

    def use_item(self, item_name: str) -> object:
        """Equips item from the inventory.
        If not found, continuously prompt the user to retry or cancel.
        Returns the equipped item if successful, None if cancelled.
        """
        if not self.has_item(item_name):
            raise ValueError(f"Item {item_name!r} not found in inventory.")
        self.item_counts[item_name] -= 1
        if self.item_counts[item_name] == 0:
            return self.items.pop(item_name)
        return self.items[item_name]

    def show_inventory(self) -> None:
        """
        Display all the items in the inventory
        """
        if self.is_empty():
            print("Inventory is empty.")
            return
        print(f'You have {self.count_items()}/15 items in the inventory')
        print("Inventory:")
        for name, count in self.item_counts.items():
            print(f"{name}: {count}")
