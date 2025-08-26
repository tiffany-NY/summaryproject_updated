weapon_list = [{"name": "sword", "damage": 10, "health": 0},
            {"name": "kaboom spell", "damage": 10, "health": -5},
            {"name": "pinkie spell", "damage": 20, "health":-5},
            {"name": "wobuffet wall", "damage": 0, "health": 0}
]

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


potion_list = [{"name": "Mrs scowers all purpose maggi mee", "health": "x2", "max_health": "0", "default_power": "0", "chance": 50},
            {"name": "Wiggenweld juice", "health": "+10", "max_health": "0", "default_power": "0", "chance": 50},
            {"name": "Alicorn elixer", "health": "+20", "max_health": "+10", "default_power": "+10", "chance": 10},
            {"name": "Boosting salve", "health": "0", "max_health": "x2", "default_power": "0", "chance": 30},
            {"name": "Gigantamax powder", "health": "0", "max_health": "0", "default_power": "x2", "chance": 20}
]

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