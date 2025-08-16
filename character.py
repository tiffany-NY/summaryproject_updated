import items

class Character:
    """e"""

    def __init__(self, name: str, health: int, power: int):
        self.name = name
        self.health = health
        self.health_max = health
        self.power = power

    def alive(self):
        """ e"""
        return self.health > 0

    def attack(self, target):
        """ p """
        if target.weapon.name == "wobuffet wall" and target.weapon.use < 2:
            print(f"{self.name} attack got blocked by {target.weapon.name}")
            target.weapon.wobuffet_use()
        else:
            if target.weapon.name == "wobuffet wall" and target.weapon.use >= 2:
                print("  #wobuffet wall has been completely used")
            target.health -= self.power
            target.health = max(target.health, 0)
            print(f"{self.name} did {self.power} damage to {target.name}")

    #def display_health(self):
        #pass #health bar hehe
    
    def display_stats(self):
        """
        disply all the stats to the player
        """
        print(f"|| {self.name} || Power: {self.power}")


class Higherup(Character):
    """u"""
    def __init__(self, name: str, health: int, power: int, weapon):
        super().__init__(name, health, power)
        self.weapon = weapon

    def attack(self, target):
        """ p """
        damage = self.power + self.weapon.damage
        target.health -= (self.power + self.weapon.damage)
        target.health = max(target.health, 0)
        print(f"{self.name} did {damage} damage to {target.name}")
        if self.weapon.health != 0:
            self.health += self.weapon.health
            print(f"  #{self.weapon.name} caused {self.name} health to drop by {self.weapon.health}")

    def display_stats(self):
        """
        disply all the stats to the player
        """
        print(f"|| {self.name} || Power: {self.power} | Equipped: {self.weapon.name} |")
        self.weapon.display_weapon_stats()
