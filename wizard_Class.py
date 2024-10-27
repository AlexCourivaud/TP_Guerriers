from avatarClass import Avatar 
import random

class Wizard(Avatar):
    def __init__(self, name, life=70, power=10, magic=100, gold=6, potion=1) -> None:
        super().__init__(name=name, life=life, power=power, magic=magic, gold=gold, potion=potion)

    def salute(self):
        print("Fufu je suis un magifien")

    def job_attack(self):
        if self.magic > 29:
            print(f"{self.name} cast a fireBall !")
            damage = self.power*3
            self.magic -= 30
        else:
            damage = self.power
            print(f"{self.name} do not have enough magic to cast a spell! So he attacks with his wand!")
        return damage
