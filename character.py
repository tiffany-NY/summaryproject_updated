from items import Weapon, Potion
from inventory import Inventory
import items
from health_bar import HealthBar
import data
import text

monster_data = data.load_game_data()['monsters']
player_data = data.load_game_data()['player']


def create_enemy(name: str) -> "Character":
    """Creates an enemy character from the monster data."""
    if name not in monster_data:
        raise ValueError(f"Monster {name!r} does not exist.")
    data = monster_data[name]
    return Character(
        name,
        data['health'],
        data['damage'],
        color="red"
    )

def create_player() -> "Player":
    """Creates the player character from the player data."""
    return Player(
        player_data['name'],
        player_data['health'],
        player_data['power'],
        player_data['color']
    )


class Character:
    """ Represents a character in the game."""

    def __init__(self, name: str, health: int, power: int, color):
        self.name = name
        self.health = health
        self.health_max = health
        self.power = power
        self.health_bar = HealthBar(self, color=color)

    def is_alive(self):
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


class Player(Character):
    """A character with an inventory, and can equip a weapon and potion."""

    def __init__(self, name: str, health: int, power: int, color):
        super().__init__(name, health, power, color)
        self.weapon: items.Weapon | None = None
        self.potion: items.Potion | None = None
        self.inventory = Inventory()

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
            self.weapon.display_stats()
        else:
            super().display_stats()

    def use_item(self, item_name: str) -> None:
        """Applies an item chosen from the inventory."""
        item = self.inventory.use_item(item_name)
        if isinstance(item, items.Element):
            print("Cannot use element.")
        self.equip(item.name)
        if isinstance(item, items.Potion):
            self.use_potion()

    def use_potion(self) -> None:
        """Changes the corressponding stats according to potion description"""
        if self.potion is None:
            return
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

    def equip(self, item_name: str):
        """equipping item and removing it from inventory"""
        if not self.inventory.has_item(item_name):
            raise ValueError(f"Item {item_name!r} not found in inventory.")
        item = self.inventory.use_item(item_name)
        if isinstance(item, Weapon):
            if self.weapon is None:
                self.weapon = item
                print(f"{item.name} has been equipped")
                return
            choice = text.prompt_inline_choice(
                prompt="you already equipped a weapon. Are you sure you want to change? you can only equip one",
                options=["yes", "no"]
            )
            if choice == "yes":
                self.unequip(self.weapon)
                self.weapon = item
                print(f"{item.name} has been equipped")
            elif choice == "no":
                self.inventory.add_item(item)
        elif isinstance(item, Potion):
            self.unequip(self.potion)
            self.potion = item

    def unequip(self, item: items.Weapon | items.Potion) -> None:
        """ unequiping item and putting it back in inventory"""
        if item is self.weapon:
            self.weapon = None
            self.inventory.add_item(item)
        elif item is self.potion:
            self.potion = None
            self.inventory.add_item(item)
        else:
            raise ValueError(f"Item {item!r} is not equipped.")
        print(f"{item.name} has been added back into the inventory")

    def pick_up(self, item: items.Item) -> None:
        """Adds item into inventory"""
        self.inventory.add_item(item)

    def display_inventory(self):
        """
        displays the inventory
        """
        self.inventory.show_inventory()
