class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        # Points to the next node

# Linked List Inventory
class Inventory:
    def __init__(self):
        self.head = None  # Start of the linked list
        self.count = 0

    def add_item(self, item):
        """
        adds the item in the inventory"""
        new_node = Node(item)
        if self.count > 15:
            self.show_inventory
            choice = input('Your inventory is full. Would you like to remove some items?')
            if choice == 'No':
                return
            else:
                self.remove_item(choice)
            
        else:
            if self.head is None:
                self.head = new_node
            else:
                current = self.head
                while current.next:  # Go to the end
                    current = current.next
                current.next = new_node
            self.count += 1
            print(f"{item} added to inventory.")

    def drop_item(self, item):
        """
        remove the item from the inventory
        """
        current = self.head
        prev = None
        while current:
            if current.item == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"{item} dropped from inventory.")
                self.count -= 1
                return
            prev = current
            current = current.next
        print(f"{item} not found in inventory.")

    def use_item(self, item):
        """
        equip the item in the hand
        """
        current = self.head
        prev = None
        while current:
            if current.item == item:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                print(f"{item} equipped")
                self.count -= 1
                return item
            prev = current
            current = current.next
        print(f"{item} not found in inventory.")

    def show_inventory(self):
        """
        display all the items in the inventory
        """
        current = self.head
        if not current:
            print("Inventory is empty.")
            return
        print(f'You have {self.count}/15 items in the inventory')
        print("Inventory:")
        while current:
            print(f"- {current.item}")
            current = current.next