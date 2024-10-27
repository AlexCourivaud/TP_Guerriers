from avatarClass import Avatar 
import random

class Thief(Avatar):
    def __init__(self, name, life=90, power=15, magic=0, gold=6, potion=1) -> None:
        super().__init__(name=name, life=life, power=power, magic=magic, gold=gold, potion=potion)

    def salute(self):
        print("Fufu je suis un ninja")


    def job_attack(self):
        if random.randint(1, 7) == 1:
            damage = self.power*2
            print(f"{self.name} dealt a critical hit!")
            print(f"With his dexterity and his luck, the thief stole 1 gold from his oponent!")
            self.gold += 1
        else:
            damage = self.power
        return damage
