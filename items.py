import random

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
            print(f"\t\t\t| {weapon.name} --> Blocks enemy attacks(x2)") 
        elif self.health == 0:
            print(f"\t\t\t| {weapon.name} --> Damage: + {self.damage} |") 
        else:
            print(f"\t\t\t| {weapon.name} --> Damage: + {self.damage} | Health: {self.health} |") 

weapon_list = [{"name": "sword", "damage": 10, "health": 0},
            {"name": "kaboom spell", "damage": 10, "health": -5},
            {"name": "pinkie spell", "damage": 20, "health":-5},
            {"name": "wobuffet wall", "damage": 0, "health": 0}
]

index = random.randint(0, len(weapon_list)-1)
chosen = weapon_list[index]
weapon = Weapon(chosen["name"], chosen["damage"], chosen["health"])
