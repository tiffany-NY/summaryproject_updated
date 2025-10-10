import data

item_data = data.load_game_data()['items']

weapon_data = item_data['weapons']
potion_data = item_data['potions']
element_data = item_data['elements']


def create_weapon(name: str):
    """ Creates a weapon object from the given name and data dictionary """
    if name not in weapon_data:
        raise ValueError(f"Weapon {name!r} does not exist.")
    data = weapon_data[name]
    return Weapon(name, data['damage'], data['health'])

def create_potion(name: str):
    """ Creates a potion object from the given name and data dictionary """
    if name not in potion_data:
        raise ValueError(f"Potion {name!r} does not exist.")
    data = potion_data[name]
    return Potion(name, data['health'], data['max_health'], data['default_power'])

def create_element(name: str):
    """ Creates an element object from the given name and data dictionary """
    if name not in element_data:
        raise ValueError(f"Element {name!r} does not exist.")
    return Element(name)


class Weapon:
    def __init__(self, name: str, damage: int, health: int):
        self.name = name
        self.damage = damage
        self.health = health
        self.use = 0
    
    def wobuffet_use(self):
        """ returns the number of times wobuffet wall has been used"""
        self.use += 1

    def display_weapon_stats(self):
        """
        disply all the stats of the weapons
        """
        if self.name == "wobuffet wall":
            print(f"{self.name} --> Blocks enemy attacks(x2)") 
        
        elif self.health == 0:
            print(f"{self.name} --> Damage: + {self.damage} |") 
        
        else:
            print(f"{self.name} --> Damage: + {self.damage} | Health: {self.health} |") 


class Potion:
    def __init__(self, name, health, max_health, default_power):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.default_power = default_power

    def display_potion_stats(self):
        """
        disply all the stats of the potions
        """
        if self.name == "Alicorn elixer":
            print(f"{self.name} --> {self.health} health, {self.max_health} max health, {self.default_power} default power")
        elif len(self.health) > 1:
            print(f"{self.name} --> {self.health} health")
        elif len(self.max_health) > 1:
            print(f"{self.name} --> {self.max_health} max health")
        else:
            print(f"{self.name} --> {self.default_power} default power")


class Element:
    def __init__(self, element):
        self.name = element