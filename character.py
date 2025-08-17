from items import weapon, potion

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
        print(f"|| {self.name} || Power: {self.power} |")


class Higherup(Character):
    """u"""
    def __init__(self, name: str, health: int, power: int, weapon, potion):
        super().__init__(name, health, power)
        self.weapon = weapon
        self.potion = potion

    def attack(self, target):
        """ p """
        if self.weapon != None:
            damage = self.power + self.weapon.damage
            target.health -= (self.power + self.weapon.damage)
            target.health = max(target.health, 0)
            print(f"{self.name} did {damage} damage to {target.name}")
            if self.weapon.health != 0:
                self.health += self.weapon.health
                print(f"  #{self.weapon.name} caused {self.name} health to drop by {self.weapon.health}")
        else:
            target.health -= self.power
            target.health = max(target.health, 0)
            print(f"{self.name} did {self.power} damage to {target.name}")

    def display_stats(self):
        """
        disply all the stats to the player
        """
        if self.weapon != None:
            print(f"|| {self.name} || Power: {self.power} | Equipped: {self.weapon.name} |")
            self.weapon.display_weapon_stats()
        else:
            super().display_stats()

    def use_potion(self, potion):
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

    def pick_up(self, weapon, potion):
        pass

    def drop(self, weapon, potion):
        pass