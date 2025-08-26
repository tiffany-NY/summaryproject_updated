class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class Inventory:
    def __init__(self):
        self.head = None  # Start of the linked list
        self.count = 0

    def add_item(self, item):
        """
        Adds item to inventory and updates count.
        If inventory is full, prompts user to drop an item and only adds item if dropped successfully.
        """
        new_node = Node(item)
        if self.count >= 15:
            self.show_inventory()
            choice = input('> Your inventory is full. Would you like to remove some items? ')
            if choice == 'No':
                return

            removal = input("> What would you like to remove? ")
            if not self.drop_item(removal):
                print(f"{item} was not added.")
                return
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Go to the end
                current = current.next
            current.next = new_node
        self.count += 1
        print(f"{item.name} added to inventory.")

    def drop_item(self, item):
        """
        Attempt to drop item from the inventory.
        If not found, continously prompts user to retry or cancel.
        Returns True if an item was dropped, False if cancelled
        """
        while True:
            current = self.head
            prev = None
            while current:
                if current.item == item:
                    if prev:
                        prev.next = current.next
                    else:
                        self.head = current.next
                    self.count -= 1
                    print(f"{item.name} dropped from inventory.")
                    return True
                prev = current
                current = current.next

            print(f"{item.name} not found in inventory.")
            choice = input("Try again? Enter a new item name or type 'cancel' to exit: ").strip()
            if choice.lower() == 'cancel':
                print("Drop operation cancelled.")
                return False
            item = choice
    
    def use_item(self, indexs):
        """
        Equips item from the inventory.
        If not found, continuously prompt the user to retry or cancel.
        Returns the equipped item if successful, None if cancelled.
        """
        current = self.head
        prev = None
        i = 0
        while current:
            if i == indexs:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                self.count -= 1
                return current.item
            prev = current
            current = current.next
            i += 1
        return None

    def show_inventory(self):
        """
        display all the items in the inventory
        """
        current = self.head
        index = 1
        if not current:
            print("Inventory is empty.")
            return
        print(f'You have {self.count}/15 items in the inventory')
        print("Inventory:")
        while current:
            print(f"{index}: {current.item.name}")
            current = current.next
            index += 1
