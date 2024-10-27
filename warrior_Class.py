from avatarClass import Avatar 
import random


class Warrior(Avatar):
    def __init__(self, name, life=100, power=20, magic=0, gold=6, potion=1) -> None:
        super().__init__(name=name, life=life, power=power, magic=magic, gold=gold, potion=potion)

    def salute(self):
        print("ARGH")

    def job_attack(self):
        if self.life < 41:
            damage = self.power*2
            print(f"{self.name} enters in rage!")
        else:
            damage = self.power
        return damage


