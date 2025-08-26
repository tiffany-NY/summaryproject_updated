from items import Weapon, Potion
from inventory import Inventory
from health_bar import HealthBar

class Character:
    def __init__(self, name: str, health: int, power: int, color):
        self.name = name
        self.health = health
        self.health_max = health
        self.power = power
        self.health_bar = HealthBar(self, color=color)

    def alive(self):
        """Returns True if character is alive"""
        return self.health > 0

    def attack(self, target):
        """Reduces target health when attacking unless target uses a shield and shield is only valid for 2 times use"""
        if target.weapon:
            if target.weapon.name == "wobuffet wall" and target.weapon.use < 2:
                print(f"{self.name} attack got blocked by {target.weapon.name}")
                target.weapon.wobuffet_use()
            else:
                if target.weapon.name == "wobuffet wall" and target.weapon.use >= 2:
                    print("  #wobuffet wall has been completely used")
 
        target.health -= self.power
        target.health = max(target.health, 0)
        target.health_bar.update()
        print(f"{self.name} did {self.power} damage to {target.name}")

    def display_health(self):
        pass
    
    def display_stats(self):
        """Disply all of character stats """
        print(f"|| {self.name} || Power: {self.power} |")


class Higherup(Character):
    def __init__(self, name: str, health: int, power: int, color):
        super().__init__(name, health, power, color)
        self.weapon = None
        self.potion = None
        self.own_inventory = Inventory()

    def attack(self, target):
        """Reduces target health when attacking, total damage is default power and weapon if equipped"""
        if self.weapon != None:
            damage = self.power + self.weapon.damage
            target.health -= (self.power + self.weapon.damage)
            target.health = max(target.health, 0)
            target.health_bar.update()
            print(f"{self.name} did {damage} damage to {target.name}")
            if self.weapon.health != 0:
                self.health += self.weapon.health
                print(f"  #{self.weapon.name} caused {self.name} health to drop by {self.weapon.health}")
        else:
            target.health -= self.power
            target.health = max(target.health, 0)
            target.health_bar.update()
            print(f"{self.name} did {self.power} damage to {target.name}")

    def display_stats(self):
        """ disply all of character stats, including weapon if equipped """
        if self.weapon != None:
            print(f"|| {self.name} || Power: {self.power} | Equipped: {self.weapon.name} |")
            self.weapon.display_weapon_stats()
        else:
            super().display_stats()

    def use_potion(self, potion):
        """Changes the corressponding stats according to potion description"""
        if self.potion.health[0] == "+":
            self.health = min(self.health + int(self.potion.health[1:]), self.health_max)
        elif self.potion.health[0] == "x":
            self.health = min(self.health * int(self.potion.health[1:]), self.health_max)

        if self.potion.max_health[0] == "+":
            self.health_max += int(self.potion.max_health[1:])
        elif self.potion.max_health[0] == "x":
            self.health_max *= int(self.potion.max_health[1:])
            
        if self.potion.default_power[0] == "+":
            self.power += int(self.potion.default_power[1:])
        elif self.potion.default_power[0] == "x":
            self.power *= int(self.potion.default_power[1:])

    def using_item(self, index):
        """uses item"""
        holder = self.own_inventory.use_item(index)
        if isinstance(holder, Weapon):
            self.weapon = holder
        if isinstance(holder, Potion):
            self.potion = holder
            self.use_potion(holder)

    def putting_back(self, item):
        """ unequiping item and putting it back in inventory"""
        if isinstance(item, Weapon):
            self.weapon = None
            self.own_inventory.add_item(item)
        else:
            return
        
    def pick_up(self, item):
        """Adds item into inventory"""
        self.own_inventory.add_item(item)

    def drop(self, item):
        """Drops item from inventory"""
        self.own_inventory.drop_item(item)

    def display_inventory(self):
        """
        displays the inventory
        """
        self.own_inventory.show_inventory()