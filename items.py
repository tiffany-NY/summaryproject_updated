import data

item_data = data.load_game_data()['items']

weapon_list = item_data['weapons']
potion_list = item_data['potions']


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